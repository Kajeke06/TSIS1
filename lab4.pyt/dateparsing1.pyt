from datetime import date, timedelta
today = date.today()
five_days_ago = today - timedelta(days=5)
print(five_days_ago)