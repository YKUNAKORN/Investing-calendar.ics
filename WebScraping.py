import datetime

import requests
from bs4 import BeautifulSoup

# URL ของหน้าเว็บที่มีข้อมูล
url = "https://www.investing.com/economic-calendar/"

# ส่ง request และดึง HTML
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# ดึงข้อมูลเหตุการณ์
events = []
for event in soup.select('.js-event-item'):
    try:
        title = event.select_one('.event').text.strip()  # ชื่อเหตุการณ์
        time = event.select_one('.time').text.strip()  # เวลา
        date = datetime.now().strftime('%Y-%m-%d')  # กำหนดวันที่ปัจจุบัน
        events.append({'title': title, 'time': time, 'date': date})
    except AttributeError:
        continue  # หากข้อมูลบางอย่างขาดไป ให้ข้ามไป

# แสดงผลข้อมูลที่ดึงได้
print(events)

# บันทึกข้อมูลลงไฟล์ .ics (หากต้องการ)
if events:
    from moveToiCalendar import create_ics  # เรียกใช้ฟังก์ชันจากไฟล์ moveToiCalendar.py
    create_ics(events)
    print("ข้อมูลที่ดึงมาได้ถูกบันทึกลงไฟล์ .ics แล้ว!")
else:
    print("ไม่มีข้อมูลเหตุการณ์ที่ดึงมาได้.")
