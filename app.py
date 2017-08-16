from flask import Flask
from flask import render_template, request
app = Flask(__name__)

# set all route here
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer_type', methods=['POST'])
def answer_type():
    # get query text
    query = request.form['query']
    # add your code here

    # replace results with real results from your model
    results = [("ENTITY", 0.37, 37), ("NUMBER", 0.13, 13),
               ("BOOLEAN", 0.25, 25), ("STRING", 0.04, 4), ("DATE", 0.01, 1)]
    return render_template('answertype.html', results=results, query=query)


if __name__ == '__main__':
    app.run(debug=True)
