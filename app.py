import streamlit as st

# Məlumat bazası (Buraya oyunları artıracaqsan)
games_db = [
    {
        "title": "A Way Out",
        "serial": "CUSA-07986",
        "size": "16.5 GB",
        "base": "https://archive.org/download/ps4-fpkg-collection-english-a/A_Way_Out.pkg",
        "update": "https://archive.org/download/ps4-fpkg-collection-english-a/A_Way_Out_Update_1.01.pkg",
        "dlc": None
    },
    {
        "title": "Assassin's Creed Odyssey",
        "serial": "CUSA-09311",
        "size": "48.2 GB",
        "base": "https://archive.org/download/ps4-fpkg-collection-english-a/Assassins_Creed_Odyssey.pkg",
        "update": "https://archive.org/download/ps4-fpkg-collection-english-a/Assassins_Creed_Odyssey_Update_1.50.pkg",
        "dlc": "https://archive.org/download/ps4-fpkg-collection-english-a/Assassins_Creed_Odyssey_DLC_Pack.pkg"
    }
]

# Səhifə Ayarları
st.set_page_config(page_title="Odlar Yurdu Store", page_icon="🎮", layout="wide")

# CSS ilə gözəl görünüş
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { width: 100%; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# Başlıq
st.title("🎮 Odlar Yurdu Store")
st.write("---")

# Yan menyu (Sidebar)
st.sidebar.header("🔍 Oyun Axtarışı")
titles = [g["title"] for g in games_db]
selected_title = st.sidebar.selectbox("Oyun seçin:", titles)

# Əsas ekran
game = next((g for g in games_db if g["title"] == selected_title), None)

if game:
    st.header(f"🕹️ {game['title']}")
    
    # Məlumat kartı
    col1, col2 = st.columns([1, 2])
    with col1:
        st.info(f"**Serial:** {game['serial']}")
        st.warning(f"**Ölçü:** {game['size']}")
    
    # Yükləmə Düymələri (Daha professional)
    st.subheader("📥 Yükləmə Linkləri")
    
    b1, b2, b3 = st.columns(3)
    
    with b1:
        st.link_button("💾 Base Game", game['base'], use_container_width=True)
    with b2:
        if game['update']:
            st.link_button("🔄 Update", game['update'], use_container_width=True)
        else:
            st.button("🔄 Update Yoxdur", disabled=True, use_container_width=True)
    with b3:
        if game['dlc']:
            st.link_button("📦 DLC", game['dlc'], use_container_width=True)
        else:
            st.button("📦 DLC Yoxdur", disabled=True, use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.write("Developed by Ümüd © 2026")
