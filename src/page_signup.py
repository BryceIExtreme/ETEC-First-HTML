import os.path
import mako.template 
import random

def get():
    d = os.path.dirname( __file__ )
    t = mako.template.Template(
            filename=f"{d}/signup.html")