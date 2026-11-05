from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FORGEN</title>

        <style>

          body {
    margin: 0;
    background: #050505;
    color: white;
    font-family: Arial;
    text-align: center;
    min-height: 100vh;
    overflow-x: hidden;
}
/* FORGEN PARALLAX BACKGROUND */

body::before {
    content: "";
    position: fixed;
    inset: -30px;
    
    background: url("/static/background.png") center center / cover no-repeat;

    z-index: -2;
    pointer-events: none;
    transform: translate3d(var(--bg-x, 0px), var(--bg-y, 0px), 0) scale(1.04);
    transition: transform 0.15s ease-out;
}

/* Dark + slightly faded overlay */
body::after {
    content: "";
    position: fixed;
    inset: 0;

    background: rgba(0, 0, 0, 0.38);

    z-index: -1;
    pointer-events: none;
}
}

           nav {
    height: 70px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    padding: 0 8%;
    border-bottom: 1px solid #222;
    gap: 5px;
}
            }

            .logo {
                font-size: 28px;
                font-weight: bold;
                letter-spacing: 5px;
            }

            .hero {
    height: 85vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
            }

            h1 {
                font-size: 100px;
                letter-spacing: 15px;
                margin: 0;
                text-shadow: 0 0 30px #aaa;
            }

            p {
                color: #999;
                font-size: 20px;
            }

            button {
                margin-top: 25px;
                padding: 15px 35px;
                border: none;
                border-radius: 8px;
                font-weight: bold;
                cursor: pointer;
            }

            button:hover {
                box-shadow: 0 0 25px white;
            }

            footer {
                padding: 20px;
                color: #666;
            }
        </style>
    </head>
<script>
let targetX = 0;
let targetY = 0;

let currentX = 0;
let currentY = 0;

document.addEventListener("mousemove", (e) => {

    // Mouse position ko -1 se +1 ke range mein convert
    targetX = (e.clientX / window.innerWidth - 0.5) * 2;
    targetY = (e.clientY / window.innerHeight - 0.5) * 2;

});

function animateBackground() {

    // Smooth movement
    currentX += (targetX - currentX) * 0.04;
    currentY += (targetY - currentY) * 0.04;

    const moveX = currentX * 12;
    const moveY = currentY * 12;

    document.body.style.setProperty(
        "--bg-x",
        moveX + "px"
    );

    document.body.style.setProperty(
        "--bg-y",
        moveY + "px"
    );

    requestAnimationFrame(animateBackground);
}

animateBackground();
</script>
    <body>

        <nav>
    <div class="logo">FORGEN</div>

    <div class="nav-links">
        <a href="#">HOME</a>
        <a href="#">ABOUT</a>
        <a href="#">DISCORD</a>
    </div>
</nav>

        <div class="hero">
            <h1>FORGEN</h1>

            <p>
                A new generation gaming community.
            </p>

            <button onclick="alert('Welcome to Forgen!')">
                EXPLORE FORGEN
            </button>
        </div>

        <footer>
            © 2026 FORGEN
        </footer>
<!-- FORGEN SPRINKLE CURSOR EFFECT -->

<style>
    .sprinkle {
        position: fixed;
        width: 3px;
        height: 3px;
        border-radius: 50%;
        pointer-events: none;
        z-index: 99999;

        animation: sprinkleFall 1s ease-out forwards;
    }

    @keyframes sprinkleFall {
        0% {
            opacity: 1;
            transform: translate(0, 0) scale(1);
        }

        30% {
            opacity: 1;
        }

        100% {
            opacity: 0;
            transform: translate(var(--x), 80px) scale(0);
        }
    }
</style>

<script>
document.addEventListener("mousemove", function(event) {

    // Har mouse movement par 2-4 sparkles
    const amount = Math.floor(Math.random() * 3) + 2;

    for (let i = 0; i < amount; i++) {

        const sparkle = document.createElement("div");
        sparkle.classList.add("sprinkle");

        // Random white / light purple
        if (Math.random() < 0.5) {
            sparkle.style.background = "white";
            sparkle.style.boxShadow = "0 0 8px white";
        } else {
            sparkle.style.background = "#d8b4fe";
            sparkle.style.boxShadow = "0 0 8px #c084fc";
        }

        // Mouse ke aas-paas random position
        sparkle.style.left = event.clientX + (Math.random() * 14 - 7) + "px";
        sparkle.style.top = event.clientY + (Math.random() * 8 - 4) + "px";

        // Neeche girte waqt thoda left/right move
        sparkle.style.setProperty(
            "--x",
            (Math.random() * 50 - 25) + "px"
        );

        // Different sizes
        const size = Math.random() * 3 + 2;
        sparkle.style.width = size + "px";
        sparkle.style.height = size + "px";

        // Different falling speeds
        sparkle.style.animationDuration =
            (Math.random() * 0.6 + 0.7) + "s";

        document.body.appendChild(sparkle);

        // Remove after animation
        setTimeout(() => {
            sparkle.remove();
        }, 1400);
    }
});
</script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
    
# ==============================
# ZXForgen Signup / Login System
# ==============================

import sqlite3
import os
from flask import request, redirect, session, render_template_string
from werkzeug.security import generate_password_hash, check_password_hash

# Session security
app.secret_key = os.environ.get("SECRET_KEY", "zxforgen-change-this-secret-key")

# Database
DATABASE = os.path.join(app.root_path, "users.db")


def init_user_database():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)


init_user_database()


AUTH_STYLE = """
<style>
body {
    margin: 0;
    background: #050505;
    color: white;
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}
.auth-box {
    width: 340px;
    padding: 35px;
    background: #10080d;
    border: 1px solid #a20d35;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 0 20px #a20d3533;
}
h1 { letter-spacing: 4px; }
input {
    box-sizing: border-box;
    width: 100%;
    padding: 13px;
    margin: 9px 0;
    background: #080808;
    border: 1px solid #444;
    color: white;
    border-radius: 5px;
}
button {
    width: 100%;
    padding: 13px;
    margin-top: 12px;
    background: #a20d35;
    color: white;
    border: 0;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
}
a { color: #ff456e; }
.message { color: #ff6688; }
</style>
"""


@app.route("/signup/", methods=["GET", "POST"])
def signup():
    message = ""

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not username or not email or len(password) < 8:
            message = "Fill all fields. Password must be at least 8 characters."
        else:
            try:
                with sqlite3.connect(DATABASE) as conn:
                    conn.execute(
                        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                        (username, email, generate_password_hash(password))
                    )
                return redirect("/login/")
            except sqlite3.IntegrityError:
                message = "This email is already registered."

    return render_template_string("""
    """ + AUTH_STYLE + """
    <div class="auth-box">
        <h1>SIGN UP</h1>
        <p class="message">{{ message }}</p>
        <form method="POST">
            <input name="username" placeholder="Username" required>
            <input name="email" type="email" placeholder="Email" required>
            <input name="password" type="password" placeholder="Password (8+ characters)" required minlength="8">
            <button type="submit">CREATE ACCOUNT</button>
        </form>
        <p>Already have an account? <a href="/login/">Log In</a></p>
        <a href="/">Back to Home</a>
    </div>
    """, message=message)


@app.route("/login/", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        with sqlite3.connect(DATABASE) as conn:
            user = conn.execute(
                "SELECT id, username, password FROM users WHERE email = ?",
                (email,)
            ).fetchone()

        if user and check_password_hash(user[2], password):
            session["user_id"] = user[0]
            session["username"] = user[1]
            return redirect("/")
        else:
            message = "Incorrect email or password."

    return render_template_string("""
    """ + AUTH_STYLE + """
    <div class="auth-box">
        <h1>LOG IN</h1>
        <p class="message">{{ message }}</p>
        <form method="POST">
            <input name="email" type="email" placeholder="Email" required>
            <input name="password" type="password" placeholder="Password" required>
            <button type="submit">LOG IN</button>
        </form>
        <p>New here? <a href="/signup/">Create Account</a></p>
        <a href="/">Back to Home</a>
    </div>
    """, message=message)


@app.route("/logout/")
def logout():
    session.clear()
    return redirect("/")
