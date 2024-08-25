from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Exemplo de dados
schedule = [
    {"time": "08:00 - 09:00", "subject": "Matemática", "room": "Sala 101"},
    {"time": "09:00 - 10:00", "subject": "História", "room": "Sala 102"},
    {"time": "10:00 - 11:00", "subject": "Física", "room": "Sala 103"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_schedule')
def get_schedule():
    return jsonify(schedule)

if __name__ == '__main__':
    app.run(debug=True)
