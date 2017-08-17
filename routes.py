#
from flask import Flask
# create a Flask application instance
app = Flask(__name__)
# define a route through the app.route decorator
@app.route("/")
def index():
        return "<h1>Hello World!</h1>"
# launch the integrated development web server
# and run the app on http://localhost:8085
        if __name__=="__main__":
               app.run(debug=True,port=8085)
