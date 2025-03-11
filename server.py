from flask import Flask, render_template, request
from Quiz import scrape_with_results

# Start the Server
app = Flask(__name__)

# Index (Home) Page
@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
    return render_template(
      "index.html"
    )

# Quiz Page
@app.route("/quiz")
@app.route("/quiz.html")
def quiz():
    return render_template(
      "quiz.html"
    )

# Results Page
@app.route("/results")
@app.route("/results.html")
def results():
    # Scrape for top jobs and return them to fill the results page
    topJobs = scrape_with_results(request.args)
    while len(topJobs) < 5:
      topJobs.insert(0, "None")
    
    return render_template(
      "results.html",
      job1=topJobs[4],
      job2=topJobs[3],
      job3=topJobs[2],
      job4=topJobs[1],
      job5=topJobs[0]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")