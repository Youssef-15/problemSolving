#Problem solving

#Leap year
#Year that can be divided 4 is leap year
#if divided by 4 and divided by 100 is not a leap year
#if divided by 100 and 400 so it will be a leap year
#1900<=year<=10^5
#return True or False

def leap_year():
    year = int(input())
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(leap_year())