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