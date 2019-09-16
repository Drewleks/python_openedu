hours = int(input())
minutes = int(input())
total_in_minutes = hours * 60 + minutes
hours = total_in_minutes // 60 % 24
minutes = total_in_minutes % 60
print(hours, minutes)
