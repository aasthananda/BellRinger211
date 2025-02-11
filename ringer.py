from datetime import datetime
current_time=datetime.now()
target_time=datetime(current_time.year, 2, 14, 0, 0, 0)
if current_time>target_time:
    target_time=datetime(current_time.year +1, 2, 14, 0,0,0)
time_change = target_time- current_time
hours = int(time_change.total_seconds()//3600)
print(hours)
