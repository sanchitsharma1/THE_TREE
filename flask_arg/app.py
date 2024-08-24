from flask import Flask, render_template, request
import script  # Import your external script

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    group = request.form.get("group")
    type_options = []

    if group == "1":
        type_options = ["1", "2"]
    elif group == "2":
        type_options = ["3", "4"]
    elif group == "3":
        type_options = ["5", "6"]

    if request.method == "POST" and "type" in request.form:
        type_ = request.form.get("type")
        mod = request.form.get("mod")
        output = script.execute(group, type_, mod)
    
    return render_template("home.html", group=group, type_options=type_options, output=output)

if __name__ == "__main__":
    app.run(debug=True)
