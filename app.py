import streamlit as st
import time

# 1. Sayfa Ayarları
st.set_page_config(page_title="İyi ki Doğdun Can Dost İyi ki Varsın !", page_icon="✨")

# 2. Mor Arka Plan ve Okunaklı Yazı Stilleri (CSS)
st.markdown("""
    <style>
    /* Arka Plan: Koyu Mordan Açık Mora Geçiş */
    .stApp {
        background: linear-gradient(to bottom, #4b0082, #8a2be2);
    }
    
    /* Genel Yazılar (Beyaz) */
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
    
    /* Resim Tasarımı: Köşeleri yuvarlatılmış ve net görünüm */
    .stImage > img {
        border-radius: 20px;
        border: 2px solid #FFD700;
        display: block;
        margin-left: auto;
        margin-right: auto;
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

    /* LİSTE MADDELERİ: Tam Siyah, Kalın ve Beyaz Kutucuk İçinde */
    .liste-maddesi {
        background-color: rgba(255, 255, 255, 0.85); /* Yazının arkasına beyaz zemin */
        color: #000000 !important; /* Tam Siyah yazı */
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

# 3. İç
