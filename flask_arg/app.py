from flask import Flask, render_template, request, redirect, url_for
import script  # Import your external script
import script2  # Import the new script
import script3  # Import the new script

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "run_script1" in request.form:
            group = request.form.get("group")
            type_ = request.form.get("type")
            mod = request.form.get("mod")
            output = script.execute(group, type_, mod)
        elif "run_script2" in request.form:
            output = script2.execute()
        elif "run_script3" in request.form:
            output = script3.execute()

        # Redirect to clear form data
        return redirect(url_for('home', output=output))
    
    output = request.args.get('output', "")
    return render_template("home.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
