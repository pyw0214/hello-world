from flask import Flask, render_template

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("potato.html")



app.run()
