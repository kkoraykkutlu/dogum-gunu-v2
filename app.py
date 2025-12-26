import streamlit as st
import time

st.set_page_config(page_title="İyi ki Doğdun Can Dost İyi ki Varsın !", page_icon="✨")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #1e3c72, #2a5298);
    }
    h1, h3, [data-testid="stMarkdownContainer"] p {
        text-align: center;
        color: #FFFFFF !important;
    }
    .gold-text {
        color: #FFD700 !important;
        text-align: center;
        font-weight: bold;
    }
    div.stButton > button {
        display: block;
        margin: 0 auto;
        background-color: #FF4B4B;
        color: white;
        border-radius: 30px;
        padding: 10px 25px;
        border: none;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

if st.button('Doğum Günü Kızı Buraya Tıkla 🎁'):
    st.balloons()
    st.snow()
    with st.spinner('HAYATININ GERİ KALANININ DA SAĞLIKLI, HUZURLU VE HEP BERABER GEÇİRMEMİZ DİLEĞİYLE'):
        time.sleep(5)
    st.success("## ✨ 2026 ve göreceğimiz tüm yeni yıllar dileğimizce olsun ! ✨")
    st.info("""
    Canım kardeşim benim, bu satırları sana özel bir Python koduyla ve yapay zeka desteğiyle yazmak istedim. 
    Sen benim hayatımdaki en güzel insanlardansın hem de ilk 5. 
    İyi ki doğdun, iyi ki varsın !
    """)
    st.markdown("<h3 class='gold-text'>✨ Bu yıl beraber yapacaklarımız:</h3>", unsafe_allow_html=True)
    st.write("- ☕ Daha çok kahve içeceğiz")
    st.write("- 🌈 Daha güzel zamanlarımız olacak")
    st.write("- 🍀 Daha sağlıklı ve huzurlu günlerimiz olacak")