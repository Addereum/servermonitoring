import views
from flask import Flask
import psutil

app = Flask(__name__, template_folder='views')

app.add_url_rule('/', view_func=views.index)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)