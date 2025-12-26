import streamlit as st
import time

st.set_page_config(page_title="İyi ki Doğdun!", page_icon="✨")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #4b0082, #8a2be2); }
    .gold-text { color: #FFD700 !important; text-align: center; font-weight: bold; }
    .stImage > img { border-radius: 20px; border: 2px solid #FFD700; display: block; margin: 0 auto; image-rendering: -webkit-optimize-contrast; }
    div.stButton > button { display: block; margin: 0 auto; background-color: #FF4B4B; color: white; border-radius: 30px; padding: 10px 25px; border: none; font-size: 20px; }
    .liste-maddesi { background-color: rgba(255, 255, 255, 0.85); color: #000000 !important; padding: 12px; border-radius: 15px; margin: 10px auto; width: 85%; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='gold-text'>🎂 İyi ki Doğdun Canım Benim! 🎂</h1>", unsafe_allow_html=True)
try: st.image("foto.jpeg", use_container_width=True)
except: st.error("foto.jpeg bulunamadı.")

if st.button('Doğum Günü Kızı Buraya Tıkla 🎁'):
    st.balloons()
    # SEÇENEK 1: ROYAL GOLD
    st.markdown("""
        <div style="text-align: center; padding: 25px; border-radius: 15px; border: 2px solid #FFD700; background: rgba(0,0,0,0.3); margin: 20px 0;">
            <h2 style="color: #FFD700; font-family: 'Georgia', serif; letter-spacing: 1px; line-height: 1.4;">
                HAYATININ GERİ KALANINDA SAĞLIKLI VE HUZURLU GEÇİRMEN DİLEĞİYLE
            </h2>
        </div>
        """, unsafe_allow_html=True)
    with st.spinner(''): time.sleep(9)
    st.info("Canım kardeşim benim, iyi ki doğdun, iyi ki varsın!")
    st.markdown("<div class='liste-maddesi'>☕ Daha çok kahve içeceğiz</div>", unsafe_allow_html=True)
