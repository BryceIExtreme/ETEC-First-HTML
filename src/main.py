import cherrypy 
import os.path
import mako.template
import mako.lookup
import random
import quotes
import names
import datesnnums


PYPATH = os.path.dirname(__file__)
lookup = mako.lookup.TemplateLookup(
    directories=[os.path.dirname(__file__),
    f"{os.path.dirname(__file__)}/../html"]
)
BASEDIR=os.path.abspath( os.path.dirname(__file__) )

#we have modules for each page we're displaying 
import page_index
import page_signup
import page_posts
import page_test

class App:
    @cherrypy.expose
    def quote(self):
        q = random.choice(quotes.quotations)
        t = lookup.get_template("quotes.html")
        return t.render(quote=q)
    @cherrypy.expose
    def index(self):
        q = random.choice(names.usernames)
        t = lookup.get_template("index.html")
        return t.render(name=q)
    @cherrypy.expose
    def signup(self):
        t = lookup.get_template("signup.html")
        return t.render()
    @cherrypy.expose
    def posts(self):
        q = datesnnums.dates
        v = datesnnums.viewcounts
        i = datesnnums.images
        print (i)
        t = lookup.get_template("posts.html")
        return t.render(images = i, postdate = q, views = v)
    @cherrypy.expose
    def test(self):
        return page_test.get()
    @cherrypy.expose
    def updateprofile(self):
        with open(f"{BASEDIR}/../src/updateprofile.html") as fp:
            return fp.read()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def do_update(self, name, birthday, pic ):
        print("name is:",name)
        print("birthday is:",birthday)
        print("pic is:",pic)
        tmp = pic.file.read()
        #just print first 10 bytes
        print("pic is:",tmp[:10])
        return {"ok": True }
        
#the location where the main.py file is stored: The src folder
srcdir = os.path.abspath(os.path.dirname(__file__))

app = App()
cherrypy.quickstart(
    app,
    '/',
    {
        "/html": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": f"{srcdir}/../html"
        }
    }
)
