from datetime import datetime, timedelta

# this function for ceate a .ics file
def create_ics(events, filename='moveToiCalendar.ics'):
    with open(filename, 'w') as f:
        f.write("BEGIN:VCALENDAR\n")
        f.write("VERSION:2.0\n")
        f.write("PRODID:-//Your Company//NONSGML v1.0//EN\n")

        for event in events:
            start_time = datetime.strptime(event['date'] + " " + event['time'], '%Y-%m-%d %H:%M')
            start = start_time.strftime('%Y%m%dT%H%M%S')
            end = (start_time + timedelta(hours=1)).strftime('%Y%m%dT%H%M%S')  

            f.write("BEGIN:VEVENT\n")
            f.write(f"UID:{start}@yourdomain.com\n")
            f.write(f"SUMMARY:{event['title']}\n")
            f.write(f"DTSTART:{start}Z\n")
            f.write(f"DTEND:{end}Z\n")
            f.write("LOCATION:Online\n")
            f.write("END:VEVENT\n")

        f.write("END:VCALENDAR\n")

# Example data from web scraping
events = [
    {'title': 'GDP Report', 'time': '17:00', 'date': '2025-01-25'},
    {'title': 'Inflation Data', 'time': '19:00', 'date': '2025-01-25'}
]

# create the .ics file
create_ics(events)
print("ไฟล์ .ics ถูกสร้างแล้ว!")
