from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def forside():
    # Definer parameter 'name' som overføres til template
    name = request.args.get("name", "Gods_Black_angel")
    return render_template("index.html", name=name, title="Black Angel")

@app.route("/Fanfick")
def fanfic():
    # Definer parameter 'name' som overføres til template
    name = request.args.get("name", "Gods_Black_angel")
    return render_template("index_v2.html", name=name, title="Fanfic")

# Start Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)