import streamlit as st
import time

# 1. Sayfa Ayarları
st.set_page_config(page_title="İyi ki Doğdun Can Dost İyi ki Varsın !", page_icon="✨")

# 2. Tasarım ve Netlik Ayarları (CSS)
st.markdown("""
    <style>
    /* Arka Plan: Mor Geçişli */
    .stApp {
        background: linear-gradient(to bottom, #4b0082, #8a2be2);
    }
    
    /* Genel Yazılar */
    h1, h3, [data-testid="stMarkdownContainer"] p {
        text-align: center;
        color: #FFFFFF !important;
    }
    
    /* Altın Sarısı Başlıklar */
    .gold-text {
        color: #FFD700 !important;
        text-align: center;
        font-weight: bold;
    }
    
    /* Resim Tasarımı: En yüksek netlik ayarları eklendi */
    .stImage > img {
        border-radius: 20px;
        border: 2px solid #FFD700;
        display: block;
        margin-left: auto;
        margin-right: auto;
        /* Resim netleştirme komutları */
        image-rendering: -webkit-optimize-contrast;
        image-rendering: crisp-edges;
    }

    /* BUTON TASARIMI */
    div.stButton > button {
        display: block;
        margin: 0 auto;
        background-color: #FF4B4B;
        color: white;
        border-radius: 30px;
        padding: 10px 25px;
        border: none;
        font-size: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    }

    /* LİSTE MADDELERİ: Tam Siyah ve Belirgin */
    .liste-maddesi {
        background-color: rgba(255, 255, 255, 0.85);
        color: #000000 !important;
        padding: 12px;
        border-radius: 15px;
        margin: 10px auto;
        width: 85%;
        font-weight: bold;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Ana İçerik
st.markdown("<h1 class='gold-text'>🎂 İyi ki Doğdun Canım Benim! 🎂</h1>", unsafe_allow_html=True)

# GITHUB'A YÜKLEDİĞİN FOTOĞRAF (Dosya adın foto.jpeg olduğu için bu şekilde çektik)
try:
    st.image("foto.jpeg", caption="İyi ki varsın! ✨", use_container_width=True)
except:
    st.error("Fotoğraf bulunamadı! Lütfen GitHub'a 'foto.jpeg' adıyla bir resim yüklediğinden emin ol.")

st.markdown("### BUGÜN 29 ARALIK EN DEĞERLİ GÜNLERİMİZDEN ÇÜNKÜ SEN DOĞDUN, İYİ Kİ SENİ TANIMIŞIM.")

st.markdown("---")

# 4. Buton ve Kutlama
if st.button('Doğum Günü Kızı Buraya Tıkla 🎁'):
    st.balloons()
    st.snow()
    
    with st.spinner('HAYATININ GERİ KALANINDA SAĞLIKLI VE HUZURLU GEÇİRMEN DİLEĞİYLE'):
        time.sleep(9)
    
    st.success("## ✨ 2026 VE GÖRECEĞİMİZ YENİ YILLAR DİLEDİĞİMİZ ŞEKİLDE OLSUN! ✨")
    
    st.info("""
    Canım kardeşim benim, bu satırları sana özel Python koduyla ve yapay zeka desteğiyle yazmak istedim. 
    Sen benim hayatımdaki en ÖZEL insanlardansın. 
    İYİ Kİ DOĞDUN, İYİ Kİ VARSIN!
    """)
    
    st.markdown("<h3 class='gold-text'>✨ Bu yıl beraber yapacaklarımız:</h3>", unsafe_allow_html=True)
    
    st.markdown("<div class='liste-maddesi'>☕ Daha çok kahve içeceğiz</div>", unsafe_allow_html=True)
    st.markdown("<div class='liste-maddesi'>🌈 Daha güzel zamanlarımız olacak</div>", unsafe_allow_html=True)
    st.markdown("<div class='liste-maddesi'>🍀 Daha sağlıklı ve huzurlu günlerimiz olacak</div>", unsafe_allow_html=True)
    st.markdown("<div class='liste-maddesi'>😁 Daha çok güleceğiz.</div>", unsafe_allow_html=True)
