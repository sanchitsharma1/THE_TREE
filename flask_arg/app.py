from flask import Flask, render_template, request
import script  # Import your external script

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    if request.method == "POST":
        group = request.form.get("group")
        type_ = request.form.get("type")
        mod = request.form.get("mod")
        output = script.execute(group, type_, mod)
    return render_template("home.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
