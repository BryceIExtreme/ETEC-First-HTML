import cherrypy 
import os.path
import mako.template
import mako.lookup
import random
import quotes
import names

PYPATH = os.path.dirname(__file__)
lookup = mako.lookup.TemplateLookup(
    directories=[os.path.dirname(__file__),
    f"{os.path.dirname(__file__)}/../html"]
)

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
        return page_signup.get()
    @cherrypy.expose
    def posts(self):
        return page_posts.get()
    @cherrypy.expose
    def test(self):
        return page_test.get()
        
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
