from flask import Flask

# appena viene eseguito un modulo "__name__" prende il nome del modulo stesso
app = Flask(__name__)

from app import routes