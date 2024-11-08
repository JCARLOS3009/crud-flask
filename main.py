from flask import Flask, render_template, url_for
from crud import app_crud

app = Flask(__name__)
app.register_blueprint(app_crud)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/main')
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port=81)
