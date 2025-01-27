import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# URL data source
url = "https://sslecal2.investing.com"

# sent request and response HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# get events
events = []
for event in soup.select('.event_row'):
    country = event.select_one('.event_country').text.strip()
    importance = len(event.select('.event_importance .icon-star-full'))  
    title = event.select_one('.event_name').text.strip()
    time_utc = event.select_one('.event_time').text.strip()

    # Sort by only Country : United States, importance = 3 
    if country == "United States" and importance == 3:
        # set timezone
        event_time = datetime.strptime(time_utc, '%H:%M') + timedelta(hours=7)
        formatted_time = event_time.strftime('%H:%M')
        formatted_date = datetime.now().strftime('%Y-%m-%d')  

        # collect the event data
        events.append({'title': title, 'time': formatted_time, 'date': formatted_date})

print(events)
