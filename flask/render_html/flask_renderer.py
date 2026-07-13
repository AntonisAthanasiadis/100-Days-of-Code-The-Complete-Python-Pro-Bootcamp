from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        name="Antonios",
        role="Software Engineer",
        language="Python"
    )

if __name__ == "__main__":
    app.run(debug=True)