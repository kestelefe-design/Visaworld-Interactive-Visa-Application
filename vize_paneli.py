import streamlit as st
import plotly.express as px
import pandas as pd

# Sayfa Ayarları
st.set_page_config(page_title="VisaWorld - İnteraktif Dünya Vize Başvuru Kılavuzu", layout="wide")

# 🎨 HD PROFESYONEL VE GÜVEN VEREN AKICI TASARIM ŞABLONU (CSS)
st.markdown("""
    <style>
    .stApp { 
        background: linear-gradient(135deg, #0f2b48 0%, #1a365d 40%, #224263 70%, #1d3557 100%);
        background-attachment: fixed;
        color: #ffffff; 
    }
    h1, h2, h3, h4, h5, h6, p, span, label { color: #ffffff !important; }
    .stSelectbox div div { background-color: #1a446c !important; color: white !important; }
    div[data-testid="stMarkdownContainer"] hr { border-color: rgba(255, 255, 255, 0.2) !important; }
    
    /* Üst Alanı Şıklaştıran Premium Banner */
    .premium-banner {
        background: linear-gradient(90deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.1) 50%, rgba(255,255,255,0.05) 100%);
        padding: 14px;
        border-radius: 14px;
        text-align: center;
        font-size: 24px;
        letter-spacing: 12px;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Giriş Kartları İçin Özel Şık CSS */
    .intro-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 12px;
        height: 100%;
    }
    
    /* İletişim Formu Kutusu */
    .form-container {
        background: rgba(255, 255, 255, 0.04);
        padding: 25px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# ✈️ KÜRESEL SEYAHAT İKONLARI BARI
st.markdown('<div class="premium-banner">✈️ 🌍 🧳 🏖️ 🏛️ ☀️ 🌊</div>', unsafe_allow_html=True)

# --- 🌍 SIDEBAR: DİL SEÇİMİ ---
st.sidebar.header("🌍 Dil / Language")
dil = st.sidebar.selectbox("Select Language / Dil Seçin", ["Türkçe", "English"])

# 🛠️ KURŞUN GEÇİRMEZ SATIR TABANLI MASTER VERİ SETİ (ABD ve Portekiz Güncellendi)
veri_havuzu = [
    {"Country_Code": "DEU", "Flag_Code": "de", "Ülke_TR": "Almanya", "Ülke_EN": "Germany", "Yoğunluk_Skor": 5, "lat": 51.1, "lon": 10.4, "zoom_level": 5.5},
    {"Country_Code": "USA", "Flag_Code": "us", "Ülke_TR": "Amerika Birleşik Devletleri (ABD)", "Ülke_EN": "United States (USA)", "Yoğunluk_Skor": 5, "lat": 37.0, "lon": -95.7, "zoom_level": 3.5},
    {"Country_Code": "CAN", "Flag_Code": "ca", "Ülke_TR": "Kanada", "Ülke_EN": "Canada", "Yoğunluk_Skor": 5, "lat": 56.1, "lon": -106.3, "zoom_level": 3.0},
    {"Country_Code": "FRA", "Flag_Code": "fr", "Ülke_TR": "Fransa", "Ülke_EN": "France", "Yoğunluk_Skor": 5, "lat": 46.2, "lon": 2.2, "zoom_level": 5.5},
    {"Country_Code": "BGR", "Flag_Code": "bg", "Ülke_TR": "Bulgaristan", "Ülke_EN": "Bulgaria", "Yoğunluk_Skor": 5, "lat": 42.7, "lon": 25.4, "zoom_level": 6.0},
    {"Country_Code": "GRC", "Flag_Code": "gr", "Ülke_TR": "Yunanistan", "Ülke_EN": "Greece", "Yoğunluk_Skor": 5, "lat": 39.0, "lon": 21.8, "zoom_level": 6.0},
    {"Country_Code": "ITA", "Flag_Code": "it", "Ülke_TR": "İtalya", "Ülke_EN": "Italy", "Yoğunluk_Skor": 5, "lat": 41.8, "lon": 12.5, "zoom_level": 5.5},
    {"Country_Code": "ESP", "Flag_Code": "es", "Ülke_TR": "İspanya", "Ülke_EN": "Spain", "Yoğunluk_Skor": 5, "lat": 40.4, "lon": -3.7, "zoom_level": 5.5},
    {"Country_Code": "NLD", "Flag_Code": "nl", "Ülke_TR": "Hollanda", "Ülke_EN": "Netherlands", "Yoğunluk_Skor": 4, "lat": 52.1, "lon": 5.2, "zoom_level": 6.5},
    {"Country_Code": "BEL", "Flag_Code": "be", "Ülke_TR": "Belçika", "Ülke_EN": "Belgium", "Yoğunluk_Skor": 4, "lat": 50.5, "lon": 4.4, "zoom_level": 6.5},
    {"Country_Code": "PRT", "Flag_Code": "pt", "Ülke_TR": "Portekiz", "Ülke_EN": "Portugal", "Yoğunluk_Skor": 4, "lat": 39.3, "lon": -8.2, "zoom_level": 6.0},
    {"Country_Code": "DNK", "Flag_Code": "dk", "Ülke_TR": "Danimarka", "Ülke_EN": "Denmark", "Yoğunluk_Skor": 4, "lat": 56.2, "lon": 9.5, "zoom_level": 6.0},
    {"Country_Code": "CHE", "Flag_Code": "ch", "Ülke_TR": "İsviçre", "Ülke_EN": "Switzerland", "Yoğunluk_Skor": 3, "lat": 46.8, "lon": 8.2, "zoom_level": 6.0},
    {"Country_Code": "AUT", "Flag_Code": "at", "Ülke_TR": "Avusturya", "Ülke_EN": "Austria", "Yoğunluk_Skor": 3, "lat": 47.5, "lon": 14.5, "zoom_level": 6.0},
    {"Country_Code": "HUN", "Flag_Code": "hu", "Ülke_TR": "Macaristan", "Ülke_EN": "Hungary", "Yoğunluk_Skor": 3, "lat": 47.1, "lon": 19.5, "zoom_level": 6.0},
    {"Country_Code": "ROU", "Flag_Code": "ro", "Ülke_TR": "Romanya", "Ülke_EN": "Romania", "Yoğunluk_Skor": 3, "lat": 45.9, "lon": 24.9, "zoom_level": 6.0},
    {"Country_Code": "AUS", "Flag_Code": "au", "Ülke_TR": "Avustralya (AUS)", "Ülke_EN": "Australia (AUS)", "Yoğunluk_Skor": 3, "lat": -25.2, "lon": 133.7, "zoom_level": 3.0},
    {"Country_Code": "NZL", "Flag_Code": "nz", "Ülke_TR": "Yeni Zelanda", "Ülke_EN": "New Zealand", "Yoğunluk_Skor": 3, "lat": -40.9, "lon": 174.8, "zoom_level": 4.0},
    {"Country_Code": "DZA", "Flag_Code": "dz", "Ülke_TR": "Cezayir", "Ülke_EN": "Algeria", "Yoğunluk_Skor": 3, "lat": 28.0, "lon": 1.6, "zoom_level": 4.5},
    {"Country_Code": "POL", "Flag_Code": "pl", "Ülke_TR": "Polonya", "Ülke_EN": "Poland", "Yoğunluk_Skor": 2, "lat": 51.9, "lon": 19.1, "zoom_level": 5.5},
    {"Country_Code": "CZE", "Flag_Code": "cz", "Ülke_TR": "Çek Cumhuriyeti (Çekya)", "Ülke_EN": "Czech Republic", "Yoğunluk_Skor": 2, "lat": 49.8, "lon": 15.4, "zoom_level": 6.0},
    {"Country_Code": "HRV", "Flag_Code": "hr", "Ülke_TR": "Hırvatistan", "Ülke_EN": "Croatia", "Yoğunluk_Skor": 2, "lat": 45.1, "lon": 15.2, "zoom_level": 6.0},
    {"Country_Code": "LTU", "Flag_Code": "lt", "Ülke_TR": "Litvanya", "Ülke_EN": "Lithuania", "Yoğunluk_Skor": 2, "lat": 55.1, "lon": 23.8, "zoom_level": 6.0},
    {"Country_Code": "LVA", "Flag_Code": "lv", "Ülke_TR": "Letonya", "Ülke_EN": "Latvia", "Yoğunluk_Skor": 2, "lat": 56.8, "lon": 24.6, "zoom_level": 6.0},
    {"Country_Code": "IRL", "Flag_Code": "ie", "Ülke_TR": "İrlanda", "Ülke_EN": "Ireland", "Yoğunluk_Skor": 2, "lat": 53.4, "lon": -8.2, "zoom_level": 6.0},
    {"Country_Code": "SVN", "Flag_Code": "si", "Ülke_TR": "Slovenya", "Ülke_EN": "Slovenia", "Yoğunluk_Skor": 2, "lat": 46.1, "lon": 14.9, "zoom_level": 6.0},
    {"Country_Code": "CHN", "Flag_Code": "cn", "Ülke_TR": "Çin", "Ülke_EN": "China", "Yoğunluk_Skor": 2, "lat": 35.8, "lon": 104.1, "zoom_level": 3.5},
    {"Country_Code": "GBR", "Flag_Code": "gb", "Ülke_TR": "İngiltere (UK)", "Ülke_EN": "United Kingdom (UK)", "Yoğunluk_Skor": 1, "lat": 55.3, "lon": -3.4, "zoom_level": 5.5},
    {"Country_Code": "SWE", "Flag_Code": "se", "Ülke_TR": "İsveç", "Ülke_EN": "Sweden", "Yoğunluk_Skor": 1, "lat": 60.1, "lon": 18.6, "zoom_level": 4.5},
    {"Country_Code": "NOR", "Flag_Code": "no", "Ülke_TR": "Norveç", "Ülke_EN": "Norway", "Yoğunluk_Skor": 1, "lat": 60.4, "lon": 8.4, "zoom_level": 4.5},
    {"Country_Code": "FIN", "Flag_Code": "fi", "Ülke_TR": "Finlandiya", "Ülke_EN": "Finland", "Yoğunluk_Skor": 1, "lat": 61.9, "lon": 25.7, "zoom_level": 4.5},
    {"Country_Code": "EST", "Flag_Code": "ee", "Ülke_TR": "Estonya", "Ülke_EN": "Estonia", "Yoğunluk_Skor": 1, "lat": 58.5, "lon": 25.0, "zoom_level": 6.0},
    {"Country_Code": "SVK", "Flag_Code": "sk", "Ülke_TR": "Slovakya", "Ülke_EN": "Slovakia", "Yoğunluk_Skor": 1, "lat": 48.6, "lon": 19.6, "zoom_level": 6.0},
    {"Country_Code": "RUS", "Flag_Code": "ru", "Ülke_TR": "Rusya", "Ülke_EN": "Russia", "Yoğunluk_Skor": 1, "lat": 61.5, "lon": 105.3, "zoom_level": 2.5},
    {"Country_Code": "VNM", "Flag_Code": "vn", "Ülke_TR": "Vietnam", "Ülke_EN": "Vietnam", "Yoğunluk_Skor": 1, "lat": 14.0, "lon": 108.2, "zoom_level": 4.5},
    {"Country_Code": "MLT", "Flag_Code": "mt", "Ülke_TR": "Malta", "Ülke_EN": "Malta", "Yoğunluk_Skor": 1, "lat": 35.9, "lon": 14.4, "zoom_level": 8.0},
    {"Country_Code": "ISL", "Flag_Code": "is", "Ülke_TR": "İzlanda", "Ülke_EN": "Iceland", "Yoğunluk_Skor": 1, "lat": 64.9, "lon": -19.0, "zoom_level": 5.0}
]

df = pd.DataFrame(veri_havuzu)
df["Ülke"] = df["Ülke_TR"] if dil == "Türkçe" else df["Ülke_EN"]
df = df.sort_values(by="Ülke").reset_index(drop=True)

# ÇİFT YÖNLÜ SENKRONİZASYON ALTYAPISI
if "secili_ulke_state" not in st.session_state:
    st.session_state.secili_ulke_state = "Almanya" if dil == "Türkçe" else "Germany"

opsiyonlar = df["Ülke"].tolist()

st.sidebar.markdown("---")
st.sidebar.header("🔍 " + ("Ülke Seçimi" if dil == "Türkçe" else "Country Selection"))
if st.session_state.secili_ulke_state not in opsiyonlar:
    st.session_state.secili_ulke_state = opsiyonlar[0]
varsayilan_idx = opsiyonlar.index(st.session_state.secili_ulke_state)

secilen_ulke = st.sidebar.selectbox(
    "Select Destination:" if dil == "English" else "Gideceğiniz Ülkeyi Seçin:", 
    options=opsiyonlar,
    index=varsayilan_idx
)

if secilen_ulke != st.session_state.secili_ulke_state:
    st.session_state.secili_ulke_state = secilen_ulke
    st.rerun()

# --- DİL PORTALI SÖZLÜK YAPISI ---
if dil == "Türkçe":
    title_text = "🗺️ VisaWorld - İnteraktif Dünya Vize Başvuru Kılavuzu"
    intro_title = "### 🌍 Dünyanın Güzelliklerine Açılan Kapıda, Yol Arkadaşınızız"
    intro_desc = """Vize hazırlıkları ilk bakışta yoğun evrak listeleri, formlar ya da sabır gerektiren randevu süreçleriyle dolu bir yolculuk gibi görünebilir. Ancak biz **VisaWorld** olarak, bu tatlı telaşın aslında hayallerinizdeki seyahatin ilk heyecanlı adımı olduğuna inanıyoruz. Randevu bulmak şu an küresel bazda çok kolay olmasa da, doğru strateji ve planlamayla tüm bu adımları seyahatinizin keyifli bir parçası haline getiriyor, süreci sizin için olabildiğince pürüzsüz ve stressiz bir şekilde ilerletmeye çalışıyoruz.

Çünkü bizim için her pasaport yeni bir başlangıç, dünyanın bambaşka bir güzelliğine açılan birer penceredir. Rotaların konsolosluk dinamikleri ne kadar farklı görünürse görünsün, yolculuğun sonunda o arzuladığınız seyahatin harika bir şekilde gerçekleşebileceğine odaklanıyoruz. Aşağıdaki interaktif kılavuzumuz yardımıyla, gitmek istediğiniz destinasyonun en güncel başvuru mekanizmasını ve resmi koordinasyon şubelerini inceleyebilirsiniz."""
    card1 = "🏛️ <b>Schengen Rotaları</b><br><small><b>Fransa</b>’nın romantik esintisi Paris, <b>Almanya</b>’nın köklü tarihi, <b>Hollanda</b>’nın renkli sokakları Amsterdam, <b>Yunanistan, İtalya ve İspanya</b>’nın yoğun Akdeniz kıyıları ve Roma sokakları.</small>"
    card2 = "🗽 <b>Amerika Birleşik Devletleri</b><br><small><b>ABD (B1/B2) Standart</b> vize yapısıyla, New York’un bitmeyen enerjisi, Los Angeles’ın ikonik sahilleri ve San Francisco’nun büyüleyici köprülerine uzanan unutulmaz yolculuklar.</small>"
    card3 = "🏰 <b>Birleşik Krallık & İrlanda</b><br><small><b>İngiltere (UK Visitor Standart)</b> ile Londra ve Edinburgh’un tarihi dokusu, <b>İrlanda</b> ile Dublin’in kendine has muazzam kültürü.</small>"
    card4 = "🌊 <b>Denizaşırı Küresel Güzellikler</b><br><small><b>Kanada (Temporary Visitor Standart)</b>’nın doğa mucizeleri, <b>Rusya</b>’nın geniş coğrafyası, <b>Avustralya</b>’nın Sidney esintileri, <b>Çin ve Vietnam</b>’ın egzotik mistik atmosferi.</small>"
    form_title = "📩 VisaWorld Hızlı Danışma Portalı"
    form_desc = "Aklınıza takılan vize sorusunu doğrudan uzmanlarımıza iletin, yanıtı anında e-posta adresinize gelsin."
    lbl_name, lbl_mail, lbl_msg = "Adınız Soyadınız:", "E-Posta Adresiniz:", "Sorunuz veya İncelediğiniz Ülke:"
    btn_text = "📩 Bilgilerimi İlet ve Süreci Başlat"
    map_tab = "🗺️ Ülke Yoğunluk Haritası"
    err_not = "⚠️ ÖNEMLİ NOT: Vize süreçleri başvuru kategorilerine göre ve şehirlere (bölgesel yetki alanlarına) göre farklılık göstermektedir."
    h_title = "⚡ Genel Randevu ve Onay Hızı Hiyerarşisi (Hızlıdan Yavaşa)"
    h_items = ["AB Aile Üyesi", "Kültürel", "Ticari", "Aile/Arkadaş Ziyareti", "Turistik"]
    lbl_b_düzeni, lbl_coord = "### 🏢 Başvuru Düzeni", "🏢 **Koordinasyon Şubeleri Bilgisi:**"
    blog_title = "💼 VisaWorld - Profesyonel Süreç Yönetimi"
    blog_desc = "Dünya genelindeki vize kurallarını sizin adınıza eksiksiz yönetiyoruz."
    b1_t, b1_d = "📊 Global Profil Analizi", "Onay şansınızı en üst seviyeye çıkaracak başvuru stratejisini uzman kadromuzla belirliyoruz."
    b2_t, b2_d = "🛡️ Tam Uyumlu Sağlık Sigortası", "Konsolosluk mevzuatına ve vize kurallarına tam uyumlu seyahat sağlık poliçenizi hazırlıyoruz."
    b3_t, b3_d = "🏨 Kurumsal Rezervasyonlar", "Sistemlerde sorgulanabilir, vize onayına destek sağlayacak uçak ve otel rezervasyonlarınızı organize ediyoruz."
else:
    title_text = "🗺️ VisaWorld - Interactive Global Visa Application Guide"
    intro_title = "### 🌍 Your Companion at the Gateway to the World's Wonders"
    intro_desc = """Visa preparations may initially seem like a journey full of dense document lists, forms, or appointment processes requiring patience. However, at **VisaWorld**, we believe that this sweet rush is actually the first exciting step of your dream trip. Although finding an appointment is not very easy on a global scale right now, with the right strategy and planning, we make all these steps an enjoyable part of your journey and try to advance the process as smoothly and stress-free as possible.

Because for us, every passport is a new beginning, a window opening to a completely different beauty of the world. No matter how different the consular dynamics of the routes appear, we focus on the fact that your desired travel can happen beautifully at the end of the journey. With the help of our interactive guide below, you can examine the most up-to-date application mechanism and official coordination branches of your destination."""
    card1 = "🏛️ <b>Schengen Routes</b><br><small>Romantic Paris in <b>France</b>, deep history of <b>Germany</b>, colorful Amsterdam in <b>Netherlands</b>, beautiful coastlines of <b>Greece, Italy, and Spain</b>.</small>"
    card2 = "🗽 <b>United States</b><br><small>With <b>USA (B1/B2) Standard</b> visa structure, the endless energy of New York, iconic beaches of Los Angeles, and breathtaking bridges of San Francisco.</small>"
    card3 = "🏰 <b>United Kingdom & Ireland</b><br><small>Historical textures of London and Edinburgh with <b>UK Visitor Standard</b>, and the unique magnificent culture of Dublin in <b>Ireland</b>.</small>"
    card4 = "🌊 <b>Overseas Global Wonders</b><br><small>Natural miracles of <b>Canada (Temporary Visitor Standard)</b>, vast geography of <b>Russia</b>, Sydney vibes of <b>Australia, China, and Vietnam</b>.</small>"
    form_title = "📩 VisaWorld Quick Inquiry Portal"
    form_desc = "Send your visa questions directly to our experts, and receive the answer instantly in your e-mail inbox."
    lbl_name, lbl_mail, lbl_msg = "Your Full Name:", "Your E-Mail Address:", "Your Question or Selected Country:"
    btn_text = "📩 Submit My Info & Start the Process"
    map_tab = "🗺️ Country Density Map"
    err_not = "⚠️ IMPORTANT NOTE: Visa processes vary according to application categories and cities (regional jurisdictions)."
    h_title = "⚡ General Appointment & Approval Speed Hierarchy (Fastest to Slowest)"
    h_items = ["EU Family Member", "Cultural", "Business", "Family/Friend Visit", "Tourist"]
    lbl_b_düzeni, lbl_coord = "### 🏢 Application Structure", "🏢 **Coordination Branches Info:**"
    blog_title = "💼 VisaWorld - Professional Process Management"
    blog_desc = "We fully manage global visa procedures on your behalf with zero errors."
    b1_t, b1_d = "📊 Profile Analysis", "We determine the application strategy that will maximize your approval chances with our expert team."
    b2_t, b2_d = "🛡️ Compliant Insurance", "We prepare your travel health insurance policy fully compliant with consular regulations."
    b3_t, b3_d = "🏨 Flight & Hotel Bookings", "We organize verifiable flight and hotel reservations that support your visa application."

# --- 🚀 ADIM 1: SAYFA ANABAŞLIĞI VE GİRİŞ METNİ ---
st.title(title_text)
st.markdown(intro_title)
st.write(intro_desc)
st.write("##")

kolon_img1, kolon_img2, kolon_img3, kolon_img4 = st.columns(4)
with kolon_img1: st.markdown(f'<div class="intro-card">{card1}</div>', unsafe_allow_html=True)
with kolon_img2: st.markdown(f'<div class="intro-card">{card2}</div>', unsafe_allow_html=True)
with kolon_img3: st.markdown(f'<div class="intro-card">{card3}</div>', unsafe_allow_html=True)
with kolon_img4: st.markdown(f'<div class="intro-card">{card4}</div>', unsafe_allow_html=True)

# --- 🎯 ADIM 2: İNTERAKTİF HARİTA PANELİ (ÜSTTE) ---
st.write("##"); st.markdown("---")
fig = px.choropleth(
    df, locations="Country_Code", color="Yoğunluk_Skor", hover_name="Ülke", custom_data=["Ülke"],
    color_continuous_scale=[[0.0, "#27ae60"], [0.25, "#2ecc71"], [0.5, "#f1c40f"], [0.75, "#e67e22"], [1.0, "#e74c3c"]]
)
aktif_satir = df[df["Ülke"] == st.session_state.secili_ulke_state].iloc[0]
fig.update_layout(
    geo=dict(showframe=False, showcoastlines=True, coastlinecolor="rgba(255,255,255,0.4)", projection_type='natural earth',
             showocean=True, oceancolor="#2b7bba", showland=True, landcolor="#f4f6f9",
             center=dict(lat=aktif_satir["lat"], lon=aktif_satir["lon"]), projection_scale=aktif_satir["zoom_level"]),
    coloraxis_showscale=False, margin=dict(l=0, r=0, t=10, b=10), height=550, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'
)

harita_kolon, detay_kolon = st.columns([1.4, 1.6])
with harita_kolon:
    st.subheader(map_tab)
    harita_secimi = st.plotly_chart(fig, use_container_width=True, on_select="rerun")
    if harita_secimi and "selection" in harita_secimi and harita_secimi["selection"]["points"]:
        tiklanan_ulke = harita_secimi["selection"]["points"][0]["customdata"][0]
        if tiklanan_ulke != st.session_state.secili_ulke_state:
            st.session_state.secili_ulke_state = tiklanan_ulke
            st.rerun()

with detay_kolon:
    secilen_ulke_guncel = st.session_state.secili_ulke_state
    aktif_satir_guncel = df[df["Ülke"] == secilen_ulke_guncel].iloc[0]
    
    sol_b, sag_b = st.columns([1, 4])
    with sol_b: st.image(f"https://flagcdn.com/w80/{aktif_satir_guncel['Flag_Code']}.png", width=70)
    with sag_b: st.subheader(f"{aktif_satir_guncel['Ülke']} " + ("Başvuru Kılavuzu" if dil == "Türkçe" else "Application Guide"))
        
    st.error(err_not)
    
    # Hiyerarşi Paneli
    st.markdown(f"""
    <div style="background-color: #112d4e; padding: 15px; border-radius: 8px; border-left: 5px solid #f1c40f; margin-bottom: 15px;">
        <h4 style='margin-top:0; color:#f1c40f !important;'>{h_title}</h4>
        <ol style='margin-bottom:0;'>
            <li><b>{h_items[0]}</b></li>
            <li><b>{h_items[1]}</b></li>
            <li><b>{h_items[2]}</b></li>
            <li><b>{h_items[3]}</b></li>
            <li><b>{h_items[4]}</b></li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    u_tr = aktif_satir_guncel['Ülke_TR']
    if u_tr == "Vietnam":
        st.success("💻 ONLINE BAŞVURU" if dil=="Türkçe" else "💻 ONLINE APPLICATION")
    elif u_tr == "Rusya":
        st.info("ℹ️ KONSOLOSLUK & E-VİZE" if dil=="Türkçe" else "ℹ️ CONSULATE & E-VISA")
    elif u_tr in ["Almanya", "İtalya", "Hollanda", "Bulgaristan", "Fransa", "Yunanistan", "İspanya", "Portekiz"]:
        st.warning("🔒 BÖLGESEL YETKİ ALANI" if dil=="Türkçe" else "🔒 REGIONAL JURISDICTION")

    st.markdown(lbl_b_düzeni)
    
    if dil == "Türkçe":
        basvuru_sekli = "📅 Yetkili Merkez Randevusu (VFS Global)"
        if u_tr in ["Almanya", "İtalya"]: basvuru_sekli = "📅 Doğrudan Randevu (iDATA)"
        elif u_tr == "Yunanistan": basvuru_sekli = "📅 Doğrudan Randevu (Kosmos Vize)"
        elif u_tr in ["Romanya", "Rusya", "Vietnam", "Çin", "Dubai (BAE)", "Cezayir"]: basvuru_sekli = "🏛️ Doğrudan Başvuru (Kendi Konsolosluğu)"
        elif u_tr == "İspanya": basvuru_sekli = "📅 Doğrudan Randevu (BLS International)"
        elif u_tr in ["Slovenya", "Macaristan", "Portekiz"]: basvuru_sekli = "📅 Doğrudan Randevu (As Visa Solution)"
        elif u_tr in ["Avustralya (AUS)", "Yeni Zelanda", "Kanada"]: basvuru_sekli = "💻 Dijital Başvuru ve Sonrasında VFS Global (Biyometrik Süreç)"
        elif u_tr == "İngiltere (UK)": basvuru_sekli = "📅 Yetkili Merkez Randevusu (VFS Global)"
        elif u_tr == "Amerika Birleşik Devletleri (ABD)": basvuru_sekli = "📅 Resmi Konsolosluk Randevusu (B1/B2 Standart)"
    else:
        basvuru_sekli = "📅 Authorized Center Appointment (VFS Global)"
        if u_tr in ["Almanya", "İtalya"]: basvuru_sekli = "📅 Direct Appointment (iDATA)"
        elif u_tr == "Yunanistan": basvuru_sekli = "📅 Direct Appointment (Kosmos Visa)"
        elif u_tr in ["Romanya", "Rusya", "Vietnam", "Çin", "Dubai (BAE)", "Cezayir"]: basvuru_sekli = "🏛️ Direct Application (Consulate)"
        elif u_tr == "İspanya": basvuru_sekli = "📅 Direct Appointment (BLS International)"
        elif u_tr in ["Slovenya", "Macaristan", "Portekiz"]: basvuru_sekli = "📅 Direct Appointment (As Visa Solution)"
        elif u_tr in ["Avustralya (AUS)", "Yeni Zelanda", "Kanada"]: basvuru_sekli = "💻 Digital Application & VFS Global Biometric Process"
        elif u_tr == "United Kingdom (UK)": basvuru_sekli = "📅 Authorized Center Appointment (VFS Global)"
        elif u_tr == "Amerika Birleşik Devletleri (ABD)": basvuru_sekli = "📅 Official Consulate Appointment (B1/B2 Standard)"
        
    st.write(f"🔹 {basvuru_sekli}")
    st.markdown(lbl_coord)
    
    if u_tr in ["Almanya", "İtalya"]:
        st.write("📍 iDATA: İstanbul, Ankara, İzmir, Bursa, Antalya, Gaziantep, Adana")
    elif u_tr == "Yunanistan":
        st.write("📍 Kosmos Vize / Kosmos Visa")
    elif u_tr == "İspanya":
        st.write("📍 BLS International")
    elif u_tr in ["Slovenya", "Macaristan", "Portekiz"]:
        st.write("📍 As Visa Solution")
    elif u_tr in ["Romanya", "Rusya", "Vietnam", "Çin", "Dubai (BAE)", "Cezayir"]:
        st.write("📍 " + ("Kendi Konsolosluğu" if dil=="Türkçe" else "Direct Consulate / No Third Party"))
    elif u_tr == "Amerika Birleşik Devletleri (ABD)":
        st.write("📍 " + ("Resmi Konsolosluk" if dil=="Türkçe" else "Official US Consulate"))
    else:
        st.write("📍 VFS Global")
        
    st.write("---")
    
    # İletişim Butonları
    wp_txt = f"Merhaba,%20VisaWorld%20üzerinden%20{secilen_ulke_guncel}%20vize%20durumuna%20baktım." if dil=="Türkçe" else f"Hello,%20I%20checked%20{secilen_ulke_guncel}%20visa%20status%20on%20VisaWorld."
    st.link_button("🟢 WhatsApp" if dil=="Türkçe" else "🟢 WhatsApp Chat", f"https://wa.me/905432664040?text={wp_txt}")
    st.link_button("🔵 Telegram" if dil=="Türkçe" else "🔵 Telegram Chat", f"https://t.me/nonglutenn")

# --- 📩 ADIM 3: MAİLİNE OTOMATİK DÜŞEN İLETİŞİM FORMU PANELİ ---
st.write("##"); st.markdown("---")
st.header(form_title)
st.write(form_desc)

KENDI_MAILIN = "infvisaworld@gmail.com"
with st.container():
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    form_html = f"""
    <form action="https://formsubmit.co/{KENDI_MAILIN}" method="POST" target="_blank">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_template" value="table">
        <div style="margin-bottom: 12px;">
            <label style="display:block; margin-bottom:5px; font-weight:bold;">{lbl_name}</label>
            <input type="text" name="name" style="width:100%; padding:10px; border-radius:6px; border:1px solid rgba(255,255,255,0.2); background:#1a446c; color:white;" required>
        </div>
        <div style="margin-bottom: 12px;">
            <label style="display:block; margin-bottom:5px; font-weight:bold;">{lbl_mail}</label>
            <input type="email" name="email" style="width:100%; padding:10px; border-radius:6px; border:1px solid rgba(255,255,255,0.2); background:#1a446c; color:white;" required>
        </div>
        <div style="margin-bottom: 12px;">
            <label style="display:block; margin-bottom:5px; font-weight:bold;">{lbl_msg}</label>
            <textarea name="message" rows="4" style="width:100%; padding:10px; border-radius:6px; border:1px solid rgba(255,255,255,0.2); background:#1a446c; color:white;" required></textarea>
        </div>
        <button type="submit" style="background:#27ae60; color:white; border:none; padding:12px 24px; border-radius:6px; font-weight:bold; cursor:pointer; width:100%;">{btn_text}</button>
    </form>
    """
    st.markdown(form_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 💼 ADIM 4: KURUMSAL BLOG PANELİ ---
st.write("##"); st.markdown("---")
st.header(blog_title)
st.write(blog_desc)

hizmet_kolon1, hizmet_kolon2, hizmet_kolon3 = st.columns(3)
with hizmet_kolon1:
    st.subheader(b1_t)
    st.write(b1_d)
with hizmet_kolon2:
    st.subheader(b2_t)
    st.write(b2_d)
with hizmet_kolon3:
    st.subheader(b3_t)
    st.write(b3_d)
