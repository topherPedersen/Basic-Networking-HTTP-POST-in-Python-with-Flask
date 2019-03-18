from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/receive-form-data', methods=['GET', 'POST'])
def receive_form_data():
    foo = request.form.get("foo")
    bar = request.form.get("bar")
    baz = request.form.get("baz")
    return render_template('receive-form-data.html', foo=foo, bar=bar, baz=baz)
