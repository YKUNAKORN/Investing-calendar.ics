from datetime import datetime, timedelta

# ฟังก์ชันสร้างไฟล์ .ics
def create_ics(events, filename='moveToiCalendar.ics'):
    with open(filename, 'w') as f:
        f.write("BEGIN:VCALENDAR\n")
        f.write("VERSION:2.0\n")
        f.write("PRODID:-//Your Company//NONSGML v1.0//EN\n")

        for event in events:
            # แปลงเวลาและวันที่
            start_time = datetime.strptime(event['date'] + " " + event['time'], '%Y-%m-%d %H:%M')
            start = start_time.strftime('%Y%m%dT%H%M%S')
            end = (start_time + timedelta(hours=1)).strftime('%Y%m%dT%H%M%S')  # สมมติว่าเหตุการณ์ยาว 1 ชั่วโมง

            f.write("BEGIN:VEVENT\n")
            f.write(f"UID:{start}@yourdomain.com\n")
            f.write(f"SUMMARY:{event['title']}\n")
            f.write(f"DTSTART:{start}Z\n")
            f.write(f"DTEND:{end}Z\n")
            f.write("LOCATION:Online\n")
            f.write("END:VEVENT\n")

        f.write("END:VCALENDAR\n")

# ตัวอย่างข้อมูลจาก WebScraping
events = [
    {'title': 'GDP Report', 'time': '10:00', 'date': '2025-01-30'},  # ตัวอย่างวันที่ล่วงหน้า
    {'title': 'Inflation Data', 'time': '12:00', 'date': '2025-01-31'}
]

# สร้างไฟล์ .ics
create_ics(events)
print("ไฟล์ .ics ถูกสร้างแล้ว!")
