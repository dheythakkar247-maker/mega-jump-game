from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # This renders the game page
    return render_template('first.html')

if __name__ == '__main__':
    # Use debug=True while developing to see errors in real-time
    app.run(debug=True)