from flask import Flask, render_template, request
import joblib
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index1.html")
model=joblib.load("student_pass-fail.pkl")
@app.route("/predict", methods=["POST"])
def predict():
    math = float(request.form["math"])
    science = float(request.form["science"])
    english = float(request.form["english"])

    average = (math + science + english) / 3

    if average >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    return render_template(
        "index1.html",
        prediction=result,
        avg=round(average, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)
