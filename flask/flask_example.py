from flask import Flask

app = Flask(__name__)
#Go to http://127.0.0.1:5000 to view home page
@app.route("/")
def home():
    return "Home page"
#Go to http://127.0.0.1:5000/about to view about page
@app.route("/about")
def about():
    return "About page"

if __name__ == "__main__":
    app.run(debug=True)