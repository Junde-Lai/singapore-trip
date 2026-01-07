import streamlit as st
import pandas as pd
import pydeck as pdk

# --- 1. 設定頁面資訊 ---
st.set_page_config(
    page_title="新加坡 5D4N 極致深度之旅",
    page_icon="🇸🇬",
    layout="wide"
)

# --- 2. 樣式設定 (CSS 美化) ---
st.markdown("""
<style>
    /* 全局字體優化 */
    .stApp {
        font-family: "Microsoft JhengHei", "PingFang TC", sans-serif;
    }
    
    /* 隱藏預設的主標題邊距 */
    .main .block-container {
        padding-top: 2rem;
    }

    /* 自定義 Hero Banner */
    .hero-container {
        position: relative;
        background-color: #2b3e50; 
        background-image: url('https://preparetravelplans.com/wp-content/uploads/2020/09/Things-to-Do-in-Singapore-at-Night.jpg');
        background-size: cover;
        background-position: center;
        border-radius: 15px;
        padding: 60px 20px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .hero-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.6); 
        border-radius: 15px;
    }
    
    .hero-title {
        position: relative; 
        color: #ffffff;
        font-size: 42px;
        font-weight: 800;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.9); 
        margin: 0;
        letter-spacing: 2px;
    }
    
    .hero-subtitle {
        position: relative;
        color: #f0f0f0;
        font-size: 20px;
        font-weight: 500;
        margin-top: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.9);
    }

    .day-header {
        font-size: 24px;
        font-weight: bold;
        color: #E74C3C;
        border-bottom: 2px solid #E74C3C;
        padding-bottom: 10px;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .spot-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 10px;
        border-left: 5px solid #3498DB;
        transition: transform 0.2s;
    }
    .spot-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.1);
    }
    .spot-title {
        font-size: 20px;
        font-weight: bold;
        color: #2980B9;
        margin-bottom: 10px;
    }
    .spot-desc {
        font-size: 16px;
        line-height: 1.6;
        color: #555;
        text-align: justify;
    }
    .food-badge {
        display: inline-block;
        background-color: #F1C40F;
        color: #34495E;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 14px;
        margin-right: 5px;
        margin-top: 10px;
    }
    .info-box {
        background-color: #ECF0F1;
        padding: 10px;
        border-radius: 8px;
        font-size: 14px;
        color: #7F8C8D;
        margin-top: 10px;
        border-left: 3px solid #BDC3C7;
    }
    .streamlit-expanderHeader {
        font-weight: bold;
        color: #555;
        background-color: #f9f9f9;
        border-radius: 10px;
    }
    
    .main-header {
        font-size: 32px; 
        font-weight: 800; 
        color: #2C3E50;
        text-align: center;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. 側邊欄：基本資訊 ---
with st.sidebar:
    st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e88c7f58-2159-4a3c-8ee4-3919ed7f8a19/dg02zac-b7472d06-5c0c-492a-bd57-69dbaf190b2a.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiIvZi9lODhjN2Y1OC0yMTU5LTRhM2MtOGVlNC0zOTE5ZWQ3ZjhhMTkvZGcwMnphYy1iNzQ3MmQwNi01YzBjLTQ5MmEtYmQ1Ny02OWRiYWYxOTBiMmEucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.QUm9G1x_098zqjyi7JyFjX5sHffD7zF8ejCrDyXu5fU", width=120)
    st.title("🇸🇬 新加坡深度遊")
    st.markdown("---")
    st.markdown("**📅 日期**：2026/1/16 (五) - 1/20 (二)")
    st.markdown("**👥 旅客**：您與媽媽")
    
    st.info("""
    **🏨 住宿資訊**
    
    **JEN Singapore Tanglin**
    (by Shangri-La)
    
    📍 1A Cuscaden Road
    🚇 近 Orchard Boulevard (TE13)
    ✨ 特色：直通 Tanglin Mall，泳池美，交通方便。
    """)
    
    st.warning("""
    **✈️ 航班資訊 (中華航空)**
    
    🛫 **去程 CI751**
    1/16 08:20 台北 (TPE)
    1/16 13:05 新加坡 (SIN)
    
    🛬 **回程 CI752**
    1/20 14:25 新加坡 (SIN)
    1/20 19:05 台北 (TPE)
    """)

    st.markdown("---")
    page = st.radio("前往頁面", ["📅 行程總覽", "🗺️ 地圖導航", "💰 預算估算", "✅ 出國當天備忘錄 (詳細版)", "🌟 其他熱門推薦", "🍷 飯店周邊夜生活", "🛍️ 必買伴手禮清單"])

    st.markdown("---")
    st.markdown("### 💡 補充資源")
    st.link_button("🎫 KKday 新加坡門票價格", "https://www.kkday.com/zh-tw/product/productlist/%E6%96%B0%E5%8A%A0%E5%9D%A1")

# --- 4. 輔助功能：產生景點卡片 ---
def render_spot_card(time, title, desc, food=None, tips=None, details=None):
    food_html = ""
    if food:
        for f in food:
            food_html += f'<span class="food-badge">🍽️ {f}</span>'
            
    tips_html = ""
    if tips:
        tips_html = f'<div class="info-box">💡 <strong>小貼士：</strong>{tips}</div>'

    st.markdown(f"""
    <div class="spot-card">
        <div class="spot-title">{time} ｜ {title}</div>
        <div class="spot-desc">{desc}</div>
        <div style="margin-top:15px;">{food_html}</div>
        {tips_html}
    </div>
    """, unsafe_allow_html=True)
    
    if details:
        with st.expander(f"🔍 點擊查看：{title} 交通與詳細攻略"):
            st.info(details)
    
    st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)

# --- 5. 地標數據 ---
locations = pd.DataFrame({
    'name': ['JEN Tanglin', '樟宜機場', '中峇魯', '福康寧公園', '克拉碼頭', '小印度', '甘幫格南', '牛車水', '植物園', '濱海灣金沙', '濱海灣花園', '聖淘沙', '如切/加東', '讚美廣場', '舊禧街警察局', 'Manhattan Bar', 'Dempsey Hill', 'Light to Night'],
    'lat': [1.3056, 1.3644, 1.2865, 1.2925, 1.2905, 1.3068, 1.3023, 1.2839, 1.3138, 1.2834, 1.2815, 1.2494, 1.3130, 1.2952, 1.2907, 1.3039, 1.3036, 1.2895],
    'lon': [103.8237, 103.9915, 103.8270, 103.8465, 103.8463, 103.8516, 103.8596, 103.8436, 103.8159, 103.8607, 103.8636, 103.8303, 103.9045, 103.8520, 103.8484, 103.8256, 103.8087, 103.8510],
    'type': ['Hotel', 'Airport', 'Spot', 'Spot', 'Spot', 'Spot', 'Spot', 'Spot', 'Spot', 'Landmark', 'Landmark', 'Island', 'Recommend', 'Recommend', 'Recommend', 'Bar', 'Bar', 'Event']
})

# --- 6. 主頁面邏輯 ---

if page == "📅 行程總覽":
    st.markdown("""
    <div class="hero-container">
        <div class="hero-overlay"></div>
        <h1 class="hero-title">✨ 新加坡五天四夜：極致深度探索</h1>
        <p class="hero-subtitle">經典地標 ✕ 多元文化 ✕ 在地美食 ✕ 濱海灣夜色</p>
    </div>
    """, unsafe_allow_html=True)
    
    day_tab1, day_tab2, day_tab3, day_tab4, day_tab5 = st.tabs(["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"])

    with day_tab1:
        st.markdown('<div class="day-header">1/16 (五) 抵達、文創區與河畔夜景</div>', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        with col1:
             st.metric("抵達時間", "13:05", "T3 航廈")
        with col2:
            st.info("👋 歡迎！請先辦理入境並入住 **JEN Tanglin 飯店**。")

        render_spot_card(
            "15:30 - 17:00", "中峇魯 (Tiong Bahru)",
            "漫步在 1930 年代的「裝飾藝術風格」老組屋之間，尋找葉耀宗繪製的懷舊壁畫。",
            food=["中峇魯水粿", "Tiong Bahru Bakery 可頌"],
            details="**🚇 交通：** 搭乘地鐵綠線至 **Tiong Bahru (EW17)** 站，A 出口步行約 8-10 分鐘。"
        )
        render_spot_card(
            "17:00 - 18:30", "福康寧公園 (Fort Canning Park)",
            "必拍「螺旋階梯」。站在階梯底部仰拍，綠色藤蔓與藍天如同秘境天井。",
            details="**🚇 交通：** 地鐵 **Dhoby Ghaut** 站 B 出口走地下道即達。"
        )
        render_spot_card(
            "18:30 - 22:00", "克拉碼頭 (Clarke Quay) 晚餐",
            "新加坡河畔最閃耀的夜生活樞紐。晚餐後可漫步河岸或搭乘復古觀光船。",
            food=["珍寶海鮮辣椒螃蟹", "松發肉骨茶"],
            details="若要吃珍寶海鮮，請務必提前 1-2 週線上訂位。"
        )

    with day_tab2:
        st.markdown('<div class="day-header">1/17 (六) 歷史、色彩與美食中心</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 12:30", "小印度 (Little India)",
            "參觀維拉馬卡里亞曼興都廟，拍下彩虹般的陳東齡故居，感受濃郁異國氛圍。",
            food=["印度甩餅 (Roti Prata)", "拉茶"],
            details="**🚇 交通：** 地鐵 **Little India (NE7/DT12)** 站 E 出口。"
        )
        render_spot_card(
            "12:30 - 17:30", "甘幫格南 (Kampong Glam) & 哈芝巷",
            "宏偉的金頂蘇丹回教堂與充滿藝術塗鴉的哈芝巷，是挖寶與街拍的絕佳去處。",
            food=["Zam Zam 印度煎餅", "白蘭閣街蝦麵"],
            details="**🚇 交通：** 地鐵 **Bugis (EW12/DT14)** 站 B 出口。"
        )
        render_spot_card(
            "17:30 - 22:00", "牛車水 (Chinatown) & 麥士威熟食中心",
            "參觀佛牙寺與馬里安曼興都廟，在麥士威熟食中心大快朵頤。",
            food=["天天海南雞飯", "林志源肉乾"],
            details="天天海南雞飯若人太多，旁邊的「阿仔海南雞飯」也是好選擇。"
        )

    with day_tab3:
        st.markdown('<div class="day-header">1/18 (日) 濱海灣核心與璀璨之夜 (🔥三秀連發 + 微醺夜景)</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 12:00", "新加坡植物園 (Botanic Gardens)",
            "UNESCO 世界遺產。與媽媽散步於精緻的國家蘭花園，享受綠意。",
            details="**🚇 交通：** 地鐵 **Botanic Gardens (CC19/DT9)** 站。"
        )
        render_spot_card(
            "12:00 - 17:30", "濱海灣地標巡禮 & 老巴剎午餐",
            "與魚尾獅拍照接水求財，走過 DNA 造型的螺旋橋。午餐在老巴剎大啖沙嗲。",
            food=["老巴剎沙嗲", "福建炒麵"],
            details="建議路線：魚尾獅公園 ➔ 雙螺旋橋 ➔ 抵達金沙購物中心。"
        )
        render_spot_card(
            "17:30 - 20:15", "濱海灣花園 (Gardens by the Bay) & 超級樹秀",
            "參觀雲霧林室內瀑布。晚上 19:45 準時在超級樹下欣賞 Garden Rhapsody 聲光秀。",
            tips="秀結束後，請快速穿過蜻蜓橋抵達金沙酒店 Tower 3。",
            details="**🌟 完美銜接：** 19:45 燈光秀 ➔ 20:30 CÉ LA VI 酒吧。"
        )
        render_spot_card(
            "20:30 - 21:30", "金沙酒店 CÉ LA VI SKYBAR 夜景 🍸 🆕",
            "登上 57 層金沙酒店頂端！在 CÉ LA VI SkyBar 點杯調酒，您可以近距離看到傳說中的無邊際泳池（只限吧台區遠觀），並俯瞰整個新加坡璀璨夜景。這比觀景台更有氣氛，21:00 還能從高處欣賞 Spectra 水舞秀的雷射光芒！",
            food=["特色雞尾酒", "高空微醺體驗"],
            tips="建議提前線上訂位。這裡有 Smart Casual 服裝要求（避免拖鞋與背心）。入場通常需購買抵用券，可全額折抵飲料費用。",
            details="**📍 位置：** 金沙酒店 Tower 3 (第 3 塔樓) 57 樓。"
        )
        render_spot_card(
            "21:30 - 22:30", "🌟 晝夜璀璨藝術節 (Light to Night 2026)",
            "下樓後過橋前往市政區。欣賞國家美術館外牆的投影藝術秀，為夜晚畫下藝術句點。",
            details="從金沙走過 Jubilee Bridge (朱比利橋) 即可抵達 Padang 草地。"
        )

    with day_tab4:
        st.markdown('<div class="day-header">1/19 (一) 海島度假與圖書館</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 13:00", "聖淘沙 (Sentosa) 丹戎海灘",
            "搭乘纜車入島俯瞰港景。前往最安靜的丹戎海灘，享受慵懶的海島時光。",
            details="**🚇 交通：** 地鐵 **HarbourFront** 站轉乘纜車或輕軌。"
        )
        render_spot_card(
            "13:00 - 17:00", "SkyHelix 空中喜立 & 度假模式",
            "在 79 公尺高空雙腳懸空旋轉觀景。下午找間海灘俱樂部放空休息。",
            food=["海灘俱樂部輕食", "椰子水"],
            details="SkyHelix 緩緩上升的過程非常療癒，記得拿好手機！"
        )
        render_spot_card(
            "17:00 - 22:00", "烏節路 (Orchard Road) & 烏節圖書館",
            "回到飯店周邊逛街。必訪烏節圖書館拍網美書架。晚餐享用胡椒味濃郁的肉骨茶。",
            food=["松發肉骨茶", "亞坤咖椰吐司"],
            details="圖書館位於 **Orchard Gateway** 3-4 樓。"
        )

    with day_tab5:
        st.markdown('<div class="day-header">1/20 (二) 悠閒早餐與最後採買</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 11:00", "飯店悠閒早晨與 Tanglin Mall",
            "今早可以睡到自然醒，與媽媽在飯店或樓下的 Tanglin Mall 慢慢吃早餐，享受悠閒時光。",
            food=["Toast Box 咖椰吐司", "飯店早餐"],
            tips="行李可先寄放在飯店櫃台，等最後要出發去機場時再領取。"
        )
        render_spot_card(
            "11:00 - 12:30", "武吉士 (Bugis) 伴手禮衝刺",
            "前往伴手禮天堂「武吉士街」，買齊紀念品。最後享用道地甜品阿秋甜品。",
            food=["亮耀海南雞飯", "阿秋甜品"],
            details="**🚇 交通：** 地鐵 **Bugis (EW12/DT14)** 站。"
        )
        render_spot_card(
            "12:30 - 14:25", "前往機場 & 星耀樟宜 (Jewel)",
            "前往機場觀賞 Jewel 的室內瀑布。看著水流傾瀉而下，為旅程完美收尾。",
            tips="瀑布位於 Jewel 正中央，建議先去 T3 辦理托運。祝旅程平安順利！",
            details="從飯店搭計程車/Grab 到機場約 25-30 分鐘。"
        )

# --- 7. 必買伴手禮清單 ---
elif page == "🛍️ 必買伴手禮清單":
    st.markdown('<div class="main-header">🛍️ 新加坡 5 大必買名產</div>', unsafe_allow_html=True)
    render_spot_card("1. 綠蛋糕 (Pandan Cake)", "Bengawan Solo", "最具代表性的伴手禮，帶有淡淡椰香與植物清香。", details="建議機場回程再買，保持最新鮮。")
    render_spot_card("2. 鹹蛋魚皮", "IRVINS", "炸得酥脆的魚皮裹上鹹蛋黃醬，超級涮嘴。", details="各大超市或 VivoCity 都有店。")
    render_spot_card("3. 咖椰醬 (Kaya Jam)", "Ya Kun / Toast Box", "新加坡國民早餐靈魂，配奶油吐司超正宗。", details="超市賣的 Glory 牌便宜又好吃。")
    render_spot_card("4. 百勝廚叻沙拉麵", "Prima Taste", "曾評為全球最好吃泡麵。湯頭極濃郁。", details="黑色包裝 Laksa 口味。")
    render_spot_card("5. 小 CK (Charles & Keith)", "平價精品包", "新加坡本土品牌，價格約台灣 8-9 折。", details="滿 SGD 100 即可辦理退稅。")

# --- 8. 夜生活分頁 ---
elif page == "🍷 飯店周邊夜生活":
    st.markdown('<div class="main-header">🍷 飯店周邊微醺推薦</div>', unsafe_allow_html=True)
    render_spot_card("Manhattan Bar", "亞洲 50 大酒吧", "優雅的紐約復古風，氣氛優雅。", details="位於 Conrad 飯店 2 樓，步行約 5 分鐘。")
    render_spot_card("Dempsey Hill", "森林裡的浪漫", "舊軍營改建，環境超美。推薦 PS.Cafe。", details="搭計程車約 5 分鐘。")
    render_spot_card("Hard Rock Cafe", "經典美式搖滾", "就在飯店隔壁，有 Live Band 演奏。", details="步行 1 分鐘即達。")

# --- 9. 其他推薦 ---
elif page == "🌟 其他熱門推薦":
    st.markdown('<div class="main-header">🌟 備選行程推薦</div>', unsafe_allow_html=True)
    render_spot_card("推薦 1：如切/加東", "彩色娘惹屋", "色彩繽紛的街區，適合拍網美照。", details="定位在 Koon Seng Road。")
    render_spot_card("推薦 2：讚美廣場", "夢幻白教堂", "電影拍攝地，充滿浪漫氛圍。", details="地鐵 City Hall 站旁。")
    render_spot_card("推薦 3：舊禧街警察局", "彩虹大樓", "擁有 927 扇彩虹窗戶，必拍打卡點。", details="就在克拉碼頭旁。")

# --- 10. 地圖導航 ---
elif page == "🗺️ 地圖導航":
    st.markdown('<div class="main-header">🗺️ 行程景點地圖</div>', unsafe_allow_html=True)
    layer = pdk.Layer("ScatterplotLayer", locations, get_position=["lon", "lat"], get_color=[200, 30, 0, 160], get_radius=300, pickable=True)
    view_state = pdk.ViewState(latitude=1.29, longitude=103.85, zoom=11, pitch=50)
    r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{name}"}, map_style='https://basemaps.cartocdn.com/gl/positron-gl-style/style.json')
    st.pydeck_chart(r)

# --- 11. 預算估算 ---
elif page == "💰 預算估算":
    st.markdown('<div class="main-header">💰 旅遊預算計算機</div>', unsafe_allow_html=True)
    num_people = st.number_input("人數", min_value=1, value=2)
    food_budget = st.slider("每日餐飲預算 (SGD/人)", 30, 100, 50)
    transport_budget = st.slider("每日交通預算 (SGD/人)", 5, 30, 10)
    ticket_budget = st.number_input("全程門票總預算 (SGD/人)", value=110)
    total_sgd = (food_budget * 5 + transport_budget * 5 + ticket_budget) * num_people
    st.markdown(f"### 📊 兩人總預算預估: **${total_sgd} SGD** (約 NT$ {total_sgd*24:,.0f})")

# --- 12. 行前清單 ---
elif page == "✅ 出國當天備忘錄 (詳細版)":
    st.markdown('<div class="main-header">✅ 出國當天備忘錄 (詳細版)</div>', unsafe_allow_html=True)
    with st.expander("🛂 1. 必備文件", expanded=True):
        st.write("* 護照、ICA 電子入境卡")
    with st.expander("💰 2. 金錢支付", expanded=True):
        st.write("* 每人換 SGD 150-200 現金，其餘刷卡")
    with st.expander("👕 3. 衣物與生活小物", expanded=True):
        st.write("* 薄外套必帶、英式三腳轉接頭、面紙、防曬用品")
    st.success("祝您和媽媽旅途愉快！ Have a nice trip! ✈️")
