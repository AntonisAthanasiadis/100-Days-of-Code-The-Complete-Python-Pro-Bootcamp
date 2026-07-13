from flask import Flask

app = Flask(__name__)

# Use something like this: http://127.0.0.1:5000/hello/Antonis
@app.route("/hello/<name>")
def greet(name):
    return f"<h1>Hello, {name}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)