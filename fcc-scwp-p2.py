def add_time(start, duration, day=''):
    
    weekdays = {
        
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 0,
    
    }

    
    start_period = start[start.find(' ')+1:]
    start_minutes = int(start[start.find(':')+1:start.find(' ')])
    add_minutes = int(duration[duration.find(':')+1:]) 
    new_minutes = (start_minutes + add_minutes) % 60
    
    start_hours = int(start[:start.find(':')])
    
    if start_period == 'AM' and start_hours == 12:
        start_hours = 0
    
    add_hours = int(duration[:duration.find(':')])
    hours_elapsed = ((start_hours + add_hours))
    
    if start_minutes + add_minutes >= 60:
        hours_elapsed += 1 
        
    if start_period == 'PM':
        hours_elapsed += 12

    new_hours = hours_elapsed % 24

    if start_minutes + add_minutes >= 60:
        hours_elapsed += 1
    
    days_elapsed = hours_elapsed // 24
    
    if new_minutes == 60:
        new_minutes = '00'
    if len(str(new_minutes)) < 2:
        new_minutes = '0' + str(new_minutes)

    if new_hours >= 12:
        new_period = 'PM'
    else:
        new_period = 'AM'
    new_hours = new_hours % 12
    if new_hours == 0:
        new_hours = 12

    
    
    
    if days_elapsed == 1:
        days_later = ' (next day)'
        new_time = f'{new_hours}:{new_minutes} {new_period}{days_later}'
    elif days_elapsed == 0:
        days_later = ''
        new_time = f'{new_hours}:{new_minutes} {new_period}{days_later}'
    else: 
        days_later = f' ({days_elapsed} days later)'
        new_time = f'{new_hours}:{new_minutes} {new_period}{days_later}'

    if day:
        start_day = weekdays[day[0].upper() + day[1:].lower()]
        new_day = [key for key, value in weekdays.items() if value == ((days_elapsed + start_day) % 7)][0]
        new_time = f'{new_hours}:{new_minutes} {new_period}, {new_day}{days_later}'
    else: 
        new_time = f'{new_hours}:{new_minutes} {new_period}{days_later}'

    



    
    return new_time



