from flask import Flask, jsonify

app = Flask(__name__)

events = [
    {"date":"2020-10-16","distance":5,"email":"sampleemail1@gmail.com","location":"sampletown1","name":"testperson","pace":"7","time":"16:00"},
    {"date":"2020-10-18","distance":15,"email":"sampleemail2@gmail.com","location":"sampletown2","name":"testperson2","pace":"6","time":"19:00"}
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


@app.route('/clearAll', methods=['POST'])
def clear_events():
    events.clear()
    return jsonify({'message': 'Cleared The Database'})


if __name__ == '__main__':
    app.run(port=5000)
