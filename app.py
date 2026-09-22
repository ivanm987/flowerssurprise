import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64


# =========================
# CONFIGURACIÓN
# =========================

st.set_page_config(
    page_title="For you ❤️",
    page_icon="🌷",
    layout="centered"
)


# =========================
# CARGAR IMÁGENES
# =========================

BASE = Path(__file__).parent
ASSETS = BASE / "assets"


def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


orquidea = image_to_base64("orquidea.jpg")
middlemist = image_to_base64("middlemist.jpg")
cerezo = image_to_base64("cerezo.jpg")
tulipan = image_to_base64("tulipan.jpg")
gatitos = image_to_base64("gatitos.jpg")


# =========================
# YOUTUBE
# =========================

# CAMBIA ESTO por el ID de tu video de YouTube
youtube_id = "https://www.youtube.com/watch?v=yKNxeF4KMsY&list=RDyKNxeF4KMsY&start_radio=1"


# =========================
# HTML
# =========================

html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<style>

body {{
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #fff0f5, #ffe4ec);
    font-family: Georgia, serif;
    text-align: center;
    color: #5a3040;
}}

.container {{
    max-width: 600px;
    margin: auto;
    padding: 25px;
}}

h1 {{
    font-size: 42px;
    margin-bottom: 10px;
}}

.subtitle {{
    font-size: 20px;
    margin-bottom: 30px;
}}

.start-btn {{
    background: #d94f70;
    color: white;
    border: none;
    padding: 15px 35px;
    border-radius: 30px;
    font-size: 18px;
    cursor: pointer;
    box-shadow: 0 5px 15px rgba(0,0,0,0.15);
}}

.start-btn:hover {{
    transform: scale(1.05);
}}

#flowers {{
    display: none;
}}

.flower {{
    margin-top: 40px;
    margin-bottom: 50px;
}}

.flower-title {{
    font-size: 26px;
    margin-bottom: 15px;
}}

.scratch-container {{
    position: relative;
    width: 300px;
    height: 300px;
    margin: auto;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 5px 20px rgba(0,0,0,0.15);
}}

.flower-image {{
    width: 100%;
    height: 100%;
    object-fit: cover;
}}

canvas {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}}

.cover-text {{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-size: 24px;
    font-weight: bold;
    pointer-events: none;
    text-shadow: 0 2px 5px black;
    transition: opacity 0.4s ease;
}}

.message {{
    margin-top: 18px;
    font-size: 21px;
    font-style: italic;
    padding: 0 20px;
}}

.final {{
    margin-top: 60px;
    padding-bottom: 50px;
}}

.final img {{
    width: 300px;
    max-width: 90%;
    border-radius: 25px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}}

.love {{
    font-size: 45px;
    color: #d94f70;
    margin-top: 20px;
}}

.music {{
    display: none;
}}

</style>

</head>


<body>

<div class="container">

    <h1>🌸 Para ti ❤️</h1>

    <div class="subtitle">
        Hice algo pequeñito para ti...
    </div>


    <button class="start-btn" onclick="startSurprise()">
        COMENZAR ❤️
    </button>


    <div id="flowers">


        <!-- ========================= -->
        <!-- ORQUÍDEA -->
        <!-- ========================= -->

        <div class="flower">

            <div class="flower-title">
                🌺
            </div>

            <div class="scratch-container">

                <img
                    class="flower-image"
                    src="data:image/jpeg;base64,{orquidea}"
                >

                <canvas></canvas>

                <div class="cover-text">
                    Raspa aquí
                </div>

            </div>

            <div class="message">
                por cada vez que me haces sonreír
            </div>

        </div>



        <!-- ========================= -->
        <!-- MIDDLEMIST'S RED -->
        <!-- ========================= -->

        <div class="flower">

            <div class="flower-title">
                🌹
            </div>

            <div class="scratch-container">

                <img
                    class="flower-image"
                    src="data:image/jpeg;base64,{middlemist}"
                >

                <canvas></canvas>

                <div class="cover-text">
                    Raspa aquí
                </div>

            </div>

            <div class="message">
                porque eres difícil de encontrar
            </div>

        </div>



        <!-- ========================= -->
        <!-- CEREZO -->
        <!-- ========================= -->

        <div class="flower">

            <div class="flower-title">
                🌸
            </div>

            <div class="scratch-container">

                <img
                    class="flower-image"
                    src="data:image/jpeg;base64,{cerezo}"
                >

                <canvas></canvas>

                <div class="cover-text">
                    Raspa aquí
                </div>

            </div>

            <div class="message">
                por todo lo bonito que todavía nos falta vivir
            </div>

        </div>



        <!-- ========================= -->
        <!-- TULIPÁN -->
        <!-- ========================= -->

        <div class="flower">

            <div class="flower-title">
                🌷
            </div>

            <div class="scratch-container">

                <img
                    class="flower-image"
                    src="data:image/jpeg;base64,{tulipan}"
                >

                <canvas></canvas>

                <div class="cover-text">
                    Raspa aquí
                </div>

            </div>

            <div class="message">
                por los momentos que pasamos juntos
            </div>

        </div>



        <!-- ========================= -->
        <!-- FINAL -->
        <!-- ========================= -->

        <div class="final">

            <img
                src="data:image/jpeg;base64,{gatitos}"
            >

            <div class="love">
                Te amo ❤️
            </div>

        </div>

    </div>

</div>



<!-- ========================= -->
<!-- YOUTUBE -->
<!-- ========================= -->

<div class="music">

    <iframe
        id="youtube"
        width="1"
        height="1"
        src="https://www.youtube.com/embed/{youtube_id}?enablejsapi=1&playsinline=1"
        frameborder="0"
        allow="autoplay"
    >
    </iframe>

</div>



<script>

let player;


function startSurprise() {{

    document.getElementById("flowers").style.display = "block";

    document.querySelector(".start-btn").style.display = "none";

    // Intentar reproducir YouTube
    if (player) {{
        player.playVideo();
    }}

}}



// =========================
// YOUTUBE API
// =========================

function onYouTubeIframeAPIReady() {{

    player = new YT.Player("youtube", {{

        events: {{

            "onReady": function(event) {{

                // No reproducimos automáticamente aquí.
                // El botón COMENZAR dará la interacción necesaria.
            }}

        }}

    }});

}}


</script>


<script src="https://www.youtube.com/iframe_api"></script>



<script>

// =========================
// SCRATCH CARDS
// =========================

document.querySelectorAll(".scratch-container").forEach(container => {{

    const canvas = container.querySelector("canvas");

    const ctx = canvas.getContext("2d");

    const coverText = container.querySelector(".cover-text");

    let drawing = false;
    let started = false;


    function resizeCanvas() {{

        canvas.width = container.offsetWidth;
        canvas.height = container.offsetHeight;

        ctx.fillStyle = "#c9c9c9";

        ctx.fillRect(
            0,
            0,
            canvas.width,
            canvas.height
        );

    }}


    resizeCanvas();


    function scratch(x, y) {{

        ctx.globalCompositeOperation = "destination-out";

        ctx.beginPath();

        ctx.arc(
            x,
            y,
            25,
            0,
            Math.PI * 2
        );

        ctx.fill();


        if (!started) {{

            started = true;

            coverText.style.opacity = "0";

        }}

    }}


    canvas.addEventListener("pointerdown", function(e) {{

        drawing = true;

        const rect = canvas.getBoundingClientRect();

        scratch(
            e.clientX - rect.left,
            e.clientY - rect.top
        );

    }});


    canvas.addEventListener("pointermove", function(e) {{

        if (!drawing) return;

        const rect = canvas.getBoundingClientRect();

        scratch(
            e.clientX - rect.left,
            e.clientY - rect.top
        );

    }});


    canvas.addEventListener("pointerup", function() {{

        drawing = false;

    }});


    canvas.addEventListener("pointerleave", function() {{

        drawing = false;

    }});

}});

</script>


</body>

</html>
"""


# =========================
# MOSTRAR
# =========================

components.html(
    html,
    height=1800,
    scrolling=True
)
