# 📊 Madduck Data Case Study – App Store Lead Filtering Script  

💡 **Filter App Store data • 🎯 Exclude Deal List apps • ⏳ Check release & update dates • 👨‍💻 Deduplicate by developer**  

---

## 📌 About the Project  

This project contains a Python script that processes App Store metadata and filters apps to make them suitable for CRM lead generation.  
It takes an **App List** and a **Deal List** from an Excel file, fetches metadata from the App Store API, applies filtering rules, and saves the results into a CSV file.  

> ✅ Fetch metadata from App Store API  
> ✅ Exclude apps already in Deal List  
> ✅ Filter by Release Date and Last Update Date  
> ✅ Deduplicate apps so only one app per developer remains  
> ✅ Reusable script with `argparse` for terminal execution  

---

## 🔧 Technologies Used  

| Technology/Library  | Purpose |
|---------------------|---------|
| 🐍 Python           | Development language |
| 📑 Pandas           | Data processing |
| 🌍 Requests         | API requests |
| ⏱️ Datetime         | Date handling |
| 🖥️ Argparse         | CLI parameter handling |

---

## 📁 Project Structure  

🔧 Tech Stack
| Technology/Library | Purpose              |
| ------------------ | -------------------- |
| 🐍 Python          | Development language |
| 📑 Pandas          | Data processing      |
| 🌍 Requests        | App Store API calls  |
| ⏱️ Datetime        | Date filtering       |
| 🖥️ Argparse       | CLI argument parsing |


## 📁 Folder / File Structure

📦 madduck_data_case
 ┣ 📜 script.py              # Main Python script
 ┣ 📊 Madduck Data Case.xlsx # Input file (App List & Deal List)
 ┣ 📑 filtered_leads.csv     # Output (filtered apps)


## 🚀 Installation & Usage

## Run the script from the terminal:

python script.py --input "Madduck Data Case Study Data Files.xlsx" --output "filtered_leads.csv"

## Parameters
--input → Path to the Excel file (App List & Deal List)

--output → Output CSV file (default: filtered_leads.csv)

python script.py --input "Madduck Data Case Study Data.xlsx" --output "result.csv"

python script.py --input "another_file.xlsx" --output "filtered.csv"


