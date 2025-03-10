from flask import Flask, render_template, request
from Quiz import scrape_with_results

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
    return render_template(
        "index.html"
    )

@app.route("/quiz")
@app.route("/quiz.html")
def quiz():
    return render_template(
        "quiz.html"
    )

@app.route("/results")
@app.route("/results.html")
def results():
    results = scrape_with_results(request.args)
    return render_template(
        "results.html",
        results=results
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")