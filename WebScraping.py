import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# URL ของหน้าเว็บที่มีข้อมูล
url = "https://sslecal2.investing.com"

# ส่ง request และดึง HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# ดึงข้อมูลเหตุการณ์
events = []
for event in soup.select('.event_row'):
    title = event.select_one('.event_name').text.strip()
    time = event.select_one('.event_time').text.strip()
    date = event.select_one('.event_date').text.strip()  # ดึงวันที่โดยตรง (สมมติว่าเว็บมีข้อมูลวันที่)

    # แปลงวันที่ที่ดึงมาให้อยู่ในรูปแบบ datetime
    event_date = datetime.strptime(date, '%Y-%m-%d')
    today = datetime.today()

    # ตรวจสอบว่า Event เกิดขึ้นในอีก 7 วันข้างหน้า
    if today <= event_date <= (today + timedelta(days=7)):
        events.append({'title': title, 'time': time, 'date': date})

print(events)
