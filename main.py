import json
from datetime import datetime

class Event:
    def __init__(self, date, name):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.name = name

# Чтение файла JSON
with open('operations.json', 'r') as f:
    events_data = json.load(f)

# Преобразование данных из JSON в объекты Event
events = [Event(event_data['date'], event_data['name']) for event_data in events_data]

# Сортировка событий по дате
sorted_events = sorted(events, key=lambda x: x.date)

# Выбор последних пяти событий
last_five_events = sorted_events[-5:]

# Вывод последних пяти событий
for event in last_five_events:
    print(f"Событие: {event.name}, Дата: {event.date.strftime('%Y-%m-%d')}")

