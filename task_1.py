time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

for value in time_string.split(','):
    current = 0
    for part in value.replace(' ', ',').split(','):
        if 'h' in part:
            current += int(part.replace('h', '')) * 60
        elif 'm' in part:
            current += int(part.replace('m', ''))
        elif 's' in part:
            current += int(part.replace('s', '')) // 60
    total_minutes += current

print("Общее количество минут:" , (total_minutes))