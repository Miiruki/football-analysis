from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def fetch_match_details_from_api(match_id):
    api_key = '0e155f34c82d16819a3538a0bdf9b39cdb1f0ec35df0ce5f29d9663943518d7b'  
    url = f"https://apiv3.apifootball.com/?action=get_events&match_id={match_id}&APIkey={api_key}"
    response = requests.get(url)
    match_details = response.json()
    return match_details

def get_league_standings(league_id, api_key):
    url = f"https://apiv3.apifootball.com/?action=get_standings&league_id={league_id}&APIkey={api_key}"
    response = requests.get(url)
    standings = response.json()
    return standings

@app.route('/', methods=['GET', 'POST'])
def index():
    standings = {}  

    if request.method == 'POST':
        date = request.form['date']
        league_id = request.form['league']
        api_key = '0e155f34c82d16819a3538a0bdf9b39cdb1f0ec35df0ce5f29d9663943518d7b'  

        url = f"https://apiv3.apifootball.com/?action=get_events&from={date}&to={date}&league_id={league_id}&APIkey={api_key}"
        response = requests.get(url)
        matches = response.json()

        
        standings[league_id] = get_league_standings(league_id, api_key)

        return render_template('index.html', matches=matches, standings=standings)

    return render_template('index.html', standings=standings)

@app.route('/match_details/<match_id>')
def match_details(match_id):
    match_details = fetch_match_details_from_api(match_id)  
    return render_template('match_details.html', match_details=match_details)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')