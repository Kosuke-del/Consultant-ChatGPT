"""This program is to summarize sentences"""

from flask import Flask, render_template, request
import openai

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    """
    Renders the index page or processes user input to summarize text.

    Returns:
        If the request method is 'POST', 
        returns the result of the text summary in the result.html template.
        Otherwise, returns the index.html template.
    """
    if request.method == 'POST':
        text = request.form['text']
        max_length = request.form['max_length']

        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize these sentences in {max_length} words.「{text}」"},
            ]
        )
        res_content = res["choices"][0]["message"]["content"]

        return render_template('result.html', result=res_content)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
