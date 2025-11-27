from flask import Flask, render_template, abort, url_for

app = Flask(__name__)

pacientes = [
    {
        "id": 1,
        "nome": "Gabriel Moia",
        "idade": 16,
        "image": "https://tse2.mm.bing.net/th/id/OIP.1CX1M1rQrhqVbIrnBJeKNgHaED?rs=1&pid=ImgDetMain&o=7&rm=3"
    },
]

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/pacientes")
def listar_pacientes():
    return render_template('listar_pacientes.html', pacientes=pacientes)

@app.route("/paciente/<int:paciente_id>")
def detalhe_paciente(paciente_id):
    for paciente in pacientes:
        if paciente['id'] == paciente_id:
            return render_template('detalhe_paciente.html', paciente=paciente)
    return "Paciente não encontrado", 404


medicos =[
    {
        "id": 1,
        "nome": "Dr Rogerio",
        "idade": 36,
        "image": "https://medicinasa.com.br/wp-content/uploads/2023/03/medico-hospital-esteto-2-850x560.jpg"
    },
]

@app.route("/")
def inicio():
    return render_template('index.html')

@app.route("/medicos")
def listar_medicos():
    return render_template('listar_medicos.html', medicos=medicos)

@app.route("/medico/<int:medico_id>")
def detalhe_medico(medico_id):
    for medico in medicos:
        if medico['id'] == medico_id:
            return render_template('detalhe_medico.html', medico=medico)
    return "Medico nao disponivel no momento", 404


if __name__ == '__main__':
    app.run(debug=True)