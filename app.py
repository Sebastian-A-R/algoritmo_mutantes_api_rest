from flask import Flask,request
from werkzeug.exceptions import abort

app = Flask(__name__)

from detector_de_mutantes import isMutant


@app.route('/mutant/',methods=['POST'])
def mutant():
    dna = request.json['dna']
    if isMutant(dna):
        return f'El resultado es {isMutant(dna)}'
    else:
        abort(403)


if __name__ == '__main__':
    app.run(debug=True, port=4000)