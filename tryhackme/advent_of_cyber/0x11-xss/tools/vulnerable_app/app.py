from flask import Flask, request, render_template_string

app = Flask(__name__)

comments = []  # Simulated DB


@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest")
    return f"<h1>Hello, {name}!</h1>"  # Vulnerable reflected


@app.route("/comments", methods=["GET", "POST"])
def comments_page():
    if request.method == "POST":
        comments.append(request.form["comment"])  # Vulnerable stored
    return render_template_string("".join(f"<p>{c}</p>" for c in comments))


if __name__ == "__main__":
    app.run(debug=True)
