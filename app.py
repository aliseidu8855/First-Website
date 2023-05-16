from flask import Flask, render_template


app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title":"Data Analyst",
        "location":"Tinga",
        "Salary": "150,00ghs"
    },

    {
        "id": 2,
        "title":"Front-End Development",
        "location":"Accra",
        "Salary": "100,00ghs"
    },

    {
        "id": 3,
        "title":"Back-End Development",
        "location":"Wa",
        "Salary": "100,00ghs"
    },

    {
        "id": 4,
        "title":"Full Stack Development",
        "location":"San Francisco, USA",
        "Salary": "120,000"
    }
]

@app.route("/")
def hello_vanco():
    return render_template("home.html",jobs=JOBS,)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)