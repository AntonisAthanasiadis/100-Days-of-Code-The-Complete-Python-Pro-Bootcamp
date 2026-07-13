from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        name="Antonios",
        logged_in=True,
        skills=["Python", "Flask", "Selenium"]
    )

if __name__ == "__main__":
    app.run(debug=True)