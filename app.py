import streamlit as st
import time

st.set_page_config(page_title="Mutlu Yıllar!", page_icon="✨")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #4b0082, #8a2be2); }
    h1, h3, [data-testid="stMarkdownContainer"] p { text-align: center; color: #FFFFFF !important; }
    .gold-text { color: #FFD700 !important; text-align: center; font-weight: bold; }
    .stImage > img { border-radius: 20px; border: 2px solid #FFD700; display: block; margin: 0 auto; }
    div.stButton > button { display: block; margin: 0 auto; background-color: #FF4B4B; color: white; border-radius: 30px; padding: 10px 25px; font-size: 20px; }
    .liste-maddesi { background-color: rgba(255, 255, 255, 0.85); color: #000000 !important; padding: 12px; border-radius: 15px; margin: 10px auto; width: 85%; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='gold-text'>🎂 İyi ki Doğdun Canım Benim! 🎂</h1>", unsafe_allow_html=True)
try: st.image("foto.jpeg", use_container_width=True)
except: st.error("Fotoğraf bulunamadı!")
st.markdown("### BUGÜN 29 ARALIK EN DEĞERLİ GÜNLERİMİZDEN ÇÜNKÜ SEN DOĞDUN, İYİ Kİ SENİ TANIMIŞIM.")
st.markdown("---")

if st.button('Doğum Günü Kızı Buraya Tıkla 🎁'):
    st.balloons()
    st.snow()
    # TASARIM 2: GLASSMORPHISM
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(15px); padding: 50px 15px; border-radius: 30px; border: 2px solid rgba(255,255,255,0.4); box-shadow: 0 15px 35px rgba(0,0,0,0.5); margin: 30px 0;">
            <p style="color: white; font-size: 34px; font-weight: 900; text-align: center; margin: 0; line-height: 1.4; text-transform: uppercase; letter-spacing: 2px;">
                HAYATININ GERİ KALANINDA<br><span style="color: #FFD700;">SAĞLIKLI VE HUZURLU</span><br>GEÇİRMEN DİLEĞİYLE
            </p>
        </div>
        """, unsafe_allow_html=True)
    with st.spinner(''): time.sleep(9)
    st.success("## ✨ 2026 VE GÖRECEĞİMİZ YENİ YILLAR DİLEDİĞİMİZ ŞEKİLDE OLSUN! ✨")
    st.info("Canım kardeşim benim, bu satırları sana özel Python koduyla ve yapay zeka desteğiyle yazmak istedim. Sen benim hayatımdaki en ÖZEL insanlardansın. İYİ Kİ DOĞDUN, İYİ Kİ VARSIN!")
    st.markdown("<h3 class='gold-text'>✨ Bu yıl
