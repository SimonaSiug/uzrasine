from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')
uzrasai = []
vartotojai = ["Vartotojas1", "Vartotojas2", "Vartotojas3"]

@app.route("/uzrasai", methods=['GET', 'POST'])
def uzrasai_route():
    global uzrasai
    if request.method == 'POST':
        notes = request.form.get('uzrasai')
        uzrasai.append(notes)
        return render_template('uzrasai.html', uzrasai=uzrasai)
    else:
        return render_template('uzrasai.html', uzrasai=uzrasai)

@app.route("/vartotojai", methods=['GET', 'POST'])
def vartotojai_route():
    if request.method == 'POST':
        user = request.form.get('vartotojai')
        vartotojai.append(user)
        return render_template('vartotojai.html', vartotojai=vartotojai)
    else:
        return render_template('vartotojai.html', vartotojai=vartotojai)


if __name__ == '__main__':
    app.run(debug=True)
