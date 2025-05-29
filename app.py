import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope of the API access
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Use the downloaded JSON key file here
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

# Open your Google Sheet by name
sheet = client.open("Samplesheet").sheet1

# Example data to write
data = [
    ["user_id", "course_id", "completion_percent", "last_activity"],
    [1, 101, 80, "2025-05-20"],
    [2, 102, 60, "2025-05-21"],
]

# Clear existing data and append rows
sheet.clear()
for row in data:
    sheet.append_row(row)

print("✅ Data written to sheet.")
