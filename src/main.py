import cherrypy
import os.path
import mako.template

BASEDIR=os.path.abspath( os.path.dirname(__file__) )

mostrecentimage = None
mostrecenttitle=""

class App:
    @cherrypy.expose
    def index(self):
        t = mako.template.Template(
            filename=f"{BASEDIR}/index.html"
        )
        return t.render(title=mostrecenttitle)

    @cherrypy.expose
    def makepost(self):
        with open(f"{BASEDIR}/../html/makepost.html") as fp:
            return fp.read()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def dopost(self,title,pic):
        tmp = pic.file.read()
        if tmp[:4] != b"\xff\xd8\xff\xe0":
            print("BAD HEADER ON JPEG:",tmp[:4])
            return {"ok":False, "reason": "Not a JPEG"}
        global mostrecentimage, mostrecenttitle
        mostrecentimage = tmp
        mostrecenttitle = title
        return {"ok":True}

    @cherrypy.expose
    def mostrecent(self):
        if not mostrecentimage:
            with open(f"{BASEDIR}/../html/question.jpg","rb") as fp:
                data = fp.read()
        else:
            data = mostrecentimage
        cherrypy.response.headers["Content-Type"] = "image/jpeg"
        return data


app = App()
cherrypy.quickstart(
    app,
    '/',
    {
        "/html": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": f"{BASEDIR}/../html"
        }
    }
)
