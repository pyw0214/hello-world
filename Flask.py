from flask import Flask, render_template, request, redirect
from flask.templating import render_template
from so import get_jobs

app = Flask("SuperScrapper")


@app.route("/")
def home():
    return render_template("potato.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        jobs = get_jobs(word)
        print(jobs)
    else:
        return redirect("/")

    return render_template("report.html",
                           searchingBy=word)


app.run()
