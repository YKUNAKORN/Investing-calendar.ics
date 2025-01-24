from datetime import datetime, timedelta
import pytz

# ฟังก์ชันสร้างไฟล์ .ics
def create_ics(events, filename='moveToiCalendar.ics'):
    with open(filename, 'w') as f:
        f.write("BEGIN:VCALENDAR\n")
        f.write("VERSION:2.0\n")
        f.write("PRODID:-//Your Company//NONSGML v1.0//EN\n")

        for event in events:
            # แปลงเวลาเป็น UTC
            local = pytz.timezone("Asia/Bangkok")  # เปลี่ยนเป็น Time Zone ที่ใช้งาน
            start_time = local.localize(datetime.strptime(event['date'] + " " + event['time'], '%Y-%m-%d %H:%M'))
            start = start_time.astimezone(pytz.utc).strftime('%Y%m%dT%H%M%SZ')
            end = (start_time + timedelta(hours=1)).astimezone(pytz.utc).strftime('%Y%m%dT%H%M%SZ')  # เหตุการณ์ยาว 1 ชั่วโมง

            # เขียนข้อมูลเหตุการณ์ในไฟล์ .ics
            f.write("BEGIN:VEVENT\n")
            f.write(f"UID:{start}@yourdomain.com\n")
            f.write(f"SUMMARY:{event['title']}\n")
            f.write(f"DTSTART:{start}\n")
            f.write(f"DTEND:{end}\n")
            f.write("LOCATION:Online\n")
            f.write("END:VEVENT\n")

        f.write("END:VCALENDAR\n")

# ตัวอย่างข้อมูลเหตุการณ์
events = [
    {'title': 'GDP Report', 'time': '10:00', 'date': '2025-01-24'},
    {'title': 'Inflation Data', 'time': '12:00', 'date': '2025-01-24'}
]

# สร้างไฟล์ .ics
create_ics(events)
print("ไฟล์ .ics ถูกสร้างแล้ว!")