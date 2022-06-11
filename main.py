# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world(num1=8, num2=8):
    # Return 8 by 8 checkerboard
    return render_template('index.html', num1=int(num1), num2=int(num2))


# The "@" decorator associates this route with the function immediately following
@app.route('/4')
def four_times(num1=8, num2=4):
    # Return 8 by 4 checkerboard
    return render_template('index.html', num1=int(num1), num2=int(num2))


# The "@" decorator associates this route with the function immediately following
@app.route('/<num1>/<num2>')
def costmized(num1, num2):
    # Return x by y checkerboard.
    return render_template('index.html', num1=int(num1), num2=int(num2))


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run t
