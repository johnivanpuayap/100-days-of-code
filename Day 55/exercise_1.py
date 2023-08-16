from flask import Flask

app = Flask(__name__)


# Create decorators to style HTML tags
def make_bold(function):

    def wrapper_function():
        text = function()
        text = f"<strong>{text}</strong>"
        return text
    return wrapper_function


def make_emphasis(function):

    def wrapper_function():
        text = function()
        text = f"<em>{text}</em>"
        return text
    return wrapper_function


def make_underlined(function):

    def wrapper_function():
        text = function()
        text = f"<u>{text}</u>"
        return text
    return wrapper_function


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


# Run the server without using the terminal
if __name__ == "__main__":
    app.run(debug=True)
