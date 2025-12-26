import streamlit as st
import time

st.set_page_config(page_title="İyi ki Doğdun Can Dost İyi ki Varsın !", page_icon="✨")

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
    # PROFESYONEL YAZI TASARIMI 1
    st.markdown("""
        <div style="text-align: center; padding: 40px 10px; border-radius: 20px; border: 3px solid #FFD700; background: rgba(0,0,0,0.4); margin: 25px 0; box-shadow: 0px 0px 30px rgba(255, 215, 0, 0.4);">
            <h1 style="color: #FFD700; font-family: 'Playfair Display', serif; font-size: 38px; line-height: 1.5; text-shadow: 2px 2px 15px rgba(255,215,0,0.5); margin: 0;">
                HAYATININ GERİ KALANINDA<br>SAĞLIKLI VE HUZURLU<br>GEÇİRMEN DİLEĞİYLE
            </h1>
        </div>
        """, unsafe_allow_html=True)
    with st.spinner(''): time.sleep(9)
    st.success("## ✨ 2026 VE GÖRECEĞİMİZ YENİ YILLAR DİLEDİĞİMİZ ŞEKİLDE OLSUN! ✨")
    st.info("Canım kardeşim benim, bu satırları sana özel Python koduyla ve yapay zeka desteğiyle yazmak istedim. Sen benim hayatımdaki en ÖZEL insanlardansın. İYİ Kİ DOĞDUN, İYİ Kİ VARSIN!")
    st.markdown("<h3 class='gold-text'>✨ Bu yıl beraber yapacaklarımız:</h3>", unsafe_allow_html=True)
    st.markdown("<div class='liste-maddesi'>☕ Daha çok kahve içeceğiz</div>", unsafe_allow_html=True)
    st.markdown("<div class='liste-maddesi'>🌈 Daha güzel zamanlarımız olacak</div>", unsafe_allow_html=True)
    st.markdown("<div class='liste-maddesi'>🍀 Daha sağlıklı ve huzurlu günlerimiz olacak</div>", unsafe_allow_html=True)
    st.markdown("<div class='liste-maddesi'>😁 Daha çok güleceğiz.</div>", unsafe_allow_html=True)
