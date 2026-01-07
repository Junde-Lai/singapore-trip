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
    
    /* 標題背景圖與 Hero Banner */
    .hero-container {
        position: relative;
        background-color: #2b3e50; 
        background-image: url('https://preparetravelplans.com/wp-content/uploads/2020/09/Things-to-Do-in-Singapore-at-Night.jpg');
        background-size: cover;
        background-position: center;
        border-radius: 20px;
        padding: 80px 20px;
        margin-bottom: 35px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }
    
    .hero-overlay {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.55); 
        border-radius: 20px;
    }
    
    .hero-title {
        position: relative; 
        color: #ffffff;
        font-size: 48px;
        font-weight: 800;
        text-shadow: 4px 4px 8px rgba(0,0,0,0.8);
        margin: 0;
        letter-spacing: 3px;
    }
    
    .hero-subtitle {
        position: relative;
        color: #f0f0f0;
        font-size: 22px;
        font-weight: 500;
        margin-top: 15px;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.8);
    }

    /* 行程卡片樣式 */
    .day-header {
        font-size: 28px;
        font-weight: bold;
        color: #D35400;
        border-bottom: 3px solid #D35400;
        padding-bottom: 12px;
        margin-top: 30px;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
    }

    .spot-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 18px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.07);
        margin-bottom: 20px;
        border-left: 8px solid #3498DB;
        transition: all 0.3s ease;
    }
    
    .spot-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 20px rgba(0,0,0,0.12);
        border-left: 8px solid #2ECC71;
    }

    .spot-title {
        font-size: 24px;
        font-weight: bold;
        color: #2E86C1;
        margin-bottom: 15px;
    }

    .spot-desc {
        font-size: 17px;
        line-height: 1.8;
        color: #34495E;
        text-align: justify;
    }

    .food-badge {
        display: inline-block;
        background-color: #F4D03F;
        color: #2C3E50;
        padding: 6px 15px;
        border-radius: 25px;
        font-weight: bold;
        font-size: 15px;
        margin-right: 10px;
        margin-top: 15px;
    }

    .info-box {
        background-color: #FBFCFC;
        padding: 18px;
        border-radius: 12px;
        font-size: 15px;
        color: #707B7C;
        margin-top: 20px;
        border-left: 4px solid #D5DBDB;
    }

    /* 調整側邊欄樣式 */
    [data-testid="stSidebar"] {
        background-color: #F4F6F7;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. 數據準備 (景點位置) ---
locations = pd.DataFrame({
    'name': ['JEN Tanglin', '中峇魯', '福康寧公園', '克拉碼頭', '小印度', '甘幫格南', '牛車水', '植物園', '魚尾獅公園', '濱海灣金沙', '濱海灣花園', '聖淘沙', '星耀樟宜'],
    'lat': [1.3056, 1.2865, 1.2925, 1.2905, 1.3068, 1.3023, 1.2839, 1.3138, 1.2867, 1.2834, 1.2815, 1.2494, 1.3602],
    'lon': [103.8237, 103.8270, 103.8465, 103.8463, 103.8516, 103.8596, 103.8436, 103.8159, 103.8545, 103.8607, 103.8636, 103.8303, 103.9898]
})

# --- 4. 側邊欄：導航與基本資訊 ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/5315/5315386.png", width=100)
    st.title("🇸🇬 新加坡深度攻略")
    st.markdown("---")
    st.markdown("**📅 日期**：2026/1/16 - 1/20")
    st.markdown("**👥 旅客**：您與媽媽")
    st.markdown("---")
    
    st.info("""
    **🏨 住宿：JEN Singapore Tanglin**
    這間飯店由香格里拉集團管理，位於使館區附近，環境安靜優雅。直通 Tanglin Mall，購物與採買伴手禮極為方便。
    """)
    
    page = st.radio("前往頁面", ["📅 5天4夜行程總覽", "🗺️ 互動景點地圖", "💰 預算估算", "🛍️ 必買伴手禮清單", "✅ 出國準備備忘錄"])
    
    st.markdown("---")
    st.markdown("### 📞 緊急聯繫與APP")
    st.caption("Grab: 叫車必備\nGoogle Maps: 導航\nMyICA: 入境申報")

# --- 5. 輔助功能：產生景點卡片 ---
def render_spot_card(time, title, desc, food=None, tips=None, details=None):
    food_html = "".join([f'<span class="food-badge">🍽️ {f}</span>' for f in food]) if food else ""
    tips_html = f'<div class="info-box">💡 <strong>貼心建議：</strong>{tips}</div>' if tips else ""
    
    st.markdown(f"""
    <div class="spot-card">
        <div class="spot-title">{time} ｜ {title}</div>
        <div class="spot-desc">{desc}</div>
        <div style="margin-top:10px;">{food_html}</div>
        {tips_html}
    </div>
    """, unsafe_allow_html=True)
    
    if details:
        with st.expander(f"🔍 點擊查看：{title} 交通與深度攻略"):
            st.info(details)

# --- 6. 主頁面內容 ---

if page == "📅 5天4夜行程總覽":
    st.markdown("""
    <div class="hero-container">
        <div class="hero-overlay"></div>
        <h1 class="hero-title">✨ 新加坡五天四夜：極致深度探索</h1>
        <p class="hero-subtitle">經典地標 ✕ 多元文化 ✕ 高空微醺 ✕ 在地慢活</p>
    </div>
    """, unsafe_allow_html=True)

    day_tabs = st.tabs(["Day 1: 抵達與文創", "Day 2: 文化色彩", "Day 3: 濱海巔峰", "Day 4: 海島放鬆", "Day 5: 圓滿告別"])

    # --- DAY 1 ---
    with day_tabs[0]:
        st.markdown('<div class="day-header">1/16 (五) 抵達、文創區與河畔夜景</div>', unsafe_allow_html=True)
        render_spot_card(
            "15:30 - 17:00", "中峇魯 (Tiong Bahru) - 歷史文藝街區",
            "這裡是新加坡最古老的住宅區之一，完美融合了 1930 年代興建的「裝飾藝術風格 (Art Deco)」建築。漫步在獨特的圓弧型白色組屋間，您可以尋找由藝術家葉耀宗繪製的懷舊壁畫，如《巴剎與算命佬》，感受昔日鄰里情懷。這裡不只是攝影勝地，更是新加坡慢活靈魂的縮影，街道兩旁隱藏著許多獨立書店與精品咖啡館。",
            food=["中峇魯水粿 (Jian Bo)", "Tiong Bahru Bakery 可頌"],
            tips="壁畫主要分佈在 Seng Poh Lane 一帶，建議開啟地圖搜尋「Tiong Bahru Murals」。",
            details="**🚇 交通：** 地鐵綠線至 **Tiong Bahru (EW17)** 站，A 出口步行 8-10 分鐘。"
        )
        render_spot_card(
            "17:00 - 18:30", "福康寧公園 (Fort Canning Park) - 螺旋階梯",
            "這座山丘曾是馬來皇族的禁地，現今最吸引人的則是隱藏在公園邊緣的「螺旋階梯 (Tree Tunnel)」。從深邃的地下隧道往上仰望，茂密的綠色藤蔓與藍天交織出的天井美景，彷彿通往愛麗絲夢遊仙境的入口，是攝影愛好者絕不能錯過的奇幻景點。拍完照後，可以順著山丘漫步，感受涼爽的樹蔭。",
            tips="階梯常需排隊 20 分鐘以上，若時間緊湊，在底部快速拍幾張氛圍感也很棒。",
            details="**🚇 交通：** 地鐵 **Dhoby Ghaut (NS24)** 站 B 出口，走地下道即達。"
        )
        render_spot_card(
            "18:30 - 22:00", "克拉碼頭 (Clarke Quay) - 晚宴與河畔漫步",
            "當夜幕降臨，新加坡河畔的舊倉庫區化身為霓虹閃爍的派對天堂。您可以沿著河岸漫步，欣賞歷史悠久的橋樑與倒映在水面的摩天大樓。這裡匯集了世界級美食，尤其是著名的海鮮餐館，點上一份辛辣鮮甜的辣椒螃蟹，配上外酥內軟的炸饅頭，是來到新加坡最正宗的味覺體驗。",
            food=["珍寶海鮮 (Jumbo) 辣椒螃蟹", "松發肉骨茶 (河畔店)"],
            details="**🚢 推薦：** 若體力尚可，可搭乘 **Singapore River Cruise** 復古木船，航程約 40 分鐘，從水上視角看金沙燈光秀。"
        )

    # --- DAY 2 ---
    with day_tabs[1]:
        st.markdown('<div class="day-header">1/17 (六) 多元種族色彩：歷史與信仰的對話</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 12:30", "小印度 (Little India) - 香料與色彩的盛宴",
            "一踏入這區，視覺與嗅覺將瞬間被喚醒！街道兩側是色彩大膽鮮豔的店屋，空氣中瀰漫著濃郁的茉莉花與咖哩香。參觀精雕細琢的「維拉馬卡里亞曼興都廟」，欣賞塔樓上無數生動的神像；接著前往「陳東齡故居」，這座兩層樓的彩色別墅是小印度的靈魂地標，展現了華麗的幾何與色彩美學。",
            food=["竹腳中心印度甩餅 (Roti Prata)", "拉茶 (Teh Tarik)"],
            tips="進入興都廟需脫鞋，當天建議穿著方便穿脫的鞋子。",
            details="**🚇 交通：** 地鐵 **Little India (NE7)** 站，E 出口出來即是美食天堂竹腳中心。"
        )
        render_spot_card(
            "12:30 - 17:30", "甘幫格南 (Kampong Glam) & 哈芝巷",
            "這裡是新加坡馬來文化的核心。壯觀的「蘇丹回教堂」擁有巨大的金色圓頂，展現宗教的莊嚴；緊鄰的「哈芝巷 (Haji Lane)」則是極大反差的潮人領地。狹窄巷弄佈滿了充滿生命力的巨幅噴漆壁畫，兩側林立著個性店鋪與中東香氛店。您可以帶媽媽在金頂回教堂前拍下如畫般的美景，再走入巷弄挖寶。",
            food=["Zam Zam 印度煎餅 (Murtabak)", "白蘭閣街蝦麵"],
            details="哈芝巷的許多風格小店下午一點後才會全開，此時前往最熱鬧好逛。"
        )
        render_spot_card(
            "17:30 - 22:00", "牛車水 (Chinatown) - 早期華人與融合美學",
            "這裡是新加坡早期華人移民的聚集地，保留了濃厚的歷史氛圍。您可以參觀莊嚴宏偉的「佛牙寺龍華院」，其建築風格融合了唐代與曼陀羅元素，內部金碧輝煌。令人驚訝的是，僅一街之隔就是新加坡最古老的印度教廟宇「馬里安曼興都廟」，展現了新加坡不同宗教的和諧共處。晚上街道上的紅燈籠亮起，充滿濃厚的東方風情，是體驗華人文化與美食的絕佳地點。",
            food=["天天海南雞飯", "林志源肉乾", "老伴豆花"],
            tips="天天海南雞飯若排隊過長，隔壁的「阿仔海南雞飯」同樣美味且節省時間。",
            details="**🚇 交通：** 地鐵 **Maxwell (TE18)** 站，一出來即是麥士威熟食中心。"
        )

    # --- DAY 3 ---
    with day_tabs[2]:
        st.markdown('<div class="day-header">1/18 (日) 濱海核心：高空微醺與璀璨藝術節</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 12:00", "新加坡植物園 (Botanic Gardens) - UNESCO 遺產",
            "擁有 160 多年歷史，是新加坡唯一的 UNESCO 世界遺產。這裡宛如隱身於都市的熱帶雨林，漫步於優雅的「國家蘭花園」，您可以欣賞到超過 2000 種蘭花競相綻放，包括以各國名貴命名的品種。這裡是與媽媽悠閒散步、遠離塵囂、享受森林浴的最佳首選。",
            tips="蘭花園內部設有冷室館，是避暑賞花的絕佳地點。",
            details="**🚇 交通：** 地鐵 **Botanic Gardens (CC19)** 站即達。"
        )
        render_spot_card(
            "12:00 - 17:30", "地標巡禮：魚尾獅公園、螺旋橋、老巴剎",
            "收集新加坡最經典的明信片視角。站在魚尾獅公園與噴水的魚尾獅合照，接著走過極具未來感的螺旋橋抵達金沙酒店。午餐特別安排在「老巴剎 (Lau Pa Sat)」，這是一座建於 19 世紀的維多利亞時代鑄鐵建築，在現代金融區摩天大樓包圍下享受沙嗲串燒，感受強烈的時空交錯感。",
            food=["老巴剎沙嗲串燒 (Satay)", "福建炒麵"],
            details="老巴剎的沙嗲街下午七點後會封路，中午前往可坐在通風良好的建築體內享用。"
        )
        render_spot_card(
            "17:30 - 20:30", "濱海灣花園 (Gardens by the Bay) ✕ 超級樹秀",
            "先在「雲霧林」觀看 35 公尺高的室內瀑布。晚上 19:45，請在超級樹下找個位置，仰望 **Garden Rhapsody 燈光秀**。隨著激昂的音樂與跳動的燈光，巨大的超級樹彷彿擁有了生命，帶您走入阿凡達的奇幻世界。這場秀是新加坡將科技與自然結合的最美呈現。",
            tips="看完 19:45 的秀後，請快速穿過金沙酒店連通道前往第 3 塔樓 (Tower 3)。",
            details="**🌟 完美銜接攻略：** 19:45 燈光秀結束 ➔ 20:30 抵達 CÉ LA VI 酒吧。"
        )
        render_spot_card(
            "20:30 - 21:45", "金沙 CÉ LA VI SkyBar - 高空微醺 🍸",
            "登上 57 層樓之巔！在 CÉ LA VI SkyBar 點杯精緻調酒，您可以近距離俯視世界著名的無邊際泳池，並將整座濱海灣的閃耀燈海盡收眼底。21:00 時，還可以從這個絕佳的高空視角，觀察下方噴泉水幕射出的雷射光芒。比起封閉的觀景台，這裡的露天氛圍更能讓您和媽媽徹底放鬆，享受頂級的視覺饗宴。",
            tips="有 Smart Casual 服裝要求（建議避開夾腳拖、男士避開背心）。",
            details="**📍 位置：** 金沙酒店 Tower 3 頂樓電梯入口。"
        )
        render_spot_card(
            "21:45 - 23:00", "🌟 晝夜璀璨藝術節 (Light to Night 2026)",
            "**今晚最夢幻的壓軸！** 此時深夜氣溫最涼爽，國家美術館與維多利亞劇院的古典牆面化身巨大畫布，上演震撼的光雕投影投影秀。深夜的人潮已散，您可以和媽媽悠閒散步在 Padang 草地上，吹著涼爽的晚風，欣賞這些古典建築在數位藝術下的繽紛變身。這是年度限時的藝術盛會，絕對值得以此收官您的濱海之夜。",
            tips="深夜的光雕效果最好。若媽媽累了，可從金沙直接叫 Grab 抵達 National Gallery 門口。",
            details="**📍 地點：** 市政區 (Civic District)。完全免費的戶外藝術饗宴。"
        )

    # --- DAY 4 ---
    with day_tabs[3]:
        st.markdown('<div class="day-header">1/19 (一) 海島放鬆與生活設計美學</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 13:00", "聖淘沙 (Sentosa) - 丹戎海灘慢時光",
            "搭乘纜車入島，從高空俯視繁忙的港景與藍海。我們避開喧囂的遊樂設施，直奔島上最安靜的「丹戎海灘 (Tanjong Beach)」。這裡是聖淘沙最安靜、最有南洋度假感的角落。您可以赤腳漫步於細軟白沙，看著搖曳椰林享受海島微風，感受截然不同的都市寧靜。",
            tips="纜車票建議事先購買 QR Code，可節省排隊買票時間。",
            details="**🚇 交通：** 從 HarbourFront 地鐵站轉乘纜車或輕軌進入。"
        )
        render_spot_card(
            "13:00 - 17:00", "SkyHelix 空中喜立 - 360 度全景體驗",
            "坐在緩緩旋轉升空的 SkyHelix 座椅上，您的雙腳會懸空上升至 79 公尺的高空，360 度無死角地俯瞰聖淘沙全景與南部的眾多小島。在上面喝著涼爽飲料，與媽媽一起拍下這段高空度假的回憶。隨後找間海灘俱樂部休息，體驗正宗的島嶼節奏。",
            food=["海灘俱樂部調酒", "新鮮椰子水"],
            details="SkyHelix 的上升過程非常平穩，懼高者也通常能接受，視野無敵。"
        )
        render_spot_card(
            "17:00 - 22:00", "烏節路 (Orchard Road) & 烏節圖書館",
            "回到飯店周邊的購物天堂。必訪隱身於商場內的「烏節圖書館 (library@orchard)」，其流線型波浪書架設計已成為全球設計與文青愛好者的朝聖點。晚餐享用著名的胡椒味肉骨茶，濃郁的暖湯能洗去一整日的疲憊，為漫長的海島之旅劃下溫潤的句點。",
            food=["松發肉骨茶 (Song Fa)", "亞坤咖椰吐司"],
            details="圖書館位於 **Orchard Gateway** 3-4 樓。晚餐後可直接步行回飯店。"
        )

    # --- DAY 5 ---
    with day_tabs[4]:
        st.markdown('<div class="day-header">1/20 (二) 悠閒結尾：飯店早餐與星耀震撼</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 11:30", "Slow Morning：飯店早餐與最後採買",
            "旅程的最後一個早晨不需要趕路。在 **JEN Tanglin** 飯店享用完早餐後，您可以和媽媽到飯店直通的 **Tanglin Mall** 逛逛。這裡有高品質的超市（如 Marketplace）可以買到精緻的新加坡香料、醬料或果醬。或是前往附近的南洋老牌咖啡店，體驗當地人最日常的早茶生活，享受離開前的悠閒節奏。",
            food=["Killiney Kopitiam 傳統咖啡", "飯店早餐"],
            tips="11:30 辦理退房，建議直接從飯店叫 Grab 載著行李前往機場，省去體力負荷。",
            details="Tanglin Mall 內有許多質感小店，與一般的觀光商場不同，更具在地氣息。"
        )
        render_spot_card(
            "12:00 - 14:25", "星耀樟宜 (Jewel) - 雨漩渦與離境告別",
            "在前往櫃台報到前，絕對要朝聖這座世界之最。走入由玻璃與鋼骨建構出的室內森林，欣賞高達 40 公尺、從圓頂傾瀉而下的「雨漩渦 (Rain Vortex)」。水霧在陽光照射下如夢似幻，這是新加坡送給每一位旅者最完美的告別禮物。在震撼的瀑布前拍下最後的紀念照，帶著圓滿的回憶準備登機。",
            tips="瀑布從 11:00 開始噴水。建議先去 T3 華航櫃台報到托運行李，再輕裝逛 Jewel。",
            details="**✈️ 提醒：** 班機 CI752 於 14:25 起飛，請最遲於 13:30 完成出關安檢。"
        )

# --- 7. 其他分頁 ---
elif page == "🗺️ 互動景點地圖":
    st.markdown('<div class="main-header">🗺️ 旅程足跡導航</div>', unsafe_allow_html=True)
    st.pydeck_chart(pdk.Deck(
        layers=[pdk.Layer("ScatterplotLayer", locations, get_position=["lon", "lat"], get_color=[200, 30, 0, 160], get_radius=400, pickable=True)],
        initial_view_state=pdk.ViewState(latitude=1.29, longitude=103.85, zoom=11, pitch=45),
        tooltip={"text": "{name}"},
        map_style='https://basemaps.cartocdn.com/gl/positron-gl-style/style.json'
    ))
    st.caption("紅色圓點代表您的核心活動區。")

elif page == "💰 預算估算":
    st.markdown('<div class="main-header">💰 兩人開支預估</div>', unsafe_allow_html=True)
    sgd_per_day = st.slider("每人每日餐飲/交通預算 (SGD)", 30, 150, 70)
    tickets = st.number_input("全程兩人門票預估 (SGD)", value=250)
    total_sgd = (sgd_per_day * 2 * 5) + tickets
    st.metric("兩人總預算預估 (不含機宿)", f"SGD ${total_sgd}", f"約 TWD ${total_sgd*24:,.0f}")

elif page == "🛍️ 必買伴手禮清單":
    st.markdown('<div class="main-header">🛍️ 新加坡 5 大經典伴手禮</div>', unsafe_allow_html=True)
    render_spot_card("1. 綠蛋糕 (Pandan Cake)", "Bengawan Solo", "最具代表性的名產，清新班蘭味與綿密口感，機場買最方便。", details="買回家後建議 2 天內食用完畢。")
    render_spot_card("2. 鹹蛋魚皮", "IRVINS", "紅遍全球的零食，炸魚皮裹滿濃郁鹹蛋黃，超級涮嘴。", details="各大超市與機場皆有售。")
    render_spot_card("3. 咖椰醬 (Kaya Jam)", "Ya Kun / Toast Box", "早餐店靈魂，椰奶與雞蛋的香甜，帶回台灣配吐司超棒。", details="玻璃罐裝較重，記得妥善包裝防碎。")
    render_spot_card("4. 百勝廚叻沙拉麵", "Prima Taste", "曾評為世界第一泡麵，湯頭還原度 100%，必買黑包裝 Laksa。", details="各大超市如 FairPrice 最划算。")
    render_spot_card("5. 小 CK 包包", "Charles & Keith", "新加坡國民精品，價格約台灣 8 折，款式多且更新快。", details="消費滿 $100 可憑護照辦理退稅。")

elif page == "✅ 出國準備備忘錄":
    st.markdown('<div class="main-header">✅ 行前確認清單</div>', unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        st.subheader("🛂 文件與網路")
        st.write("- 護照 (效期 6 個月以上)")
        st.write("- ICA 入境卡 (出發前 3 天申報)")
        st.write("- 網路網卡/eSim (確認已安裝)")
        st.write("- 保險憑證與機票截圖")
    with cols[1]:
        st.subheader("🧴 生活小物")
        st.write("- 英式轉接頭 (三腳方形)")
        st.write("- 輕便雨傘/雨衣 (午後陣雨多)")
        st.write("- 薄外套 (室內冷氣像冰箱)")
        st.write("- 隨身濕紙巾 (吃海鮮必備)")

    st.success("一切準備就緒！祝您與媽媽擁有一個完美的新加坡之旅！✈️")
