from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("model/phishing_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        email_text = request.form["email"]

        email_vector = vectorizer.transform([email_text])
        result = model.predict(email_vector)[0]

        prediction = "Phishing" if result == 1 else "Safe"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)