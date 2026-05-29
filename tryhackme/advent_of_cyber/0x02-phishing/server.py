from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Change this in real deployments!

# Simulated user database (in real scenarios, this would be a proper database)
users = {"admin": "S@ntaCl4us2025!"}

# Flag for the task (this is what participants need to capture)
FLAG = "THM{PH1SH1NG_M3RRY_CL1CKM4S}"


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Check credentials
    if username in users and users[username] == password:
        session["username"] = username
        # Log the successful phish (this is visible in the task for learning purposes)
        print(
            f"[+] Phishing successful! Captured credentials -> Username: {username}, Password: {password}"
        )
        print(f"[+] Flag for the victim: {FLAG}")
        return redirect(url_for("dashboard"))
    else:
        return render_template("login.html", error="Invalid credentials. Try again!")


@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("index"))
    return render_template("dashboard.html", flag=FLAG)


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    # In the TryHackMe task, this runs on 0.0.0.0:80 inside the vulnerable machine
    app.run(host="0.0.0.0", port=80)
