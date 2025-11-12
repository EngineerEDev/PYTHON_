##date##
from datetime import datetime

now = datetime.now()

year_2025= datetime(2025, 1, 1)

def print_date(date):
    print("Año actual:", date.year)
    print("Mes actual:", date.month)
    print("Día actual:", date.day)
    print("Hora actual:", date.hour)
    print("Minuto actual:", date.minute)
    print("Segundo actual:", date.second)

##print_date(now)


year_2025= datetime(2025, 1, 1)


##print(year_2025)


##print_date(year_2025)

from datetime import time 
current_time = time(21,2,30)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


from datetime import date

current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

#print(current_date.year +5, current_date.month+1, current_date.day+1)

#print(type(now))
#print(type(current_time))
#diff = current_date - year_2025.date() 
#print(diff)

from datetime import timedelta


start_timedelta = timedelta(200,100,100,weeks=10)
end_timedelta = timedelta(300,100,100,weeks=13)
print(start_timedelta-end_timedelta)
print(end_timedelta+end_timedelta)