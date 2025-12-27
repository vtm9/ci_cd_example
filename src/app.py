from flask import Flask, request

app = Flask(__name__)


@app.route("/multiply", methods=["GET"])
def multiply():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
    except (TypeError, ValueError):
        return "a и b - НЕ числа"
    return str(a * b)


@app.route("/divide", methods=["GET"])
def divide():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
    except (TypeError, ValueError):
        return "a и b - НЕ числа"
    if b == 0:
        return "Деление на ноль невозможно"
    return str(a / b)


def main():
    app.run(host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
