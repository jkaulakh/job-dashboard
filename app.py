from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    jobs = []
    error = None

    if request.method == "POST":

        keyword = request.form.get("keyword")

        try:

            url = f"https://remotive.com/api/remote-jobs?search={keyword}"

            response = requests.get(url)

            data = response.json()

            jobs = data.get("jobs", [])[:12]

        except Exception as e:

            error = str(e)

    return render_template(
        "index.html",
        jobs=jobs,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)