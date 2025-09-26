import argparse
import pandas as pd
import requests
import time
from datetime import datetime, timedelta, timezone

def load_app_ids(excel_path, sheet_name="App List"):
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    return df["app_id"].dropna().astype(str).tolist()

def load_deal_list(excel_path, sheet_name="Deal List"):
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    return set(df["app_id"].dropna().astype(str).tolist())

def fetch_metadata(app_ids):
    """
    App Store API'den 200'erli batch halinde metadata çek
    """
    results = []
    base_url = "https://itunes.apple.com/lookup?country=us&id="
    for i in range(0, len(app_ids), 200):
        chunk = app_ids[i:i+200]
        url = base_url + ",".join(chunk)
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json().get("results", [])
            results.extend(data)
        time.sleep(1)  # API rate limit
    return results

def json_to_df(results):
    """
    JSON response → DataFrame (istenen alanlar)
    """
    mapped = []
    for app in results:
        mapped.append({
            "app_id": app.get("trackId"),
            "app_name": app.get("trackName"),
            "developer_id": app.get("artistId"),
            "developer_account_name": app.get("artistName"),
            "price": app.get("price"),
            "rating": app.get("averageUserRating"),
            "rating_count": app.get("userRatingCount"),
            "primary_category": app.get("primaryGenreName"),
            "version": app.get("version"),
            "release_date": app.get("releaseDate"),
            "description": app.get("description"),
            "last_update_date": app.get("currentVersionReleaseDate")
        })
    df = pd.DataFrame(mapped)
    # Tarih kolonlarını datetime yap
    for col in ["release_date", "last_update_date"]:
        df[col] = pd.to_datetime(df[col], errors="coerce", utc=True)
    return df

def apply_filters(df, deal_list):
    today = datetime.now(timezone.utc)
    twelve_months_ago = today - timedelta(days=365)
    three_months_ago = today - timedelta(days=90)

    # 1) Deal list'te olanları çıkar
    df = df[~df["app_id"].astype(str).isin(deal_list)]

    # 2) Release date son 12 ay içinde olmalı
    df = df[df["release_date"] >= twelve_months_ago]

    # 3) Son update 3 aydan eski olmamalı
    df = df[df["last_update_date"] >= three_months_ago]

    # 4) Her developer'dan sadece 1 app
    df = df.sort_values("last_update_date", ascending=False)
    df = df.drop_duplicates(subset=["developer_id"], keep="first")

    return df


#  Ana Script

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Excel dosya path")
    parser.add_argument("--output", default="filtered_leads.csv", help="Çıktı CSV path")
    args = parser.parse_args()

    # Excel'den app_id ve deal list oku
    app_ids = load_app_ids(args.input, "App List")
    deal_list = load_deal_list(args.input, "Deal List")
    print(f"{len(app_ids)} app_id yüklendi. Deal List: {len(deal_list)} kayıt")

    # API'den metadata çek
    results = fetch_metadata(app_ids)
    print(f"API'den {len(results)} uygulama bilgisi çekildi.")

    # JSON → DataFrame
    df = json_to_df(results)

    # Filtreleri uygula
    filtered_df = apply_filters(df, deal_list)
    print(f"Filtre sonrası {len(filtered_df)} uygulama kaldı.")

    # CSV yaz
    filtered_df.to_csv(args.output, index=False)
    print(f"Sonuç kaydedildi: {args.output}")

if __name__ == "__main__":
    main()
