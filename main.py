from flask import Flask, render_template, request
from summarizer import summarize_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def summarize():
    if request.method == 'POST':
        text = request.form['text']
        max_length = int(request.form['max'])
        min_length = int(request.form['min'])
        summary = summarize_text(text, max_length, min_length)
        return render_template('index.html', summary=summary)

    return render_template('index.html', summary=None)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
