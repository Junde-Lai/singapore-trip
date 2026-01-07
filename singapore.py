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
    st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e88c7f58-2159-4a3c-8ee4-3919ed7f8a19/dg02zac-b7472d06-5c0c-492a-bd57-69dbaf190b2a.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiIvZi9lODhjN2Y1OC0yMTU5LTRhM2MtOGVlNC0zOTE5ZWQ3ZjhhMTkvZGcwMnphYy1iNzQ3MmQwNi01YzBjLTQ5MmEtYmQ1Ny02OWRiYWYxOTBiMmEucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.QUm9G1x_098zqjyi7JyFjX5sHffD7zF8ejCrDyXu5fU", width=120)
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
    st.caption("Grab: 叫車預約\nGoogle Maps: 地圖導航\nMyICA: 入境卡申報")

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

    day_tabs = st.tabs(["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"])

    # --- DAY 1 ---
    with day_tabs[0]:
        st.markdown('<div class="day-header">1/16 (五) 抵達、文創區與河畔夜景</div>', unsafe_allow_html=True)
        render_spot_card(
            "15:30 - 17:00", "中峇魯 (Tiong Bahru) - 歷史文藝街區",
            "中峇魯是新加坡最迷人且歷史悠久的住宅區，完美融合了 1930 年代興建的「裝飾藝術風格 (Art Deco)」建築。漫步在獨特的圓弧型白色組屋與優雅的螺旋樓梯間，您可以尋找由藝術家葉耀宗繪製的懷舊壁畫，如《巴剎與算命佬》，感受昔日鄰里情懷。這裡不只是攝影勝地，更是新加坡慢活靈魂的縮影，街道兩旁隱藏著許多獨立書店與精品咖啡館。",
            food=["中峇魯水粿 (Jian Bo)", "Tiong Bahru Bakery 可頌"],
            tips="壁畫主要分佈在 Seng Poh Lane 一帶，建議開啟地圖搜尋「Tiong Bahru Murals」。",
            details="**🚇 交通：** 地鐵綠線至 **Tiong Bahru (EW17)** 站，A 出口步行 8-10 分鐘。"
        )
        render_spot_card(
            "17:00 - 18:30", "福康寧公園 (Fort Canning Park) - 螺旋階梯",
            "這座鬱鬱蔥蔥的山丘曾是馬來皇族的禁地，現今最著名的則是隱藏在公園邊緣的「螺旋階梯 (Tree Tunnel)」。從深邃的地下隧道往上仰望，茂密的綠色藤蔓與藍天交織出的天井美景，彷彿通往愛麗絲夢遊仙境的入口，是攝影愛好者絕不能錯過的奇幻景點。拍完照後，可以順著山丘漫步，感受涼爽的樹蔭與古老的堡壘遺跡。",
            tips="階梯常需排隊，若時間較趕，在底部快速拍幾張氛圍感照片也很棒。",
            details="**🚇 交通：** 地鐵 **Dhoby Ghaut (NS24)** 站 B 出口，往 Penang Road 走地下道即達。"
        )
        render_spot_card(
            "18:30 - 22:00", "克拉碼頭 (Clarke Quay) - 晚宴與河畔漫步",
            "當夜幕降臨，新加坡河畔的舊倉庫區化身為霓虹閃爍的派對天堂。您可以沿著河岸漫步，欣賞歷史悠久的橋樑與倒映在水面的摩天大樓。這裡匯集了世界級美食，尤其是著名的海鮮餐館，點上一份辛辣鮮甜的辣椒螃蟹，配上外酥內軟的炸饅頭，是來到新加坡最正宗的味覺體驗。餐後吹著晚風，看著河面上來往的觀光船，愜意無比。",
            food=["珍寶海鮮 (Jumbo) 辣椒螃蟹", "松發肉骨茶 (河畔店)"],
            details="**🚢 推薦：** 可搭乘 **Singapore River Cruise** 復古木船，航程約 40 分鐘，從水上視角看克拉碼頭與金沙。"
        )

    # --- DAY 2 ---
    with day_tabs[1]:
        st.markdown('<div class="day-header">1/17 (六) 多元種族色彩：歷史與信仰的對話</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 12:30", "小印度 (Little India) - 香料與色彩的盛宴",
            "一踏入這區，視覺與嗅覺將瞬間被喚醒！街道兩側是色彩大膽鮮豔的店屋，空氣中瀰漫著濃郁的茉莉花與香料芬芳。參觀精雕細琢的「維拉馬卡里亞曼興都廟」，欣賞塔樓上無數生動的神像雕刻；接著前往「陳東齡故居」，這座兩層樓的彩色別墅是小印度的靈魂地標，展現了華麗的幾何與色彩美學，每一角都是完美的拍照背景。",
            food=["竹腳中心印度甩餅 (Roti Prata)", "拉茶 (Teh Tarik)"],
            tips="進入興都廟需脫鞋，建議當天穿著方便穿脫的鞋子。廟內拍照請避開祭祀活動。",
            details="**🚇 交通：** 地鐵 **Little India (NE7)** 站，E 出口出來即是美食天堂竹腳中心。"
        )
        render_spot_card(
            "12:30 - 17:30", "甘幫格南 (Kampong Glam) & 哈芝巷",
            "這裡是新加坡馬來與穆斯林文化的核心。壯觀的「蘇丹回教堂」擁有巨大的金色圓頂，在陽光下閃閃發光；緊鄰的「哈芝巷 (Haji Lane)」則是極大反差的潮流領地。狹窄巷弄佈滿了充滿生命力的巨幅噴漆壁畫，兩側林立著個性店鋪與中東香氛店。您可以帶媽媽在金頂回教堂前拍下如畫般的美景，再走入巷弄挖寶。",
            food=["Zam Zam 印度煎餅 (Murtabak)", "白蘭閣街蝦麵"],
            details="哈芝巷下午一點後店家會開齊，適合午後慢慢散步尋找有趣的文創商品。"
        )
        render_spot_card(
            "17:30 - 22:00", "牛車水 (Chinatown) - 早期華人與融合美學",
            "這裡是新加坡早期華人移民的聚集地，保留了濃厚的歷史氛圍。您可以參觀莊嚴宏偉的「佛牙寺龍華院」，其建築風格融合了唐代與曼陀羅元素，內部金碧輝煌。令人驚訝的是，僅一街之隔就是新加坡最古老的印度教廟宇「馬里安曼興都廟」，展現了新加坡不同宗教的和諧共處。晚上街道上的紅燈籠亮起，充滿濃厚的東方風情，是體驗華人文化與美食的絕佳地點。",
            food=["麥士威熟食中心 (天天海南雞飯)", "林志源肉乾", "老伴豆花"],
            tips="天天海南雞飯若排隊過長，隔壁的「阿仔海南雞飯」據說是前主廚出來開的，同樣美味。",
            details="**🚇 交通：** 地鐵 **Maxwell (TE18)** 站，一出來即是麥士威熟食中心。"
        )

    # --- DAY 3 ---
    with day_tabs[2]:
        st.markdown('<div class="day-header">1/18 (日) 濱海核心：高空微醺與璀璨藝術節 🌙</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 12:00", "新加坡植物園 (Botanic Gardens) - UNESCO 遺產",
            "擁有 160 多年歷史的新加坡植物園，是這座城市唯一的 UNESCO 世界遺產。這裡宛如一片隱身於都市的熱帶雨林，漫步於優雅的「國家蘭花園」，您可以欣賞到超過 2000 種蘭花競相綻放。這裡是與媽媽悠閒散步、享受森林浴的最佳去處，內部的冷室館更是模擬了高山森林氣候，涼爽宜人。",
            tips="蘭花園需門票，但其展示的精緻程度絕對值得一遊。",
            details="**🚇 交通：** 地鐵 **Botanic Gardens (CC19)** 站即達。"
        )
        render_spot_card(
            "12:00 - 17:30", "地標巡禮：魚尾獅公園、螺旋橋、老巴剎",
            "收集新加坡最經典的明信片視角。站在魚尾獅公園與噴水的魚尾獅合照、接水求財，接著走過擁有 DNA 雙螺旋造型的螺旋橋抵達金沙酒店。午餐特別安排在「老巴剎 (Lau Pa Sat)」，這是一座建於 19 世紀的維多利亞時代鑄鐵建築，在現代摩天大樓包圍下享受沙嗲串燒，感受強烈的時空交錯感。",
            food=["老巴剎沙嗲串燒 (Satay)", "福建炒麵"],
            details="**🚶 建議路線：** 魚尾獅 ➔ 雙螺旋橋 ➔ 金沙購物中心 ➔ 步行至老巴剎。"
        )
        render_spot_card(
            "17:30 - 20:30", "濱海灣花園 (Gardens by the Bay) ✕ 超級樹秀",
            "先在冷室「雲霧林」觀看 35 公尺高的室內瀑布。晚上 19:45，請找一個舒適的位置，欣賞「超級樹 (Supertree Grove)」的 Garden Rhapsody 燈光秀。隨著壯闊的音樂，發光的巨樹群閃爍起繽紛色彩，帶來極致的視覺震撼。這場秀是新加坡將未來感科技與自然結合的最美呈現。",
            tips="超級樹秀結束後，請快速穿過金沙酒店連通道前往第 3 塔樓 (Tower 3)。",
            details="**🌟 完美銜接：** 19:45 燈光秀 ➔ 20:30 抵達 CÉ LA VI 酒吧。"
        )
        render_spot_card(
            "20:30 - 21:45", "金沙 CÉ LA VI SkyBar - 高空微醺 🍸",
            "登上 57 層樓之巔！在 CÉ LA VI SkyBar 點杯精緻調酒，您可以近距離俯視著名的無邊際泳池，並將整座濱海灣的璀璨燈海盡收眼底。21:00 時，還可以從這個絕佳的高空視角，俯瞰下方噴水池射出的雷射水舞秀。比起封閉的觀景台，這裡的露天氛圍更能讓您和媽媽徹底放鬆，享受頂級的微醺之夜。",
            tips="建議提前預約並說明慶生/旅遊需求。有 Smart Casual 著裝要求（避免拖鞋、男士避開背心）。",
            details="**📍 位置：** 金沙酒店 Tower 3 頂樓入口。"
        )
        render_spot_card(
            "21:45 - 23:00", "🌟 晝夜璀璨藝術節 (Light to Night 2026)",
            "**今晚最震撼的 Ending！** 此時深夜氣溫最涼爽，國家美術館與維多利亞劇院的古典牆面化身巨大畫布，上演震撼的光雕投影秀。深夜的人潮已散，您可以和媽媽悠閒散步在 Padang 草地上，吹著晚風欣賞古典建築在數位藝術下的繽紛變身。這是年度限時的盛會，絕對值得以此收官您的濱海之夜。",
            tips="光雕效果在深夜最清晰。若體力受限，可從金沙直接叫車到國家美術館門口，少走一點路。",
            details="**📍 地點：** 市政區 (Civic District)。這是完全免費的年度藝術盛事。"
        )

    # --- DAY 4 ---
    with day_tabs[3]:
        st.markdown('<div class="day-header">1/19 (一) 海島度假與生活設計美學</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 13:00", "聖淘沙 (Sentosa) - 丹戎海灘慢時光",
            "搭乘纜車入島，從高空俯視繁忙的港景。我們避開擁擠的環球影城，直奔最安靜的「丹戎海灘 (Tanjong Beach)」，這裡是聖淘沙最有南洋度假感的角落。您可以赤腳漫步於細軟白沙，看著搖曳椰林享受海島微風，享受與媽媽共享的慢節奏度假時光。",
            tips="纜車票事先買好電子票，掃碼即可快速通關。",
            details="**🚇 交通：** 地鐵 **HarbourFront** 站轉乘纜車或輕軌進入。"
        )
        render_spot_card(
            "13:00 - 17:00", "SkyHelix 空中喜立 - 360 度全景體驗",
            "體驗聖淘沙最受歡迎的高空設施 SkyHelix。您的座位會緩緩旋轉上升至 79 公尺高空，雙腳懸空俯瞰聖淘沙全景與南部島嶼群。在上面喝著飲料，與媽媽一起拍下這段高空度假的回憶。隨後可找間海灘俱樂部休息，點杯調酒或現剖椰子，沉浸在度假氛圍中。",
            food=["海灘俱樂部調酒", "新鮮椰子水"],
            details="SkyHelix 上升過程平穩，視野開闊，票價通常含一杯飲料。"
        )
        render_spot_card(
            "17:00 - 22:00", "烏節路 (Orchard Road) & 烏節圖書館",
            "回到飯店周邊。必訪隱身於商場內的「烏節圖書館 (library@orchard)」，其流線型波浪書架設計已成為全球文青的朝聖點。晚餐享用胡椒味濃郁的肉骨茶，溫潤的熱湯能洗去整日疲憊，為海島之旅劃下暖心的句點。",
            food=["松發肉骨茶 (Song Fa)", "亞坤咖椰吐司"],
            details="圖書館位於 **Orchard Gateway** 3-4 樓。晚餐推薦松發，湯頭可無限續加。"
        )

    # --- DAY 5 ---
    with day_tabs[4]:
        st.markdown('<div class="day-header">1/20 (二) 悠閒結尾：飯店慢活與星耀驚喜</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 11:30", "飯店慢活與最後採買",
            "最後一個早晨不需要趕路。在飯店享用完早餐後，您可以和媽媽到飯店直通的 **Tanglin Mall** 逛逛。這裡有高品質的超市可以買到精緻的新加坡醬料或果醬。或是前往附近的南洋老牌咖啡店，體驗當地人最日常的早茶，享受離開前的悠閒節奏，徹底放鬆心情。",
            food=["Killiney Kopitiam 咖啡", "飯店早餐"],
            tips="11:30 辦理退房，建議直接從飯店預約計程車前往機場，節省體力負擔。",
            details="Tanglin Mall 內有許多質感生活雜貨店，非常適合最後的紀念品採買。"
        )
        render_spot_card(
            "12:00 - 14:25", "星耀樟宜 (Jewel) - 雨漩渦震撼告別",
            "在前往櫃台報到前，絕對要朝聖這座世界級的地標。走入由玻璃與鋼骨建構的森林谷，欣賞高達 40 公尺、從屋頂傾瀉而下的「雨漩渦 (Rain Vortex)」。水霧在陽光下如夢似幻，這是新加坡送給每一位旅者最難忘的告別禮物。看著瀑布，為這段完美的旅程畫下圓滿句點。",
            tips="瀑布從 11:00 開始噴水。建議先去 T3 航廈華航櫃台報到托運，再輕裝逛 Jewel。",
            details="**✈️ 提醒：** 班機 CI752 為 14:25 起飛，請務必於 13:30 前完成出境安檢。"
        )

# --- 7. 其他分頁內容 ---

elif page == "🗺️ 互動景點地圖":
    st.markdown('<div class="main-header">🗺️ 旅程足跡導航</div>', unsafe_allow_html=True)
    st.pydeck_chart(pdk.Deck(
        layers=[pdk.Layer("ScatterplotLayer", locations, get_position=["lon", "lat"], get_color=[200, 30, 0, 160], get_radius=400, pickable=True)],
        initial_view_state=pdk.ViewState(latitude=1.29, longitude=103.85, zoom=11, pitch=45),
        tooltip={"text": "{name}"},
        map_style='https://basemaps.cartocdn.com/gl/positron-gl-style/style.json'
    ))

elif page == "💰 預算估算":
    st.markdown('<div class="main-header">💰 旅遊預算計算機</div>', unsafe_allow_html=True)
    num_people = st.number_input("人數", min_value=1, value=2)
    food_budget = st.slider("每日餐飲預算 (SGD/人)", 30, 150, 70)
    tickets = st.number_input("全程門票總預算 (SGD/人)", value=120)
    total_sgd = (food_budget * 5 + tickets) * num_people
    st.metric("兩人總預算預估 (不含機宿)", f"SGD ${total_sgd}", f"約 NT$ {total_sgd*24:,.0f}")

elif page == "🛍️ 必買伴手禮清單":
    st.markdown('<div class="main-header">🛍️ 新加坡 5 大必買名產</div>', unsafe_allow_html=True)
    render_spot_card("1. 綠蛋糕 (Pandan Cake)", "Bengawan Solo", "最具代表性的班蘭蛋糕，口感綿密帶椰香，機場買最新鮮。", details="買回家後建議 2 天內食用完畢。")
    render_spot_card("2. 鹹蛋魚皮", "IRVINS", "新加坡零食之王，炸魚皮裹滿鹹蛋黃醬，超級涮嘴。", details="各大超市或機場都有分店。")
    render_spot_card("3. 咖椰醬 (Kaya Jam)", "Ya Kun / Toast Box", "早餐靈魂，抹在吐司上加奶油就是正宗南洋味。", details="超市買玻璃罐裝便宜且口味選擇多。")
    render_spot_card("4. 百勝廚叻沙拉麵", "Prima Taste", "世界第一泡麵，湯頭極濃郁，推薦買黑色包裝 Laksa 口味。", details="超市採購比機場便宜很多。")
    render_spot_card("5. 小 CK 包包", "Charles & Keith", "本地平價精品，價格約台灣 8 折左右，款式更新極快。", details="滿 $100 即可憑護照辦理退稅。")

elif page == "✅ 出國準備備忘錄":
    st.markdown('<div class="main-header">✅ 行前準備確認清單</div>', unsafe_allow_html=True)
    st.info("出發前請再次勾選，確保旅途無憂！")
    st.checkbox("護照效期超過 6 個月")
    st.checkbox("已申報 SG Arrival Card (ICA) 入境卡")
    st.checkbox("已開通電信漫遊或安裝 eSim")
    st.checkbox("英式三腳轉接頭 (Type G)")
    st.checkbox("薄外套 (防冷氣冰箱)")
    st.checkbox("隨身濕紙巾 (吃螃蟹必備)")
    st.success("一切準備就緒，祝您與媽媽擁有完美的旅程！✈️")
