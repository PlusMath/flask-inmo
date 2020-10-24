from flask import Flask
import time
import threading 
app = Flask(__name__)
from app.main.index import main as main
def inmo():
    
    
    app.register_blueprint(main)

    threading.Timer(60, inmo).start()

inmo()
