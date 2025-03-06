import datetime as dt

detail = dt.datetime.now()
print(detail)
detail = dt.date.today()
print(detail)
# detail= dt.time.
print(dir(dt.time))
print(dt.time(hour=2 , minute=3 ,second=8))