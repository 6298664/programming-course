def indentify_day_type(day_num):
    if day_num < 1 or day_num > 7:
        return "Not a proper day number!"
    elif 1 <= day_num <= 5:
        return "It's a weekday!"
    else:
        return "It's a weekend" 
    
day_num = int(input("Enter day number"))

print(indentify_day_type(day_num))



def identify_day_name(day_num):
    if day_num == 1:
        return "It is a Monday"
    if day_num == 2:
        return "It is a Tuesday"
    if day_num == 3: 
        return "It is a Wednesday"
    if day_num == 4:
        return "It is a Thursday"
    if day_num == 5:
        return "It is a Friday"
    if day_num == 6: 
        return "It is a Saturday"
    if day_num == 7:
        return "It is a Sunday"
    else:
        return "Not a proper day number!"
    
day_num = int(input("Enter day number"))

print(identify_day_name(day_num))
