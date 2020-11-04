from flask import Flask
 
app = Flask(__name__)

from app.main.index import main as main

app.register_blueprint(main)

from app import app
 
app.run(host="0.0.0.0", port=80)


