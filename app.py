# app.py
import streamlit as st
import random
import os

st.set_page_config(page_title="🎮 Sociedad de Brainrots 🎮", layout="centered")

# --- Reglas de tu archivo original ---
reglas = [
    "No spam.",
    "Respetar a los integrantes.",
    "No enviar links que no sean del juego.",
    "Todos los trades con admin."
]

# --- ASCII COMPLETO PEGADO AQUÍ ---
ascii_art = r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⢤⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡦⠤⠤⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⣀⣀⠠⠤⠤⠤⠐⠒⠒⠲⣦⠀⢿⣄⣠⣤⣤⣤⣤⣿⡽⢀⣤⠤⠤⠤⠶⠖⠲⠲⣦⣹⡇⠀⠀⠀⣽⣇⣴⡶⠶⠶⠶⠶⠶⠶⣦⡀⠀⠀⠀⠀⠀⠀⣀⣴⠶⢤⣄⣀⣀⠀⠀⠀
⣿⡇⠀⢀⣀⣀⡀⠀⠀⠀⠀⢻⡷⠖⠛⠛⠒⠒⠒⠒⠚⣷⣸⡇⠀⠀⣤⣄⣀⣀⠀⠀⠙⢧⠀⠀⠀⣿⡿⠁⠀⠀⠀⠀⢀⠀⠀⠀⣷⡤⠶⠶⡆⣠⡾⠋⠀⠀⠀⢈⣽⣯⠟⠂⠀
⢸⡇⠀⠘⣯⣭⡽⠇⠀⠀⠀⠘⡏⠀⢀⣀⣀⡀⠀⠀⠀⠘⣿⡇⠀⠀⢻⣀⣬⠏⠀⠀⠀⡾⠀⠀⠀⣿⣽⠀⠀⣤⡶⠿⣿⡆⠀⠻⣅⠀⠀⠀⠙⠋⠀⠀⠀⣠⣾⠟⠋⠀⠀⠀⠀
⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⢸⣏⠉⠹⣷⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠀⠀⠀⣿⣏⠀⠀⢹⡀⠀⢱⣿⠀⠀⢀⣿⣆⠀⠀⠀⠀⠀⣾⣿⠁⠀⠀⠀⠀⠀⠀
⢸⣿⠀⠘⣿⡄⠈⠻⣿⡛⠛⣿⠀⠀⠸⣿⣀⡤⠟⠃⠀⠀⠘⡇⠀⠀⣶⠚⢿⡇⠀⠈⠙⢺⡀⠀⢰⣯⢻⡄⠀⠈⢧⣀⣠⣿⠀⠀⢸⡟⠁⠀⠀⠀⠀⠀⠛⠳⢦⣄⣀⠀⠀
⢘⣾⠀⠀⢹⣷⡄⠀⠀⠻⢶⣿⣦⡀⠀⠁⠀⠀⠀⢀⣀⣀⣠⡗⠀⠀⠻⠳⠿⠀⠀⠀⢀⣾⠀⠀⠈⠉⢉⣁⣸⠂⠈⠀⠀⠀⠀⢴⣋⡀⠀⠀⢀⣼⣶⣄⠀⠀⠀⠀⣈⣿⢿⠶
⠈⠛⠳⠶⢾⣷⣳⣄⢀⣀⣈⣫⣿⣟⡛⠛⠛⠛⠛⠛⠋⠉⢿⣦⣤⣤⣴⣤⠶⠶⠶⠶⠾⢿⠶⠶⠛⠛⠋⠙⢷⡴⠶⠶⠶⠶⠶⠾⠋⠛⠻⠶⣾⠃⠻⢿⣦⣀⣤⣾⠿⠋⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠋⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠋⠁⠀⠀⠀⠀"""

# --- CSS estilo neón, sombras, botones gamer ---
st.markdown(
    """
    <style>
    .stApp { background: #05050b; color: #e6fff9; }

    .neon-title {
      font-family: "Comic Sans MS", sans-serif;
      font-size: 28px;
      color: #00ffea;
      text-align:center;
      text-shadow: 0 0 6px #00ffe6, 0 0 12px #00d4ff, 0 0 20px #ff1493;
      margin-bottom: 6px;
    }

    .ascii {
      font-family: "Courier New", monospace;
      font-size: 7px;
      color:#00ffea;
      white-space: pre;
      overflow:auto;
      line-height: 8px;
    }

    .footer {
      text-align:center;
      color:#00ff7f;
      font-style:italic;
      margin-top:8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Canvas de estrellas + destellos ---
st.components.v1.html(
    """
    <canvas id="starfield" style="position:fixed; inset:0; z-index:-1;"></canvas>
    <script>
    const canvas=document.getElementById('starfield');
    const ctx=canvas.getContext('2d');

    function resize(){
      canvas.width=window.innerWidth;
      canvas.height=window.innerHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    const stars=[];
    const N=120;
    for(let i=0;i<N;i++){
      stars.push({
        x:Math.random()*canvas.width,
        y:Math.random()*canvas.height,
        r:Math.random()*2+1,
        v:Math.random()*1+0.3,
        b:Math.floor(Math.random()*155)+100
      });
    }

    function draw(){
      ctx.clearRect(0,0,canvas.width,canvas.height);
      for(const s of stars){
        s.y+=s.v;
        if(s.y>canvas.height){
          s.y=0;
          s.x=Math.random()*canvas.width;
        }
        ctx.beginPath();
        ctx.fillStyle=`rgba(0,255,${s.b},0.9)`;
        ctx.arc(s.x,s.y,s.r,0,Math.PI*2);
        ctx.fill();
      }
      requestAnimationFrame(draw);
    }
    draw();

    // Destello al hacer click
    canvas.addEventListener('click', e=>{
      const x=e.clientX, y=e.clientY;
      for(let i=0;i<20;i++){
        const p=document.createElement('div');
        p.style.position='fixed';
        p.style.left=x+'px';
        p.style.top=y+'px';
        p.style.width='10px';
        p.style.height='10px';
        p.style.borderRadius='50%';
        const colors=['#00ffff','#ff00ff','#ffff00','#00ffea','#ff1493'];
        p.style.background=colors[Math.floor(Math.random()*colors.length)];
        p.style.zIndex=99999;
        document.body.appendChild(p);
        const dx=(Math.random()-0.5)*250;
        const dy=(Math.random()-0.5)*250;
        p.animate([
          { transform:'translate(0,0)', opacity:1 },
          { transform:`translate(${dx}px,${dy}px) scale(0.2)`, opacity:0 }
        ], { duration:900, easing:'ease-out' });
        setTimeout(()=>p.remove(),1000);
      }
      const audio=document.getElementById('sfx');
      if(audio){ audio.play().catch(()=>{}); }
    });
    </script>
    """,
    height=0,
)

# Intentar cargar audio si existe
audio_html = ""
if os.path.exists("power-up.wav"):
    audio_html = '<audio id="sfx" src="power-up.wav"></audio>'
else:
    audio_html = '<audio id="sfx"></audio>'

st.components.v1.html(audio_html, height=0)

# --- Layout de la app ---
st.markdown('<div class="neon-title">🎮 Sociedad de Brainrots 🎮</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    st.markdown(f'<div class="ascii">{ascii_art}</div>', unsafe_allow_html=True)

with col2:
    st.markdown("### Reglas")
    for i, regla in enumerate(reglas):
        if st.button(f"Regla {i+1}"):
            with st.modal(f"Regla {i+1}"):
                st.write(regla)
                if os.path.exists("power-up.wav"):
                    audio_bytes = open("power-up.wav","rb").read()
                    st.audio(audio_bytes, format="audio/wav")
                st.button("Cerrar")

    st.write("---")

    if st.button("👋 Bienvenida"):
        with st.modal("¡Bienvenido!"):
            st.write("¡Bienvenido a la Sociedad de Brainrots! Sigue las reglas y diviértete.")
            if os.path.exists("power-up.wav"):
                audio_bytes=open("power-up.wav","rb").read()
                st.audio(audio_bytes, format="audio/wav")
            st.button("✨ OK ✨")

st.markdown('<div class="footer">⚡️ Respeta las reglas y diviértete ⚡️</div>', unsafe_allow_html=True)
