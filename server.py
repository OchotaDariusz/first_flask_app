from flask import Flask, request, render_template

app = Flask(__name__)
notes = ['first note', 'second']

@app.route('/')
def index():
    return render_template('index.html', notes=notes)


@app.route('/note', methods=['GET', 'POST'])
def handle_notes():
    if request.method == 'POST':
        pass
    else:
        return render_template('note.html', notes=notes)


if __name__ == '__main__':
    app.run(debug=True)