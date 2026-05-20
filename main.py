from flask import *

from admin import admin
from public import public



app=Flask(__name__)
app.register_blueprint(admin)
app.register_blueprint(public)


app.run(debug=True,port=5092,host="0.0.0.0")
