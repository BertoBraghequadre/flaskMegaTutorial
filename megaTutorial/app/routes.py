# Quì vengono gestiti tutti gli end-point, ovvero le loro root

from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello world"
