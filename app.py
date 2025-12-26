import streamlit as st
import time

st.set_page_config(page_title="Neon Birthday", page_icon="✨")

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
st.markdown("### BUGÜN 29 ARALIK EN DEĞERLİ GÜNLERİMİZDEN ÇÜNKÜ SEN DOĞDUN, İYİ Kİ SENİ TANIMIŞIM🫶🏽")
st.markdown("---")

if st.button('DEVAMI İÇİN BURAYA TIKLA🤪'):
    st.balloons()
    st.snow()
    # TASARIM 5: NEON PULSING
    st.markdown("""
        <div style="text-align: center; padding: 55px 10px;">
            <h2 style="color: #FFFFFF; font-size: 38px; font-weight: 800; text-shadow: 0 0 10px #FFF, 0 0 25px #FF4B4B, 0 0 45px #FF4B4B; line-height: 1.6; font-style: italic;">
                "Hayatının geri kalanında sağlıklı ve huzurlu geçirmen dileğiyle..."
            </h2>
        </div>
        """, unsafe_allow_html=True)
    with st.spinner(''): time.sleep(5)
    st.success("## ✨ 2026 VE GÖRECEĞİMİZ YENİ YILLARDA HER ŞEY GÖNLÜMÜZCE OLSUN! ✨")
    st.info("Canım kardeşim benim, bu sürprizi sana özel Python koduyla ve yapay zeka desteğiyle hazıraldım. Sen benim hayatımdaki en ÖZEL insanlardansın. İYİ Kİ DOĞDUN, İYİ Kİ VARSIN!")
    st.markdown("<h3 class='gold-text'>✨ Bu yıl beraber yapacaklarımız:</h3>", unsafe_allow_html=True)
    st.markdown("<div class='liste-maddesi'>☕ Daha çok kahve içeceğiz</div>", unsafe_allow_html=True)
    st.markdown("<div class='liste-maddesi'>🌈 Daha güzel zamanlarımız olacak</div>", unsafe_allow_html=True)
    st.markdown("<div class='liste-maddesi'>🍀 Daha sağlıklı ve huzurlu günlerimiz olacak</div>", unsafe_allow_html=True)
    st.markdown("<div class='liste-maddesi'>😁 Daha çok güleceğiz.</div>", unsafe_allow_html=True)


