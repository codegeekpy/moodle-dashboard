# 📊 LMS Dashboard Automation

This project automates the collection and visualization of student engagement data from a Moodle-based LMS (Learning Management System). It fetches data via API or pre-exported files, updates a connected Google Sheet daily via GitHub Actions, and displays insights through a Streamlit dashboard.

---

## 🚀 Features

- 📥 Daily data extraction from the LMS API or CSV.
- 🔄 Automated upload to Google Sheets using `gspread` + GitHub Actions.
- 📅 Scheduled task runs every day at 7 AM UTC.
- 📊 Interactive and clean dashboard using Streamlit.
- 🔐 Secure secrets management using GitHub Actions and base64-encoded credentials.

---

## ⚙️ Tech Stack

- **Python**: Data extraction, transformation, and visualization.
- **Pandas**: Data cleaning and preprocessing.
- **gspread + oauth2client**: Google Sheets API integration.
- **GitHub Actions**: Automates the script daily.
- **Streamlit**: Visualization dashboard.
- **Google Cloud**: Service account + Google Sheets API.

---

#Google Sheets Setup

Create a new Google Cloud project.

Enable Google Sheets API.

Create a Service Account and generate a key in JSON format.

Rename the file to creds.json and do not commit it.

Share your Google Sheet with the service account email (xyz@project.iam.gserviceaccount.com).



