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
    .stApp {
        font-family: "Microsoft JhengHei", "PingFang TC", sans-serif;
    }
    .main-header {
        font-size: 36px; 
        font-weight: 800; 
        color: #2C3E50;
        text-align: center;
        margin-bottom: 30px;
        letter-spacing: 2px;
        text-shadow: 2px 2px 4px #eee;
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
    
    **YOTEL Singapore Orchard Road**
    
    📍 366 Orchard Road
    🚇 近 Orchard MRT (烏節站)
    ✨ 特色：位於市中心黃金地段，交通極致便利，設計時尚現代。
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
    page = st.radio("前往頁面", ["📅 行程總覽", "🗺️ 地圖導航", "💰 預算估算", "✅ 行前清單"])

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
    'name': ['YOTEL Orchard', '樟宜機場', '中峇魯', '福康寧公園', '克拉碼頭', '小印度', '甘榜格南', '牛車水', '植物園', '濱海灣金沙', '濱海灣花園', '聖淘沙'],
    'lat': [1.3063, 1.3644, 1.2865, 1.2925, 1.2905, 1.3068, 1.3023, 1.2839, 1.3138, 1.2834, 1.2815, 1.2494],
    'lon': [103.8318, 103.9915, 103.8270, 103.8465, 103.8463, 103.8516, 103.8596, 103.8436, 103.8159, 103.8607, 103.8636, 103.8303],
    'type': ['Hotel', 'Airport', 'Spot', 'Spot', 'Spot', 'Spot', 'Spot', 'Spot', 'Spot', 'Landmark', 'Landmark', 'Island']
})

# --- 6. 主頁面邏輯 ---

if page == "📅 行程總覽":
    st.markdown('<div class="main-header">✨ 新加坡五天四夜：極致深度探索</div>', unsafe_allow_html=True)
    
    day_tab1, day_tab2, day_tab3, day_tab4, day_tab5 = st.tabs(["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"])

    with day_tab1:
        st.markdown('<div class="day-header">1/16 (五) 抵達、文創區與河畔夜景</div>', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        with col1:
             st.metric("抵達時間", "13:05", "T3 航廈")
        with col2:
            st.info("👋 歡迎！請先辦理入境、領行李，搭乘計程車/地鐵前往 YOTEL 辦理入住，放下行李輕裝出發！")

        render_spot_card(
            "15:30 - 17:00", "中峇魯 (Tiong Bahru)",
            "新加坡最古老的住宅區之一，融合了歷史底蘊與現代文青氣息。",
            food=["中峇魯水粿", "Tiong Bahru Bakery 可頌"],
            tips="壁畫散佈在不同巷弄，建議先在 Google Maps 標記好『Tiong Bahru Murals』的位置。",
            details="**🚇 交通指南：** 搭乘地鐵至 Tiong Bahru (EW17) 站，A 出口步行約 8-10 分鐘。"
        )
        render_spot_card(
            "17:00 - 18:30", "福康寧公園 (Fort Canning Park)",
            "這座山丘見證了新加坡的歷史變遷。必去打卡點是位於公園邊緣的「螺旋階梯」。",
            tips="螺旋階梯通常需要排隊拍照，建議預留一些時間。",
            details="**🚇 交通指南：** 搭乘地鐵至 Dhoby Ghaut (NS24/NE6/CC1) 站，B 出口步行至 Penang Road。"
        )
        render_spot_card(
            "18:30 - 22:00", "克拉碼頭 (Clarke Quay) 晚餐與夜遊",
            "新加坡河畔的熱鬧樞紐，舊倉庫改建成的餐廳與酒吧林立。",
            food=["珍寶/無招牌海鮮 (辣椒螃蟹)"],
            tips="吃螃蟹建議事先訂位，價格較高但份量足。",
            details="**🚇 交通指南：** 從福康寧公園步行約 10 分鐘即可抵達。"
        )

    with day_tab2:
        st.markdown('<div class="day-header">1/17 (六) 歷史、色彩與美食中心</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 12:30", "小印度 (Little India)",
            "踏入這裡彷彿瞬間移動到印度。空氣中飄散著香料味，建築色彩鮮豔大膽。",
            food=["竹腳中心 (Tekka Centre) 印度甩餅", "拉茶"],
            tips="進入印度廟宇需脫鞋。",
            details="**🚇 交通指南：** 搭乘地鐵至 Little India (NE7/DT12) 站，E 出口。"
        )
        render_spot_card(
            "12:30 - 17:30", "甘榜格南 (Kampong Glam)",
            "穆斯林文化區。金頂的蘇丹回教堂是地標，周圍的哈芝巷充滿塗鴉牆與個性小店。",
            food=["Zam Zam 印度煎餅", "土耳其料理"],
            tips="哈芝巷下午店鋪才全開，非常適合午後逛街拍照。",
            details="**🚇 交通指南：** 搭乘地鐵至 Bugis (EW12/DT14) 站，B 出口。"
        )
        render_spot_card(
            "17:30 - 22:00", "牛車水 (Chinatown)",
            "華人移民的歷史街區。參觀佛牙寺與馬里安曼廟。",
            food=["麥士威熟食中心 (天天海南雞飯)"],
            tips="天天海南雞飯通常大排長龍。",
            details="**🚇 交通指南：** 搭乘地鐵至 Maxwell (TE18) 站或 Chinatown (NE4/DT19) 站。"
        )

    with day_tab3:
        st.markdown('<div class="day-header">1/18 (日) 濱海灣核心與超級樹</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 12:00", "新加坡植物園 (Botanic Gardens)",
            "世界文化遺產，重點遊覽「國家蘭花園」。",
            tips="天氣炎熱，早上前往較為涼爽。",
            details="**🚇 交通指南：** 搭乘地鐵至 Botanic Gardens (CC19/DT9) 站。"
        )
        render_spot_card(
            "12:00 - 17:30", "濱海灣地標巡禮 & 老巴剎",
            "前往市中心，與魚尾獅拍照，步行經過螺旋橋。",
            food=["老巴剎沙嗲串燒", "福建炒麵"],
            details="**🚇 交通指南：** 搭乘地鐵至 Raffles Place (EW14/NS26) 站，F 出口。"
        )
        render_spot_card(
            "17:30 - 22:00", "濱海灣花園 (Gardens by the Bay)",
            "參觀兩大冷室：雲霧林與花穹。晚上欣賞超級樹燈光秀。",
            food=["Satay by the Bay"],
            tips="燈光秀時間為 19:45 和 20:45。",
            details="**🚇 交通指南：** 搭乘地鐵至 Bayfront (CE1/DT16) 站，B 出口。"
        )

    with day_tab4:
        st.markdown('<div class="day-header">1/19 (一) 海島放鬆與購物</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 13:00", "聖淘沙 (Sentosa) 上午",
            "搭乘纜車入島，直奔丹戎海灘 (Tanjong Beach)。",
            tips="纜車票建議事先購買。",
            details="**🚇 交通指南：** 搭乘地鐵至 HarbourFront (NE1/CC29) 站。"
        )
        render_spot_card(
            "13:00 - 18:00", "度假體驗 & SkyHelix",
            "體驗 SkyHelix 空中喜立，360度旋轉欣賞聖淘沙全景。",
            food=["海灘俱樂部輕食"],
            details="**SkyHelix：** 露天旋轉觀景台，會送一杯飲料。"
        )
        render_spot_card(
            "18:00 - 22:00", "烏節路 (Orchard Road) 回歸",
            "逛百貨、烏節圖書館打卡，晚餐吃肉骨茶。",
            food=["松發肉骨茶", "亞坤咖椰吐司"],
            tips="松發肉骨茶湯可以無限續加。",
            details="**📚 烏節圖書館：** 位於 Orchard Gateway 商場。"
        )

    with day_tab5:
        st.markdown('<div class="day-header">1/20 (二) 採買、高空觀景與告別</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 11:00", "金沙空中花園 (Sands SkyPark)",
            "登上金沙酒店頂樓，俯瞰濱海灣美景。",
            tips="早上人潮較少。",
            details="**🚇 交通指南：** 搭乘地鐵至 Bayfront (CE1/DT16) 站。"
        )
        render_spot_card(
            "11:00 - 12:30", "武吉士 (Bugis) 最後採買",
            "前往武吉士街採買平價伴手禮。",
            food=["亮耀海南雞飯", "Zam Zam 印度煎餅"],
            tips="人多擁擠，請注意隨身財物。",
            details="**🚇 交通指南：** 搭乘地鐵至 Bugis (EW12/DT14) 站。"
        )
        render_spot_card(
            "12:30 - 14:25", "前往機場 & 星耀樟宜 (Jewel)",
            "回飯店取行李前往機場，觀賞雨漩渦瀑布。",
            tips="瀑布位於 T1 前方。",
            details="**💦 雨漩渦：** 位於 Jewel 正中央，不需出境即可看到。"
        )

elif page == "🗺️ 地圖導航":
    st.markdown('<div class="main-header">🗺️ 行程景點地圖</div>', unsafe_allow_html=True)
    st.markdown("包含：飯店、機場、濱海灣、聖淘沙及各大文化區")
    
    # 建立地圖圖層
    layer = pdk.Layer(
        "ScatterplotLayer",
        locations,
        get_position=["lon", "lat"],
        get_color=[200, 30, 0, 160],
        get_radius=300,
        pickable=True,
    )
    
    # 設定視角
    view_state = pdk.ViewState(
        latitude=1.29,
        longitude=103.85,
        zoom=11,
        pitch=50,
    )
    
    # 渲染地圖 - 使用 CARTO 的免費樣式修復黑屏問題
    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "{name}\n類型: {type}"},
        map_style='https://basemaps.cartocdn.com/gl/positron-gl-style/style.json'
    )
    st.pydeck_chart(r)
    st.caption("🔴 紅點代表您行程中的主要停留點。您可以放大縮小查看相對位置。")

elif page == "💰 預算估算":
    st.markdown('<div class="main-header">💰 旅遊預算計算機</div>', unsafe_allow_html=True)
    st.info("此計算機僅估算當地花費（餐飲、交通、門票），**不含**機票與住宿費用。")
    
    num_people = st.number_input("人數", min_value=1, value=2)
    days = 5
    
    col1, col2, col3 = st.columns(3)
    with col1:
        food_budget = st.slider("每日餐飲預算 (SGD/人)", 30, 100, 50, help="熟食中心約 5-10 SGD/餐，餐廳約 20-40 SGD/餐")
    with col2:
        transport_budget = st.slider("每日交通預算 (SGD/人)", 5, 30, 10, help="MRT很便宜，Grab計程車較貴")
    with col3:
        ticket_budget = st.number_input("全程門票總預算 (SGD/人)", value=110, help="含空中花園、冷室、纜車等")

    total_sgd = (food_budget * days + transport_budget * days + ticket_budget) * num_people
    total_twd = total_sgd * 24 
    
    st.divider()
    st.subheader(f"📊 兩人總預算預估")
    st.markdown(f"**新幣 (SGD):** ${total_sgd}")
    st.markdown(f"**台幣 (TWD):** ${total_twd:,.0f} (匯率以 24 計算)")
    st.write("---")
    st.write("建議換匯金額：每人建議攜帶 **150 - 200 SGD** 現金，其餘使用信用卡 (Visa/Mastercard) 感應支付。")

elif page == "✅ 行前清單":
    st.markdown('<div class="main-header">✅ 出發前檢查表</div>', unsafe_allow_html=True)
    st.checkbox("填寫 SG Arrival Card (電子入境卡) - 出發前3天內")
    st.checkbox("下載 Grab APP (並綁定信用卡)")
    st.checkbox("確認護照效期 (6個月以上)")
    st.checkbox("準備英式轉接頭 (三腳方形 Type G)")
    st.checkbox("準備好走的鞋子 (行程走路較多)")
    st.checkbox("攜帶薄外套 (室內冷氣強) 與雨傘")
    st.success("祝您和媽媽旅途愉快！ Have a nice trip! ✈️")
