import streamlit as st
import time

st.set_page_config(page_title="Mutlu Yıllar!", page_icon="✨")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #2d004d, #4b0082); }
    .gold-text { color: #FFD700 !important; text-align: center; font-weight: 800; font-size: 40px; }
    .stImage > img { border-radius: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin: 0 auto; display: block; }
    .glass-box { background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); padding: 30px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.2); text-align: center; margin: 20px 0; }
    div.stButton > button { background: #FF4B4B; color: white; border-radius: 50px; width: 100%; font-weight: bold; }
    .liste-maddesi { background: white; color: black !important; padding: 15px; border-radius: 12px; margin: 8px 0; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='gold-text'>🎂 İYİ Kİ DOĞDUN!</h1>", unsafe_allow_html=True)
st.image("foto.jpeg", use_container_width=True)

if st.button('Tıkla ve Sürprizi Gör 🎁'):
    st.snow()
    # SEÇENEK 2: GLASSMORPHISM
    st.markdown("""
        <div class="glass-box">
            <p style="color: white; font-size: 26px; font-weight: 900; margin: 0; line-height: 1.4;">
                HAYATININ GERİ KALANINDA<br><span style="color: #FFD700;">SAĞLIKLI VE HUZURLU</span><br>GEÇİRMEN DİLEĞİYLE
            </p>
        </div>
        """, unsafe_allow_html=True)
    with st.spinner(''): time.sleep(9)
    st.info("Sen benim hayatımdaki en ÖZEL insanlardansın. İYİ Kİ VARSIN!")
    st.markdown("<div class='liste-maddesi'>🌈 Daha güzel zamanlarımız olacak</div>", unsafe_allow_html=True)
