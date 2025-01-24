import requests
from bs4 import BeautifulSoup

# URL ของหน้าเว็บที่มีข้อมูล
url = "https://sslecal2.investing.com"
#url = https://www.investing.com/economic-calendar/

# ส่ง request และดึง HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# ดึงข้อมูลเหตุการณ์ (ปรับ selector ให้ตรงกับโครงสร้าง HTML ของเว็บ)
events = []
for event in soup.select('.event_row'):
    title = event.select_one('.event_name').text.strip()
    time = event.select_one('.event_time').text.strip()
    date = "2025-01-24"  # กำหนดวันที่ (เปลี่ยนเป็นดึงจากเว็บถ้าได้)
    events.append({'title': title, 'time': time, 'date': date})

print(events)