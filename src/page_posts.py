import os.path
import mako.template 
import random
import datetime

def get():



    x = datetime.timedelta(minutes=random.randrange(8000))
    hoursago = int( x.seconds / 3600 )
    minutesago = round(x.seconds - x.days*3600)
    d = os.path.dirname( __file__ )
    t = mako.template.Template(
            filename=f"{d}/posts.html")
    return t.render(postdate = print( f"{x.days} days, {hoursago} hours, and {minutesago} minutes ago" ) )