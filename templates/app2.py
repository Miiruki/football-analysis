from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form['date']
        league_id = request.form['league']
        api_key = '0e155f34c82d16819a3538a0bdf9b39cdb1f0ec35df0ce5f29d9663943518d7b'  # Remplacez par votre clé API

        url = f"https://apiv3.apifootball.com/?action=get_events&from={date}&to={date}&league_id={league_id}&APIkey={api_key}"
        response = requests.get(url)
        matches = response.json()

        return render_template('index.html', matches=matches)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)