📊 Madduck Data Case Study – App Store Lead Filtering Script

💡 Filter App Store data • 🎯 Exclude Deal List • ⏳ Check recent updates • 👨‍💻 Deduplicate apps by developer

📌 About the Project

This project provides a Python script designed to process App Store data and make it suitable for integration into a CRM system.
The script ingests an App List and a Deal List, fetches metadata from the App Store API, applies filtering rules, and outputs the final result as a CSV file.

✅ Fetch metadata via App Store API
✅ Exclude apps listed in the Deal List
✅ Apply release date & last update date filters
✅ Deduplicate results by developer (only one app per developer)
✅ Reusable command-line script with argparse

🔧 Tech Stack
| Technology/Library | Purpose              |
| ------------------ | -------------------- |
| 🐍 Python          | Development language |
| 📑 Pandas          | Data processing      |
| 🌍 Requests        | App Store API calls  |
| ⏱️ Datetime        | Date filtering       |
| 🖥️ Argparse       | CLI argument parsing |


📁 Folder / File Structure

📦 madduck_data_case
 ┣ 📜 script.py              # Main Python script
 ┣ 📊 Madduck Data Case.xlsx # Input file (App List & Deal List)
 ┣ 📑 filtered_leads.csv     # Output (filtered apps)


🚀 Installation & Usage

Run the script from the terminal:

python script.py --input "Madduck Data Case Study Data Files.xlsx" --output "filtered_leads.csv"

Parameters

--input → Path to the Excel file (App List & Deal List)

--output → Output CSV file (default: filtered_leads.csv)

python script.py --input "Madduck Data Case Study Data.xlsx" --output "result.csv"
python script.py --input "another_file.xlsx" --output "filtered.csv"


