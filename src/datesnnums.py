import datetime
import random

dates = []
viewcounts = []
images = ["/html/sample1.jpg", "/html/sample2.jpg", "/html/sample3.jpg","/html/sample4.jpg", "/html/sample5.jpg", "/html/sample6.jpg",
          "/html/sample7.jpg", "/html/sample8.jpg","/html/sample9.jpg", "/html/sample10.jpg"]

for i in range(10):
    v = random.randrange(10000)
    x = datetime.timedelta(minutes=random.randrange(8000))
    hoursago = int( x.seconds / 3600 )
    minutesago = round((x.seconds - hoursago*3600)/60)
    dates.append(f"{x.days} days, {hoursago} hours, and {minutesago} minutes ago")
    viewcounts.append(v)