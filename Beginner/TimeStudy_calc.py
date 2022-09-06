from datetime import datetime

begin = datetime(2022,4,7) # Начало обучения
today = datetime.now()
result = today - begin

print(result.days)