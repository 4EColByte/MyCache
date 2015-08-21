# coding: utf-8
YEAR = input("输入年份:")

#判断是否为闰年
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:    
        return True    
#print "闰年"
    else:
       #print "非闰年"
        return False

#判断月大小
def is_bigmonth(month):
    if month not in range(1,13):
        return 'Invaiad value'
    if month <=7:
        if (month % 2) == 1:
            return 31
        else:
            return 30
    else:
        if (month % 2) == 0:
            return 31
        else:
            return 30
def days(*args):
    (year,month,day)=args
    print year,month,day
    days=0
    if month == 1 :
        return day
    for mon in range(0,month):
        if is_bigmonth(mon):
            days +=mon*31
        else:
            days+=mon*30
    if is_leap(year):
        
        days -=1                   
    return days
