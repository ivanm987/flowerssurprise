import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

# ---------------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------------

st.set_page_config(
    page_title="Para ti ❤️",
    page_icon="🌸",
    layout="centered"
)

# ---------------------------------------------------------
# FUNCIONES
# ---------------------------------------------------------

def image_to_base64(path):
    """Convierte una imagen local a Base64 para mostrarla en HTML."""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def audio_to_base64(path):
    """Convierte el audio local a Base64."""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# ---------------------------------------------------------
# ARCHIVOS
# ---------------------------------------------------------

orquidea = image_to_base64("orquidea.jpg")
middlemist = image_to_base64("middlemist.jpg")
cerezo = image_to_base64("cerezo.jpg")
tulipan = image_to_base64("tulipan.jpg")
gatitos = image_to_base64("gatitos.jpg")

yellow = audio_to_base64("yellow.mp3")


# ---------------------------------------------------------
# HTML
# ---------------------------------------------------------

html = f"""
<!DOCTYPE html>

<html>

<head>

<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    padding: 0;
    font-family: Georgia, serif;
    background: linear-gradient(
        135deg,
        #fff7fb,
        #fffaf0,
        #f9f4ff
    );
    color: #4b3540;
}}

.container {{
    max-width: 950px;
    margin: auto;
    padding: 25px;
    text-align: center;
}}

h1 {{
    font-size: 42px;
    margin-bottom: 5px;
    color: #8b4567;
}}

.subtitle {{
    font-size: 18px;
    margin-bottom: 30px;
    color: #765b68;
}}

.instructions {{
    background: rgba(255,255,255,0.75);
    border-radius: 20px;
    padding: 15px;
    margin-bottom: 30px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
}}

.flowers {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 25px;
}}

.card {{
    position: relative;
    height: 390px;
    border-radius: 25px;
    overflow: hidden;
    background: white;
    box-shadow: 0 8px 25px rgba(0,0,0,0.12);
}}

.flower-image {{
    width: 100%;
    height: 100%;
    object-fit: cover;
}}

.message {{
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;

    background: rgba(255,255,255,0.92);

    padding: 20px;

    font-size: 20px;
    line-height: 1.5;

    color: #633f50;
}}

.flower-name {{
    font-size: 25px;
    font-weight: bold;
    margin-bottom: 8px;
}}

.scratch {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    cursor: crosshair;
    z-index: 5;
}}

.cover-text {{
    position: absolute;
    z-index: 6;

    top: 50%;
    left: 50%;

    transform: translate(-50%, -50%);

    color: white;

    font-size: 22px;
    font-weight: bold;

    text-shadow:
        0 2px 5px rgba(0,0,0,0.6);

    pointer-events: none;
}}

.final {{
    margin-top: 50px;
    padding: 35px;

    background: rgba(255,255,255,0.8);

    border-radius: 30px;

    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}}

.final img {{
    width: 100%;
    max-width: 500px;
    border-radius: 25px;
}}

.final h2 {{
    font-size: 40px;
    color: #a13f65;
}}

.final p {{
    font-size: 22px;
}}

.music {{
    margin: 20px auto;
    max-width: 500px;
}}

@media (max-width: 700px) {{

    .flowers {{
        grid-template-columns: 1fr;
    }}

    h1 {{
        font-size: 32px;
    }}

    .card {{
        height: 360px;
    }}

}}

</style>

</head>


<body>

<div class="container">

<h1>🌸 Para ti 🌸</h1>

<div class="subtitle">
Hay algunas cosas que quería decirte...
</div>

<div class="instructions">

<strong>Una pequeña sorpresa para ti</strong>

<br><br>

Raspa cada tarjeta con tu dedo o con el mouse
para descubrir lo que hay debajo. ❤️

</div>


<div class="flowers">


<!-- ORQUÍDEA -->

<div class="card">

<img
class="flower-image"
src="data:image/jpeg;base64,{orquidea}"
>

<div class="message">

<div class="flower-name">
🌺 Orquídea
</div>

Por cada vez que me haces sonreír.

</div>

<canvas class="scratch"></canvas>

<div class="cover-text">
✨ Raspa aquí ✨
</div>

</div>


<!-- MIDDLEMIST -->

<div class="card">

<img
class="flower-image"
src="data:image/jpeg;base64,{middlemist}"
>

<div class="message">

<div class="flower-name">
🌹 Middlemist's Red
</div>

Porque eres difícil de encontrar.

</div>

<canvas class="scratch"></canvas>

<div class="cover-text">
✨ Raspa aquí ✨
</div>

</div>


<!-- CEREZO -->

<div class="card">

<img
class="flower-image"
src="data:image/jpeg;base64,{cerezo}"
>

<div class="message">

<div class="flower-name">
🌸 Flor de cerezo
</div>

Por todo lo bonito que todavía
nos falta vivir.

</div>

<canvas class="scratch"></canvas>

<div class="cover-text">
✨ Raspa aquí ✨
</div>

</div>


<!-- TULIPÁN -->

<div class="card">

<img
class="flower-image"
src="data:image/jpeg;base64,{tulipan}"
>

<div class="message">

<div class="flower-name">
🌷 Tulipán
</div>

Por todos los momentos
que pasamos juntos.

</div>

<canvas class="scratch"></canvas>

<div class="cover-text">
✨ Raspa aquí ✨
</div>

</div>


</div>


<!-- FINAL -->

<div class="final">

<h2>❤️ Y todavía falta una cosa... ❤️</h2>

<img src="data:image/jpeg;base64,{gatitos}">

<h2>Te amo</h2>

<p>
Más de lo que estas cuatro flores
pueden explicar. 🐱❤️
</p>

</div>


<!-- MÚSICA -->

<div class="music">

<audio controls loop>

<source
src="data:audio/mpeg;base64,{yellow}"
type="audio/mpeg"
>

</audio>

<p>
🎵 Nuestra canción
</p>

</div>


</div>


<script>

const canvases = document.querySelectorAll(".scratch");


canvases.forEach(canvas => {{

    const ctx = canvas.getContext("2d");

    function resizeCanvas() {{

        const rect = canvas.getBoundingClientRect();

        canvas.width = rect.width;
        canvas.height = rect.height;

        // Capa que se raspa
        ctx.fillStyle = "#d9b6c5";
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Patrón visual
        ctx.fillStyle = "rgba(255,255,255,0.25)";

        for(let x = 0; x < canvas.width; x += 30) {{
            for(let y = 0; y < canvas.height; y += 30) {{
                ctx.beginPath();
                ctx.arc(x, y, 2, 0, Math.PI * 2);
                ctx.fill();
            }}
        }}

    }}

    resizeCanvas();

    let drawing = false;


    function scratch(x, y) {{

        ctx.globalCompositeOperation = "destination-out";

        ctx.beginPath();

        ctx.arc(x, y, 25, 0, Math.PI * 2);

        ctx.fill();

    }}


    function getPosition(e) {{

        const rect = canvas.getBoundingClientRect();

        if(e.touches) {{

            return {{

                x: e.touches[0].clientX - rect.left,

                y: e.touches[0].clientY - rect.top

            }};

        }}

        return {{

            x: e.clientX - rect.left,

            y: e.clientY - rect.top

        }};

    }}


    canvas.addEventListener("mousedown", function(e) {{

        drawing = true;

        const p = getPosition(e);

        scratch(p.x, p.y);

    }});


    canvas.addEventListener("mousemove", function(e) {{

        if(!drawing) return;

        const p = getPosition(e);

        scratch(p.x, p.y);

    }});


    canvas.addEventListener("mouseup", function() {{

        drawing = false;

    }});


    canvas.addEventListener("mouseleave", function() {{

        drawing = false;

    }});


    canvas.addEventListener("touchstart", function(e) {{

        e.preventDefault();

        drawing = true;

        const p = getPosition(e);

        scratch(p.x, p.y);

    }}, {{passive:false}});


    canvas.addEventListener("touchmove", function(e) {{

        e.preventDefault();

        if(!drawing) return;

        const p = getPosition(e);

        scratch(p.x, p.y);

    }}, {{passive:false}});


    canvas.addEventListener("touchend", function() {{

        drawing = false;

    }});

}});

</script>


</body>

</html>
"""


components.html(
    html,
    height=1500,
    scrolling=True
)

BASE = Path(__file__).parent
ASSETS = BASE / "assets"

orquidea = "orquidea.jpg"
middlemist = "middlemist.jpg"
cerezo =  "cerezo.jpg"
tulipan =  "tulipan.jpg"
gatitos =  "gatitos.jpg"
yellow =  "yellow.mp3"
