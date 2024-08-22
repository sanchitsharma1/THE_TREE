from flask import Flask, render_template, request
import ps1
import ps2
import ps3
import ps4
import ps5

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    if request.method == "POST":
        if "ps1" in request.form:
            output = ps1.run()
        elif "ps2" in request.form:
            output = ps2.run()
        elif "ps3" in request.form:
            output = ps3.run()
        elif "ps4" in request.form:
            output = ps4.run()
        elif "ps5" in request.form:
            output = ps5.run()
    return render_template("home.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
