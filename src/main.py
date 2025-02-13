import cherrypy 
import os.path
import mako.template
import mako.lookup
import random
import quotes
import names
import datesnnums
import PIL.Image
import io


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

recent_image = None
text_name = None

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
        return t.render(name=q, postname=text_name)
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
    
    def checkImage(self, data, name):
        global recent_image 
        global text_name
        try:
            MAXSIZE=4096
            tmp = data.file.read()
            image = io.BytesIO(tmp)
            temp = name
            with PIL.Image.open(image, formats=["JPEG","PNG"]) as img:
                if img.width > MAXSIZE or img.height > MAXSIZE:
                    return False
            recent_image = tmp
            text_name = temp
            return True
        except PIL.UnidentifiedImageError:
            return False
        
    @cherrypy.expose
    def mostrecent(self):
        global recent_image
        if recent_image == None:
            with open(f"{srcdir}/../html/thumbnail.jpg","rb") as fp:
                recent_image = fp.read()
        cherrypy.response.headers["Content-Type"] = "image/jpeg"
        return recent_image
    

    
        
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
