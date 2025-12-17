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
    
    /* 隱藏預設的主標題邊距，讓背景圖可以貼頂 */
    .main .block-container {
        padding-top: 2rem;
    }

    /* 自定義 Hero Banner (標題背景圖) */
    .hero-container {
        position: relative;
        background-color: #2b3e50; /* 增加深色底色，避免圖片載入失敗時白字看不到 */
        background-image: url('https://preparetravelplans.com/wp-content/uploads/2020/09/Things-to-Do-in-Singapore-at-Night.jpg');
        background-size: cover;
        background-position: center;
        border-radius: 15px;
        padding: 60px 20px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    /* 加上半透明遮罩，讓文字更清晰 */
    .hero-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.6); /* 加深遮罩到 60% */
        border-radius: 15px;
    }
    
    /* 標題文字樣式 */
    .hero-title {
        position: relative; /* 確保文字在遮罩之上 */
        color: #ffffff;
        font-size: 42px;
        font-weight: 800;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.9); /* 加強文字陰影 */
        margin: 0;
        letter-spacing: 2px;
    }
    
    /* 副標題文字樣式 */
    .hero-subtitle {
        position: relative;
        color: #f0f0f0;
        font-size: 20px;
        font-weight: 500;
        margin-top: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.9); /* 加強文字陰影 */
    }

    /* 其他既有樣式 (日期標題、卡片等) */
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
    
    /* 一般頁面的標題樣式 (非首頁用) */
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
    'name': ['JEN Tanglin', '樟宜機場', '中峇魯', '福康寧公園', '克拉碼頭', '小印度', '甘榜格南', '牛車水', '植物園', '濱海灣金沙', '濱海灣花園', '聖淘沙', '如切/加東', '讚美廣場', '舊禧街警察局', 'Manhattan Bar', 'Dempsey Hill', 'Light to Night'],
    'lat': [1.3056, 1.3644, 1.2865, 1.2925, 1.2905, 1.3068, 1.3023, 1.2839, 1.3138, 1.2834, 1.2815, 1.2494, 1.3130, 1.2952, 1.2907, 1.3039, 1.3036, 1.2895],
    'lon': [103.8237, 103.9915, 103.8270, 103.8465, 103.8463, 103.8516, 103.8596, 103.8436, 103.8159, 103.8607, 103.8636, 103.8303, 103.9045, 103.8520, 103.8484, 103.8256, 103.8087, 103.8510],
    'type': ['Hotel', 'Airport', 'Spot', 'Spot', 'Spot', 'Spot', 'Spot', 'Spot', 'Spot', 'Landmark', 'Landmark', 'Island', 'Recommend', 'Recommend', 'Recommend', 'Bar', 'Bar', 'Event']
})

# --- 6. 主頁面邏輯 ---

if page == "📅 行程總覽":
    # 使用 HTML/CSS 插入背景圖片與標題
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
            st.info("👋 歡迎！請先辦理入境、領行李，搭乘計程車/地鐵前往 **JEN Tanglin 飯店** 辦理入住，放下行李輕裝出發！")

        render_spot_card(
            "15:30 - 17:00", "中峇魯 (Tiong Bahru)",
            "中峇魯是新加坡最迷人且歷史悠久的住宅區之一，完美融合了豐富的歷史底蘊與現代文青氣息。您可以漫步在 1930 年代由英國殖民政府建造的「裝飾藝術風格（Art Deco）」老組屋之間，欣賞其標誌性的螺旋樓梯、圓弧形陽台與白色外牆。這個街區充滿了故事，務必尋找由知名藝術家葉耀宗繪製的懷舊壁畫，如描繪昔日居民生活的《巴剎與算命佬》或《鳥語花香》，彷彿穿越時空。此外，巷弄間隱藏著許多獨立書店（如 Woods in the Books）與精品咖啡館，是感受新加坡慢活步調的最佳地點。",
            food=["中峇魯水粿 (Jian Bo Shui Kueh)", "Tiong Bahru Bakery 可頌", "Loo's Hainanese Curry Rice"],
            tips="壁畫散佈在不同巷弄，建議先在 Google Maps 標記好『Tiong Bahru Murals』的位置，以免迷路。",
            details="""
            **🚇 交通指南：**
            搭乘地鐵東西線 (Green Line) 至 **Tiong Bahru (EW17)** 站，從 **A 出口**出站後，步行約 8-10 分鐘即可抵達中峇魯市場與主要街區。
            
            **📸 必拍重點與路線：**
            1.  **中峇魯市場 (Tiong Bahru Market)**：二樓熟食中心是美食天堂，一定要試試這裡的水粿。
            2.  **壁畫巡禮**：從 Seng Poh Lane 開始，尋找那些藏在角落的壁畫。
            3.  **特色建築**：欣賞 Tiong Poh Road 一帶的低層組屋建築群，非常適合人像攝影。
            """
        )
        render_spot_card(
            "17:00 - 18:30", "福康寧公園 (Fort Canning Park)",
            "這座鬱鬱蔥蔥的山丘見證了新加坡數百年的歷史變遷，從馬來皇族的禁地到英國殖民時期的軍事指揮中心。雖然這裡歷史悠久，但現在最吸引年輕人的熱門打卡點是位於公園邊緣的「螺旋階梯（Tree Tunnel）」。站在深邃的階梯底部由下往上仰拍，茂密的綠色藤蔓與藍天在井口形成強烈對比，如同通往秘境的天井，充滿神祕感與生命力，是 Instagram 上爆紅的必拍景點。",
            tips="螺旋階梯通常需要排隊拍照，建議預留一些時間。若遇下雨階梯可能濕滑，請小心行走。",
            details="""
            **🚇 交通指南 (最快路徑)：**
            搭乘地鐵至 **Dhoby Ghaut (NS24/NE6/CC1)** 站，從 **B 出口**出站後，往 Penang Road 方向走，過馬路後會看到一個地下道入口，走進去即可直接抵達螺旋階梯底部。
            
            **💡 遊玩建議：**
            拍完照後，可以順著階梯往上走，散步到山頂的 Fort Canning Centre 或 Sang Nila Utama Garden（仿古爪哇風格花園），再從 Clarke Quay 的方向下山，剛好銜接晚餐行程。
            """
        )
        render_spot_card(
            "18:30 - 22:00", "克拉碼頭 (Clarke Quay) 晚餐與夜遊",
            "新加坡河畔最閃耀的夜生活樞紐，昔日繁忙的舊倉庫與駁船碼頭，如今已改建成色彩繽紛的餐廳、酒吧與俱樂部。當夜幕低降，河岸兩旁的霓虹燈亮起，氣氛變得浪漫又熱鬧。晚餐後，您可以沿著新加坡河漫步，感受涼爽的晚風，欣賞河面倒映的城市燈火，或是看著遠處金沙酒店的雷射光束。這裡匯集了各國美食與現場音樂表演，是放鬆身心的絕佳去處。",
            food=["珍寶海鮮 (Jumbo Seafood) 辣椒螃蟹", "松發肉骨茶 (河畔店)"],
            tips="若要吃珍寶海鮮，強烈建議提前 1-2 週線上訂位，以免現場久候。辣椒螃蟹價格較高（秤重計價），但醬汁配炸饅頭絕對值得一試。",
            details="""
            **🚇 交通指南：**
            從福康寧公園步行約 10 分鐘即可抵達，或搭乘地鐵至 **Clarke Quay (NE5)** 站，C 出口即是。
            
            **🚶 散步路線與活動：**
            建議沿著河畔走，可以一路看到舊禧街警察局（彩虹窗戶建築）、新聞及藝術部大廈。
            若有興致，可現場買票搭乘 **Singapore River Cruise** 復古觀光遊船（約 40 分鐘，票價約 SGD 28），從水上視角遊覽這座城市，非常浪漫。
            """
        )

    with day_tab2:
        st.markdown('<div class="day-header">1/17 (六) 歷史、色彩與美食中心</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 12:30", "小印度 (Little India)",
            "一踏入這裡，視覺與嗅覺將瞬間被強烈喚醒！空氣中飄散著濃郁的咖哩、香料與茉莉花環的香氣，建築外牆被漆成大膽鮮豔的色彩。您可以參觀「維拉馬卡里亞曼興都廟」，欣賞塔樓上繁複且色彩斑斕的神像雕刻，感受印度教的莊嚴與熱鬧。別忘了去「陳東齡故居」拍下那棟色彩繽紛、如同糖果屋般的別墅，它是小印度最經典的打卡地標，展現了華人富商與歐洲建築風格的有趣融合。",
            food=["竹腳中心 (Tekka Centre) 印度甩餅 (Roti Prata)", "拉茶 (Teh Tarik)", "Briyani 薑黃飯"],
            tips="進入印度廟宇必須脫鞋，建議當天穿著方便穿脫的鞋子。竹腳中心一樓是美食街，地板可能較濕滑，行走請小心。",
            details="""
            **🚇 交通指南：**
            搭乘地鐵東北線或濱海市區線至 **Little India (NE7/DT12)** 站，**E 出口**出來就是竹腳中心。
            
            **🗺️ 路線建議：**
            竹腳中心吃道地早餐 ➔ 逛逛水牛路 (Buffalo Rd) 看賣花與蔬菜的攤販 ➔ 步行至陳東齡故居 (彩色別墅) 拍照 ➔ 參觀維拉馬卡里亞曼興都廟 ➔ 逛逛 Little India Arcade 挑選印度風紀念品。
            """
        )
        render_spot_card(
            "12:30 - 17:30", "甘榜格南 (Kampong Glam) & 哈芝巷",
            "這裡是新加坡的馬來與穆斯林文化核心。宏偉的金頂「蘇丹回教堂」是必訪地標，其巨大的金色圓頂在陽光下閃閃發光。參觀完嚴肅的宗教建築後，轉個彎進入旁邊的「哈芝巷 (Haji Lane)」，氣氛瞬間轉變為年輕潮流。這裡是新加坡最窄的街道之一，牆上滿是藝術家的大型塗鴉創作，兩旁林立著個性小店、獨立設計師品牌與時尚酒吧，是挖寶與街拍的絕佳去處。",
            food=["Zam Zam 印度煎餅 (Murtabak)", "白蘭閣街蝦麵", "土耳其料理"],
            tips="哈芝巷的許多店鋪下午才會開門，午後前往最為熱鬧。蘇丹回教堂中午有午休時間不開放參觀，若要入內請避開禮拜時間並注意服裝儀容。",
            details="""
            **🚇 交通指南：**
            搭乘地鐵至 **Bugis (EW12/DT14)** 站，**B 出口**出站後，沿著 Victoria Street 步行約 5-8 分鐘。
            
            **📸 拍照點：**
            1.  **蘇丹回教堂**：必拍金色圓頂，最佳拍攝點是在正對面的 Bussorah Street 步行街上。
            2.  **哈芝巷**：整條街都是壁畫，非常有個性，適合幫媽媽拍網美照。
            3.  **阿拉伯街 (Arab Street)**：販售各種精美的布料、地毯與香水瓶，充滿異國風情。
            """
        )
        render_spot_card(
            "17:30 - 22:00", "牛車水 (Chinatown) & 麥士威熟食中心",
            "這裡是新加坡早期華人移民的聚集地，保留了濃厚的歷史氛圍。您可以參觀莊嚴宏偉的「佛牙寺龍華院」，其建築風格融合了唐代與曼陀羅元素，內部金碧輝煌。令人驚訝的是，僅一街之隔就是新加坡最古老的印度教廟宇「馬里安曼興都廟」，展現了新加坡不同宗教的和諧共處。晚上街道上的紅燈籠亮起，充滿濃厚的東方風情，是體驗華人文化與美食的絕佳地點。",
            food=["麥士威熟食中心 (天天海南雞飯)", "林志源肉乾", "老伴豆花"],
            tips="天天海南雞飯通常大排長龍，若不想排隊，旁邊的「阿仔海南雞飯」據說是前主廚出來開的，口味也相當棒。",
            details="""
            **🚇 交通指南：**
            搭乘地鐵至 **Maxwell (TE18)** 站（一出來就是麥士威熟食中心）或 **Chinatown (NE4/DT19)** 站。
            
            **🙏 參觀重點：**
            * **佛牙寺**：入內需穿著得體（短褲短裙需在門口借圍龍），可以搭電梯到頂樓參觀空中花園和巨大的轉經輪。
            * **馬里安曼興都廟**：塔門上有色彩鮮豔的神像雕刻，非常壯觀。
            * **牛車水美食街**：史密斯街 (Smith St) 晚上有許多露天餐飲攤位。
            """
        )

    with day_tab3:
        st.markdown('<div class="day-header">1/18 (日) 濱海灣核心與超級樹 (🔥雙秀+藝術節)</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 12:00", "新加坡植物園 (Botanic Gardens)",
            "這是新加坡唯一被列入 UNESCO 世界文化遺產的景點，擁有超過 160 年的歷史。這裡不像一般的城市公園，更像是一座巨大的熱帶森林，環境清幽雅致。重點遊覽需購票的「國家蘭花園」，這裡種植了超過 1000 個原種和 2000 個雜交種的蘭花，色彩斑斕，美不勝收，是與媽媽散步拍照的優雅首選，也是新加坡國花「卓錦·萬代蘭」的展示地。",
            tips="新加坡天氣炎熱，建議早上前往較為涼爽。園區很大，請穿著舒適好走的鞋子，並攜帶防蚊液。",
            details="""
            **🚇 交通指南：**
            搭乘地鐵環狀線或濱海市區線至 **Botanic Gardens (CC19/DT9)** 站，一出站就是植物園的 Bukit Timah Gate 大門。
            
            **🌸 國家蘭花園 (National Orchid Garden)：**
            這是園區內唯一需要收費的地方（成人約 SGD 15，長者有優惠），但非常值得。裡面有空調冷室館 (Cool House)，是模擬高山氣候的區域，避暑賞花兩相宜。
            """
        )
        render_spot_card(
            "12:00 - 17:30", "濱海灣地標巡禮 & 老巴剎午餐",
            "前往市中心核心地帶，一次收集新加坡最經典的地標。首先與著名的「魚尾獅」拍照接水求財，接著步行經過充滿科技感與DNA造型設計的「螺旋橋」，遠眺外型像大榴槤的「濱海藝術中心」。午餐安排在「老巴剎 (Lau Pa Sat)」，這是一座建於 19 世紀的維多利亞時期鑄鐵建築，在金融區摩天大樓的包圍下吃著道地路邊攤，有一種時空交錯的獨特美感。",
            food=["老巴剎沙嗲串燒", "福建炒麵", "雷茶飯"],
            details="""
            **🚇 交通指南：**
            搭乘地鐵至 **Raffles Place (EW14/NS26)** 站，**F 出口**步行約 5 分鐘可達老巴剎。吃完後步行約 10 分鐘可達魚尾獅公園。
            
            **🚶 散步路線：**
            老巴剎午餐 ➔ 魚尾獅公園 (Merlion Park) ➔ 走過朱比利橋 (Jubilee Bridge) ➔ 濱海藝術中心 (大榴槤) ➔ 雙螺旋橋 (Helix Bridge) ➔ 抵達濱海灣金沙購物中心。這條路線沿途風景極佳，非常適合拍照。
            """
        )
        render_spot_card(
            "17:30 - 21:15", "濱海灣花園 (Gardens by the Bay) & 雙秀連發",
            "這是新加坡的重頭戲，將「花園城市」的概念發揮到極致。先參觀兩大冷室：「雲霧林」擁有一座 35 公尺高的室內人造山與世界最高的室內瀑布，雲霧繚繞極為壯觀；「花穹」則展示了世界各地的奇花異草，四季如春。晚上最不能錯過的是躺在巨大的「超級樹」下，欣賞每晚兩場的聲光秀 (Garden Rhapsody)，隨著磅礡的音樂與燈光閃爍，彷彿置身阿凡達電影場景，震撼感十足。",
            food=["Satay by the Bay (園區內熟食中心)", "Shake Shack"],
            tips="必看攻略：先看 19:45 超級樹，再走去金沙廣場看 21:00 水舞秀。",
            details="""
            **🚇 交通指南：**
            搭乘地鐵至 **Bayfront (CE1/DT16)** 站，**B 出口**跟著指示牌走地下道即可抵達濱海灣花園入口。
            
            **🌟 雙秀完美攻略 (Time Table)：**
            1. **19:45**：在 Supertree Grove 躺著看 **Garden Rhapsody 燈光秀** (15分鐘)。
            2. **20:00**：秀結束後，走 Dragonfly Bridge (蜻蜓橋) 穿過金沙酒店，前往戶外活動廣場 (Event Plaza)。步行約 15-20 分鐘。
            3. **20:30 或 21:00**：在金沙廣場看 **Spectra 水舞秀** (15分鐘)，有雷射與噴泉。
            """
        )
        render_spot_card(
            "21:15 - 22:30", "🌟 晝夜璀璨藝術節 (Light to Night 2026)",
            "您非常幸運！這段期間剛好是新加坡一年一度的「Light to Night」藝術節。就在水舞秀對岸的市政區，國家美術館和維多利亞劇院的外牆會變成巨大的畫布，投射出震撼的光雕秀 (Projection Mapping)，草地上也有許多發光的裝置藝術，是年輕人最愛的夜間活動，而且完全免費！",
            food=["Art X Social 節慶市集小吃"],
            tips="看完水舞秀後，過個橋（Jubilee Bridge）走去 Padang 草地就可以看到了。",
            details="""
            **🚇 交通指南：**
            從金沙廣場走過 Jubilee Bridge (朱比利橋) 即可抵達市政區 (Civic District)。
            
            **📸 必拍亮點：**
            1. **National Gallery 外牆光雕**：最壯觀的主秀。
            2. **Padang 草地**：大型發光充氣裝置。
            3. **Victoria Theatre**：古典建築與現代投影的結合。
            """
        )

    with day_tab4:
        st.markdown('<div class="day-header">1/19 (一) 海島放鬆與購物</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 13:00", "聖淘沙 (Sentosa) 上午",
            "搭乘花柏山纜車入島，這是一個絕佳的體驗，能從高空俯瞰繁忙的港口、郵輪與美麗的海岸線。下島後避開人潮，直奔「丹戎海灘 (Tanjong Beach)」，這裡是聖淘沙最寧靜、最有度假感的海灘，遠離了環球影城的喧囂。您可以赤腳踩在細軟的沙灘上，或是找個樹蔭下休息，享受海島的慵懶時光。",
            tips="纜車票建議事先在 Klook 或 KKday 購買，價格通常比現場便宜，且可直接掃碼入場。",
            details="""
            **🚇 交通指南：**
            搭乘地鐵至 **HarbourFront (NE1/CC29)** 站。走到 VivoCity 怡豐城 3 樓搭乘 Sentosa Express (輕軌) 或依照指示步行至 Harbourfront Tower 2 搭乘纜車。
            
            **🏖️ 海灘交通：**
            入島後，可搭乘免費的聖淘沙海灘火車 (Beach Shuttle) 前往 Tanjong Beach，這是最後一站，所以人最少最安靜。
            """
        )
        render_spot_card(
            "13:00 - 18:00", "度假體驗 & SkyHelix",
            "體驗聖淘沙最新的景點「SkyHelix 空中喜立」，這是一個露天的全景熱氣球式設施，雙腳懸空喝著飲料，緩緩旋轉上升到 79 公尺高空，360 度無死角欣賞聖淘沙全景與南部島嶼。下午找間氣氛好的海灘俱樂部 (Beach Club)，點杯冰涼的調酒或椰子水，享受真正的度假模式。",
            food=["海灘俱樂部輕食/飲料", "Coastes 餐廳"],
            details="""
            **SkyHelix：**
            這是一個露天的旋轉觀景台，票價通常包含一杯非酒精飲料。因為雙腳懸空，請務必把手機拿好或使用掛繩。
            
            **🍹 推薦休息點：**
            **Tanjong Beach Club** 是當地最紅的俱樂部，氣氛慵懶，很適合點杯飲料躺在沙發床上休息。若喜歡熱鬧一點，Siloso Beach 附近的 **Rumours Beach Club** 也是不錯的選擇。
            """
        )
        render_spot_card(
            "18:00 - 22:00", "烏節路 (Orchard Road) 逛街",
            "傍晚回到飯店附近的烏節路（Orchard Road），這裡是新加坡的購物天堂，整條街百貨林立。**JEN Tanglin** 飯店直通 **Tanglin Mall**，旁邊就是 **ION Orchard** 等大型商場。除了逛街，別忘了前往位於商場內的「烏節圖書館」，其波浪形的書架設計充滿現代設計感，是文青必訪之地。晚餐享用新加坡著名的肉骨茶，濃郁的胡椒湯頭能驅散一天的疲憊。",
            food=["松發肉骨茶 (Song Fa)", "亞坤咖椰吐司", "麵包夾冰淇淋 (路邊攤)"],
            tips="松發肉骨茶的湯可以無限續加，服務員會提著茶壺巡視，記得多喝幾碗暖胃！",
            details="""
            **📚 烏節圖書館：**
            位於 **Orchard Gateway** 商場的 3 樓和 4 樓。設計非常現代，波浪書架是必拍重點，但請保持安靜，不要打擾閱讀的人。
            
            **🛍️ 購物建議：**
            * **Tanglin Mall**：就在飯店樓下，適合逛超市、生活雜貨。
            * **ION Orchard**：國際大牌齊全，地下室美食街選擇多。
            * **Paragon**：精品為主，環境優雅。
            * **Don Don Donki**：位於 Orchard Central，採買日本零食的好地方。
            """
        )

    with day_tab5:
        st.markdown('<div class="day-header">1/20 (二) 採買、高空觀景與告別</div>', unsafe_allow_html=True)
        render_spot_card(
            "09:00 - 11:00", "金沙空中花園 (Sands SkyPark)",
            "在離開前，登上金沙酒店頂樓的觀景台。從 57 層的高空俯瞰整個濱海灣、新加坡海峽，還有昨天去過的超級樹與植物園，將這座城市的美景盡收眼底，為旅程留下最壯闊的記憶。船型的建築結構本身就是世界工程奇蹟。",
            tips="早上人潮較少，且早晨的光線柔和，非常適合拍出清透的城市景觀照。",
            details="""
            **🚇 交通指南：**
            搭乘地鐵至 **Bayfront (CE1/DT16)** 站，從金沙酒店 3 號塔樓 (Tower 3) 外部入口進入售票處與電梯。
            
            **📸 拍照技巧：**
            觀景台最前端的角角是拍攝濱海灣全景的最佳位置，可以把整個灣區都拍進去。
            """
        )
        render_spot_card(
            "11:00 - 12:30", "武吉士 (Bugis) 最後採買",
            "前往「武吉士街 (Bugis Street)」，這裡是平價伴手禮的天堂，有點像是有冷氣的迷宮夜市。您可以在此買齊要送給親友的紀念品（如魚尾獅巧克力、鑰匙圈、班蘭蛋糕等）。午餐在附近享用道地美食，確保離開前沒有遺憾。",
            food=["亮耀海南雞飯", "Zam Zam 印度煎餅", "阿秋甜品"],
            tips="武吉士街人多擁擠，採買時請注意隨身財物。許多店家可以講價。",
            details="""
            **🚇 交通指南：**
            搭乘地鐵至 **Bugis (EW12/DT14)** 站，過個馬路就到 Bugis Street。
            
            **🎁 伴手禮建議：**
            魚尾獅造型巧克力、班蘭蛋糕 (Bengawan Solo)、鹹蛋魚皮 (Irvins)、百勝廚叻沙泡麵、Kaya 醬。
            """
        )
        render_spot_card(
            "12:30 - 14:25", "前往機場 & 星耀樟宜 (Jewel)",
            "回 **JEN Tanglin** 取行李前往機場。務必預留時間去機場旁的「星耀樟宜 (Jewel Changi)」，觀賞世界最大的室內瀑布「雨漩渦 (Rain Vortex)」。看著水流從 40 公尺高空傾瀉而下，搭配周圍的森林谷，震撼人心，是新加坡送給旅客最後的驚喜。",
            tips="瀑布位於 T1 航廈前方，若您的班機在 T3 報到，可以搭乘機場電車前往觀賞。",
            details="""
            **🚇 交通指南：**
            從飯店搭計程車/Grab 到機場約 25-30 分鐘，費用約 SGD 25-35。
            或是搭乘地鐵從 **Orchard Boulevard (TE13)** 轉乘至機場（時間較長，約 1 小時 15 分）。
            
            **💦 雨漩渦 (Rain Vortex)：**
            位於 Jewel (星耀樟宜) 的正中央，不需要出境就可以看到。建議先去 T3 華航櫃台寄放行李（若櫃台已開），再輕裝去 Jewel 逛逛。Jewel 與 T1/T2/T3 都有連通道。
            """
        )

# --- NEW: 必買伴手禮清單 ---
elif page == "🛍️ 必買伴手禮清單":
    st.markdown('<div class="main-header">🛍️ 新加坡 5 大必買名產</div>', unsafe_allow_html=True)
    st.info("這裡幫您整理了最受歡迎、最值得買回台灣送禮或自用的商品！")

    render_spot_card(
        "1. 綠蛋糕 (Pandan Cake)",
        "Bengawan Solo",
        "用班蘭葉汁做的戚風蛋糕，口感超綿密，帶有淡淡的椰香和植物清香，是新加坡最代表性的伴手禮。",
        food=["綠蛋糕 (戚風)", "娘惹糕 (Kueh)"],
        tips="強烈建議在樟宜機場買，因為蛋糕需要保鮮，上飛機前買剛剛好，不用提著跑行程。",
        details="**📍 購買地點：** 樟宜機場 T1/T2/T3/T4 管制區內外都有分店。"
    )

    render_spot_card(
        "2. 鹹蛋魚皮",
        "IRVINS / The Golden Duck",
        "炸得酥脆的魚皮裹上濃郁的鹹蛋黃醬，超級涮嘴（也很罪惡）。IRVINS 是最紅的牌子，包裝上有隻黑鴨子。",
        tips="除了原味，辣味也非常受歡迎！",
        details="**📍 購買地點：** VivoCity (去聖淘沙那天會經過)、機場、各大超市。"
    )

    render_spot_card(
        "3. 咖椰醬 (Kaya Jam)",
        "Ya Kun / Toast Box / Glory",
        "新加坡國民早餐的靈魂，甜甜的椰奶雞蛋醬，抹在烤吐司上加奶油超好吃。",
        tips="如果不想提太重，超市賣的 Glory 牌（玻璃罐裝）便宜又好吃。",
        details="**📍 購買地點：** 飯店樓下的 Toast Box、亞坤門市、FairPrice 超市。"
    )

    render_spot_card(
        "4. 百勝廚叻沙拉麵 (Prima Taste)",
        "世界第一泡麵",
        "曾被評為全球最好吃的泡麵。湯頭非常濃郁，不是粉包而是醬包，還原度極高。",
        tips="記得買「Laksa (叻沙)」口味，黑色包裝。",
        details="**📍 購買地點：** 任何超市 (FairPrice / Cold Storage) 都買得到，比機場便宜。"
    )

    render_spot_card(
        "5. 小 CK (Charles & Keith)",
        "平價精品包",
        "新加坡本土品牌，價格比台灣便宜約 10-20%，而且款式更新、更齊全。",
        tips="滿 SGD 100 可以退稅！",
        details="**📍 購買地點：** ION Orchard (Day 5 行程)、VivoCity、機場免稅店。"
    )

# --- 夜生活分頁 ---
elif page == "🍷 飯店周邊夜生活":
    st.markdown('<div class="main-header">🍷 飯店周邊微醺推薦</div>', unsafe_allow_html=True)
    st.info("這裡精選了 **JEN Tanglin** 附近的優質酒吧，適合帶媽媽去體驗一下新加坡的夜晚氛圍，安全又放鬆。")

    render_spot_card(
        "Manhattan Bar (曼哈頓酒吧)",
        "世界級的奢華享受",
        "位於附近的 Conrad Singapore Orchard 飯店內（步行約 5-8 分鐘），曾多次獲選「亞洲 50 大酒吧」。裝潢走精緻的紐約復古風，氣氛優雅。",
        food=["免費佐酒小點心", "招牌調酒"],
        details="**📍 地點：** Conrad Singapore Orchard 2樓。\n**💡 建議：** 穿著稍微正式一點（避免拖鞋短褲）。"
    )

    render_spot_card(
        "Dempsey Hill (登布西山)",
        "森林裡的異國浪漫",
        "離飯店非常近（搭計程車約 5 分鐘）。這裡是舊軍營改建的餐飲區，環境綠意盎然。推薦 **PS.Cafe** 或 **The Dempsey Cookhouse & Bar**。",
        food=["松露薯條", "精釀啤酒"],
        details="**📍 地點：** Dempsey Road。\n**💡 交通：** 建議直接請飯店幫忙叫車前往。"
    )

    render_spot_card(
        "Hard Rock Cafe",
        "經典美式搖滾",
        "就在您飯店隔壁的 Cuscaden Road 上！有現場樂團演奏 (Live Band)，非常放鬆。",
        food=["美式漢堡", "雞尾酒"],
        details="**📍 地點：** 50 Cuscaden Road (就在飯店旁邊)。"
    )

# --- 其他熱門推薦 (Plan B) ---
elif page == "🌟 其他熱門推薦":
    st.markdown('<div class="main-header">🌟 沒去會後悔？備選行程推薦</div>', unsafe_allow_html=True)
    st.info("如果您還有體力，或者想替換掉原本行程中的某個點，這裡有 3 個非常適合拍照、氛圍也很棒的推薦去處！")

    render_spot_card(
        "推薦 1：如切/加東 (Joo Chiat / Katong)",
        "彩色娘惹屋與道地叻沙",
        "新加坡色彩最繽紛的街區！這裡有整排保留完整的「Peranakan Houses (娘惹排屋)」，粉紅、粉綠、粉藍的精緻建築立面，配上精美的磁磚。",
        food=["328 加東叻沙", "金珠肉粽"],
        details="**🚇 交通指南：** 建議搭 Grab 前往，定位在 **Koon Seng Road**。"
    )

    render_spot_card(
        "推薦 2：讚美廣場 (CHIJMES)",
        "夢幻白教堂與露天酒吧",
        "位於市中心，前身是一座古老的修道院。純白色的哥德式教堂非常浪漫（電影《瘋狂亞洲富豪》婚禮拍攝地）。",
        food=["Prive", "各式 Tapas"],
        details="**🚇 交通指南：** 搭乘地鐵至 **City Hall** 站，步行 5 分鐘。"
    )

    render_spot_card(
        "推薦 3：舊禧街警察局",
        "彩虹窗戶大樓",
        "這棟建築擁有 927 扇窗戶，被漆成彩虹般的漸層色，非常吸睛。它其實就在克拉碼頭和福康寧公園旁邊，是順路打卡 CP 值最高的景點。",
        details="**🚇 交通指南：** 就在 **Clarke Quay** 地鐵站旁。"
    )

elif page == "🗺️ 地圖導航":
    st.markdown('<div class="main-header">🗺️ 行程景點地圖</div>', unsafe_allow_html=True)
    st.markdown("包含：飯店、機場、濱海灣、聖淘沙及各大文化區，紅點代表您將造訪的地點。")
    
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
    
    # 渲染地圖
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
    
    st.markdown("### 🍳 早餐特別推薦 (飯店附近)")
    st.info("""
    * **Toast Box (Tanglin Mall)**：最方便！就在飯店樓下商場，吃 Kaya 吐司套餐。
    * **Killiney Kopitiam**：最經典！去 Lucky Plaza 或 Killiney Road 本店體驗老字號。
    * **Nassim Hill Bakery**：氣氛棒！在古蹟郵局裡吃西式早午餐。
    """)

# --- 行前清單 (詳細版) ---
elif page == "✅ 出國當天備忘錄 (詳細版)":
    st.markdown('<div class="main-header">✅ 出國當天備忘錄 (懶人包)</div>', unsafe_allow_html=True)
    
    # 1. 必備文件與入境
    st.markdown("### 🛂 1. 必備文件與入境 (最重要！)")
    with st.expander("📄 護照、電子入境卡 (ICA)、網卡攻略", expanded=True):
        st.markdown("""
        * **護照**：
            * 請再次確認護照效期還有 **6 個月以上**。
            * 建議拍一張護照內頁照片存手機備用。
        * **SG Arrival Card (電子入境卡)**：
            * **必填！** 出發前 **3 天內** (含當天) 上網填寫。
            * **免費**，請勿找代辦。建議下載官方 APP **MyICA Mobile** 填寫，可掃描護照自動帶入資料。
            * 填寫完會有 Email 確認信，入境時不需要印出來，新加坡海關系統會自動抓到資料。
        * **機票與飯店憑證**：
            * 建議將電子機票和 Agoda/Booking 訂房憑證截圖存在手機，或印出一份紙本備用 (海關偶爾會抽問)。
        * **網卡/漫遊**：
            * **Sim 卡 / eSIM**：建議在台灣先買好 (Klook/KKday)，到樟宜機場領取或掃描 QR Code 開通。
            * **漫遊**：若用電信漫遊，記得出發前向電信公司申請開通。
        """)

    # 2. 金錢與支付
    st.markdown("### 💰 2. 金錢與支付")
    with st.expander("💵 現金要帶多少？卡要帶哪張？", expanded=True):
        st.markdown("""
        * **現金建議**：
            * 每人準備 **SGD 150 - 200** (約 NT$ 3,600 - 4,800) 現金即可。
            * **用途**：主要用於熟食中心 (Hawker Centre)、傳統雜貨店、部分只能付現的計程車。
            * **小撇步**：去銀行換錢時，請行員盡量給 **10元、50元** 小面額，1000元大鈔很多店家找不開。
        * **信用卡 (Visa / Mastercard)**：
            * 帶 **2 張** 海外回饋高 (大於 1.5%) 的卡。
            * **交通神卡**：新加坡 **地鐵 (MRT) 和 公車** 可以直接刷台灣的信用卡 (感應式)，**不需要買 EZ-Link 卡**！(注意：每人要用一張實體卡或手機感應，不能兩人共用一張)。
            * 百貨公司、超市、超商、餐廳幾乎都可刷卡。
        * **行動支付**：Apple Pay / Google Pay 在當地非常普及。
        """)

    # 3. 衣物與穿搭
    st.markdown("### 👕 3. 衣物與穿搭 (溫差大注意！)")
    with st.expander("☀️ 室外像烤箱，室內像冰箱"):
        st.markdown("""
        * **天氣概況**：新加坡全年夏天 (28-32度)，非常悶熱潮濕，且常有午後雷陣雨。
        * **戶外穿著**：
            * 短袖、短褲、裙子、透氣材質 (棉麻/排汗衫)。
            * 顏色鮮豔的衣服拍照比較好看！
        * **室內穿著 (非常重要！)**：
            * **一定要帶薄外套**！新加坡的地鐵、百貨公司、電影院冷氣開超強，沒帶外套真的會感冒。
        * **鞋子**：
            * **好走的球鞋/休閒鞋**：這幾天日行萬步是基本，千萬不要穿新鞋或咬腳的鞋。
            * **拖鞋/涼鞋**：去聖淘沙海灘玩水，或下大雨時穿。
        * **雨具**：必備 **輕便摺疊傘** (遮陽+擋雨) 或輕便雨衣。
        """)

    # 4. 電子產品與轉接頭
    st.markdown("### 🔌 4. 電子產品")
    with st.expander("⚡ 電壓、插座、充電"):
        st.markdown("""
        * **轉接頭**：**英式三腳方形 (Type G)**。台灣的插頭插不進去，一定要帶轉接頭！
        * **電壓**：新加坡是 230V。現在的手機、筆電、相機充電器通常是 100-240V 通用電壓，所以**不需要變壓器**，只要轉接頭即可。(吹風機若非國際電壓則不可用)。
        * **行動電源**：自由行整天開地圖、拍照，電量消耗快，必備 1-2 顆 (記得放隨身行李上飛機，不能託運)。
        * **充電線**：多帶一條備用。
        """)

    # 5. 生活小物
    st.markdown("### 🧴 5. 生活小物 (提升旅遊品質)")
    with st.expander("💊 藥品、衛生紙、防曬"):
        st.markdown("""
        * **面紙/濕紙巾**：新加坡的熟食中心通常**不提供衛生紙**，一定要隨身攜帶！也可以拿來佔位子 (Chope 文化)。
        * **個人藥品**：
            * 胃藥、止痛藥、暈車藥 (去聖淘沙搭車可能用到)、OK繃 (防磨腳)。
            * 個人慢性病藥物記得帶足量。
        * **防曬用品**：太陽眼鏡、帽子、防曬乳 (紫外線很強)。
        * **水壺**：新加坡水龍頭的水煮沸後可喝，帶水壺出門可以省錢 (超商瓶裝水較貴)。
        * **環保袋**：超市購物通常不給免費塑膠袋。
        """)

    # 6. APP 下載推薦
    st.markdown("### 📱 6. 推薦下載 APP")
    with st.expander("🚖 交通與地圖"):
        st.markdown("""
        * **Grab**：東南亞的 Uber，叫車必備 (建議在台灣先下載並綁定信用卡)。
        * **Google Maps**：找路、查公車時間最準。
        * **MyICA Mobile**：填寫電子入境卡用。
        """)

    st.success("祝您和媽媽旅途愉快！ Have a nice trip! ✈️")
