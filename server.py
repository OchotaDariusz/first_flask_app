from flask import Flask, request, render_template

app = Flask(__name__)

notes = []

@app.route('/')
def index():
    return render_template('index.html', notes=notes)


@app.route('/note', methods=('GET', 'POST'))
def handle_notes():
    if request.method == 'POST':
        note = request.form['content']
        if not note:
            return render_template('note.html', notes=notes, counter=len(notes), bad_note=True)
        else:
            notes.append(note)
    return render_template('note.html', notes=notes, counter=len(notes))


@app.route('/note/edit', methods=('GET', 'POST'))
def edit_notes():
    indexes = range(len(notes))
    if request.method == 'POST':
        index = request.form['indexes']
        note = request.form['content']
        if not note:
            return render_template('edit.html', notes=notes, indexes=indexes, bad_note=True)
        notes[int(index)] = note
    return render_template('edit.html', notes=notes, indexes=indexes)


@app.route('/note/delete', methods=('GET', 'POST'))
def delete_notes():
    if request.method == 'POST':
        index = request.form['indexes']
        notes.pop(int(index))
    indexes = range(len(notes))
    return render_template('delete.html', notes=notes, indexes=indexes)


if __name__ == '__main__':
    app.run(debug=True)