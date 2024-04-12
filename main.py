from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)
uzrasai = []

@app.route('/uzrasai', methods=['GET', 'POST'])
def handle_uzrasai():
    if request.method == 'POST':
        tekstinis_uzrasas = request.form['tekstas']
        uzrasai.append(tekstinis_uzrasas)
    return render_template('uzrasai.html', uzrasai=uzrasai)

@app.route('/vartotojai', methods=['GET'])
def handle_vartotojai():
    vartotojai = ['Jonas', 'Petras', 'Ona']
    return render_template('vartotojai.html', vartotojai=vartotojai)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
