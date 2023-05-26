#.venv\Scripts\Activate.ps1
#ran $env:FLASK_APP="server.py" and then flask run
#turn on debug mode =>app.run(debug=True)

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('test.html')
    '''
    return '<h1 style="text-align:center"> Hello, Ella! </h1> \
            <h2>Hello World </h2>\
            <p><iframe src="https://giphy.com/embed/9dC7BpMHisDagbjgYq" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/corgi-lazy-hk-9dC7BpMHisDagbjgYq">via GIPHY</a></p>'
    '''


if __name__ == "__main__":
    app.run(debug=True)