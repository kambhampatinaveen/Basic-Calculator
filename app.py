from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None

    if request.method == "POST":
        try:
            a = float(request.form["num1"])
            b = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "+":
                result = a + b
            elif operation == "-":
                result = a - b
            elif operation == "*":
                result = a * b
            elif operation == "/":
                if b != 0:
                    result = a / b
                else:
                    error = "Division by zero is not allowed"
        except:
            error = "Invalid input"

    return render_template("calculator.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
