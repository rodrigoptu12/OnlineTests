from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/location', methods=['POST'])
def get_location():
    if request.method == 'POST':
        if 'geolocation' in request.form:
            lat = request.form['lat']
            lon = request.form['lon']
            return f'Sua localização é: {lat}, {lon}'
        else:
            return 'Acesso à localização negado.'
