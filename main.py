from flask import Flask, jsonify

app = Flask(__name__)

events = [
    {'name': 'Richie', 'date': '2020-10-16', 'time': '16:00', 'email': 'richieglennon@gmail.com',
     'distance': 5, 'pace': '7', 'location': 'haddonfield'},
    {'name': 'Shane', 'date': '2020-10-18', 'time': '19:00', 'email': 'shane@gmail.com',
     'distance': 15, 'pace': '6', 'location': 'Easton'}
]



@app.route('/')
def home():
    return 'Hello World'


@app.route('/getAllEvents', methods=['GET'])
def get_all_events():
    return jsonify(events)


@app.route('/postEvent/<name>/<date>/<time>/<email>/<distance>/<pace>/<location>', methods=['POST'])
def post_event(name, date, time, email, distance, pace, location):
    new_event = {'name': name,
                 'date': date,
                 'time': time,
                 'email': email,
                 'distance': distance,
                 'pace': pace,
                 'location': location
                 }
    events.append(new_event)
    return jsonify(new_event)


if __name__ == '__main__':
    app.run(port=5000)
