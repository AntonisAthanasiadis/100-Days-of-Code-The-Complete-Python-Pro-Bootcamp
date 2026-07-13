from flask import Flask

app = Flask(__name__)

#change to true to enter!
logged_in = False


def login_required(func):
    def wrapper():
        if not logged_in:
            return "<h1>Access Denied</h1>"

        return func()

    return wrapper


@app.route("/")
def home():
    return "<h1>Public Page</h1>"


@app.route("/secret")
@login_required
def secret():
    return "<h1>Top Secret Stuff</h1>"


if __name__ == "__main__":
    app.run(debug=True)