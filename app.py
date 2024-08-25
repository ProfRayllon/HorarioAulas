from flask import Flask, render_template, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Exemplo de estrutura do horário
horario = {
    "Segunda-feira": [("07:20", "08:20", "Português", "Sala A"),
                     ("08:20", "09:20", "Matemática", "Sala B")],
    "Terça-feira": [("07:20", "08:20", "Inglês", "Sala A"),
                    ("08:20", "09:20", "Física", "Sala B")],
    # Continue para os outros dias...
}

def obter_horarios_do_dia():
    agora = datetime.now()
    dia_semana = agora.strftime("%A").capitalize() + "-feira"
    
    if dia_semana not in horario:
        return []
    
    return horario[dia_semana]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/horarios_do_dia')
def horarios_do_dia():
    return jsonify(obter_horarios_do_dia())

if __name__ == '__main__':
    app.run(debug=True)
