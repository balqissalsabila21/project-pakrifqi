from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operator = request.form["operator"]

            if operator == "add":
                result = num1 + num2
            elif operator == "subtract":
                result = num1 - num2
            elif operator == "multiply":
                result = num1 * num2
            elif operator == "divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error! Division by Zero."
        except ValueError:
            result = "Invalid Input"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
