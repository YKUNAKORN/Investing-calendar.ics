import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from ics import Calendar, Event
import pytz

URL = "https://www.investing.com/economic-calendar/"
HEADERS = { "User-Agent": "Mozilla/5.0" }
res = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(res.text, "html.parser")
table = soup.select_one("#economicCalendarData")
tz = pytz.timezone("Asia/Bangkok")
events = []

for row in table.select("tr"):
    try:
        time = row.select_one(".time")
        cur = row.select_one(".currency")
        imp = row.select_one(".sentiment")
        event = row.select_one(".event")

        if not (time and cur and imp and event):
            continue
        if cur.get_text(strip = True) != "USD":
            continue
        stars = len(imp.select("i.grayFullBullishIcon"))
        if stars < 3:
            continue
        eventName = event.get_text(strip = True)
        timeStr = time.get_text(strip = True)
        if not timeStr:
            continue

        eventT = datetime.strptime(timeStr, "%H:%M")
        now = datetime.now(tz)
        eventTime = tz.localize(datetime.combine(now.date(), eventT.time()))
        events.append((eventTime, eventName))

    except Exception as e:
        continue

calen = Calendar()

for evTime, evName in events:
    e = Event()
    e.name = evName
    e.begin = evTime
    e.end = evTime + timedelta(hours = 1)  
    e.description = "USD High Impact Event"
    calen.events.add(e)

with open("economic_calendar.ics", "w", encoding="utf-8") as f:
    f.writelines(calen)

print("economic_calendar.ics generated successfully")