from flask import Flask, request, render_template

app = Flask(__name__)

notes = []

@app.route('/')
def index():
    return render_template('index.html', notes=notes)


@app.route('/note', methods=['GET', 'POST'])
def handle_notes():
    if request.method == 'POST':
        note = request.form['content']
        if not note:
            return render_template('note.html', notes=notes, counter=len(notes), bad_note=True)
        else:
            notes.append(note)
    return render_template('note.html', notes=notes, counter=len(notes))


if __name__ == '__main__':
    app.run(debug=True)