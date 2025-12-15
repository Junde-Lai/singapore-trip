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
# 這裡定義了卡片、標題、標籤的樣式，讓介面看起來像旅遊網站
st.markdown("""
<style>
    /* 全局字體優化 */
    .stApp {
        font-family: "Microsoft JhengHei", "PingFang TC", sans-serif;
    }
    
    /* 主標題樣式 */
    .main-header {
        font-size: 36px; 
        font-weight: 800; 
        color: #2C3E50;
        text-align: center;
        margin-bottom: 30px;
        letter-spacing: 2px;
        text-shadow: 2px 2px 4px #eee;
    }
    
    /* 日期分頁標題 */
    .day-header {
        font-size: 24px;
        font-weight: bold;
        color: #E74C3C;
        border-bottom: 2px solid #E74C3C;
        padding-bottom: 10px;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* 景點卡片設計 */
    .spot-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 25px;
        border-left: 5px solid #3498DB;
        transition: transform 0.2s;
    }
    .spot-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px rgba(0,0,0,0.1);
    }

    /* 卡片內標題 */
    .spot-title {
        font-size: 20px;
        font-weight: bold;
        color: #2980B9;
        margin-bottom: 10px;
    }

    /* 卡片內文 */
    .spot-desc {
        font-size: 16px;
        line-height: 1.6;
        color: #555;
        text-align: justify;
    }

    /* 美食標籤 */
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

    /* 小貼士區塊 */
    .info-box {
        background-color: #ECF0F1;
        padding: 10px;
        border-radius: 8px;
        font-size: 14px;
        color: #7F8C8D;
        margin-top: 10px;
        border-left: 3px solid #BDC3C7;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. 側邊欄：基本資訊 ---
with st.sidebar:
    # 使用您指定的特定圖片連結
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
# 這是一個小工具，用來生成漂亮的 HTML 卡片
def render_spot_card(time, title, desc, food=None, tips=None):
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

# --- 5. 地標數據 (地圖用) ---
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

    # --- Day 1 ---
    with day_tab1:
        st.markdown('<div class="day-header">1/16 (五) 抵達、文創區與河畔夜景</div>', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        with col1:
             st.metric("抵達時間", "13:05", "T3 航廈")
        with col2:
            st.info("👋 歡迎！請先辦理入境、領行李，搭乘計程車/地鐵前往 YOTEL 辦理入住，放下行李輕裝出發！")

        render_spot_card(
            "15:30 - 17:00", "中峇魯 (Tiong Bahru)",
            "這裡被譽為新加坡最迷人的社區之一，完美融合了豐富的歷史底蘊與現代文青氣息。您可以漫步在 1930 年代建造的「裝飾藝術風格（Art Deco）」老組屋之間，欣賞其獨特的弧形陽台與螺旋樓梯。務必尋找由藝術家葉耀宗繪製的懷舊壁畫，如描繪昔日居民生活的《巴剎與算命佬》。巷弄間隱藏著許多獨立書店（如 Woods in the Books）與精品咖啡館，是感受新加坡慢活步調的最佳地點。",
            food=["中峇魯水粿 (Jian Bo Shui Kueh)", "Tiong Bahru Bakery 可頌", "Loo's Hainanese Curry Rice"],
            tips="壁畫散佈在不同巷弄，建議先在 Google Maps 標記好『Tiong Bahru Murals』的位置，以免迷路。"
        )
        render_spot_card(
            "17:00 - 18:30", "福康寧公園 (Fort Canning Park)",
            "這座鬱鬱蔥蔥的山丘見證了新加坡的歷史變遷，從馬來皇族的禁地到英國殖民時期的軍事據點。現在最熱門的網美打卡點是位於公園邊緣的「螺旋階梯（Tree Tunnel）」。站在階梯底部由下往上拍攝，茂密的綠色藤蔓與藍天形成如同天井般的夢幻場景，充滿神祕感與生命力。",
            tips="螺旋階梯位於 Dhoby Ghaut 地鐵站附近入口，通常需要排隊拍照，建議預留一些時間。"
        )
        render_spot_card(
            "18:30 - 22:00", "克拉碼頭 (Clarke Quay) 晚餐與夜遊",
            "新加坡河畔的熱鬧樞紐，昔日的舊倉庫與駁船碼頭如今已改建成色彩繽紛的餐廳、酒吧與俱樂部。晚餐後，您可以沿著新加坡河漫步，感受涼爽的晚風，欣賞河面倒映的城市燈火。若有興趣，也可以搭乘復古的觀光遊船（Bumboat），從水上視角遊覽這座城市。",
            food=["珍寶海鮮 (Jumbo Seafood) 辣椒螃蟹", "松發肉骨茶 (河畔店)"],
            tips="若要吃珍寶海鮮，強烈建議提前線上訂位，以免現場久候。辣椒螃蟹價格較高，但絕對值得一試。"
        )

    # --- Day 2 ---
    with day_tab2:
        st.markdown('<div class="day-header">1/17 (六) 歷史、色彩與美食中心</div>', unsafe_allow_html=True)
        
        render_spot_card(
            "09:00 - 12:30", "小印度 (Little India)",
            "一踏入這裡，視覺與嗅覺將瞬間被喚醒！空氣中飄散著濃郁的咖哩與花環香氣，建築外牆被漆成大膽鮮豔的色彩。參觀「維拉馬卡里亞曼興都廟」，欣賞塔樓上繁複的神像雕刻。別忘了去「陳東齡故居」拍下那棟色彩繽紛、如同糖果屋般的別墅，是小印度最經典的打卡地標。",
            food=["竹腳中心 (Tekka Centre) 印度甩餅 (Roti Prata)", "拉茶 (Teh Tarik)", "Briyani 薑黃飯"],
            tips="進入印度廟宇需脫鞋，建議當天穿著方便穿脫的鞋子。竹腳中心地板可能較濕滑，行走請小心。"
        )
        render_spot_card(
            "12:30 - 17:30", "甘榜格南 (Kampong Glam) & 哈芝巷",
            "這裡是新加坡的馬來與穆斯林文化核心。宏偉的金頂「蘇丹回教堂」是必訪地標。參觀完嚴肅的宗教建築後，轉個彎進入旁邊的「哈芝巷 (Haji Lane)」，氣氛瞬間轉變為年輕潮流。這裡是新加坡最窄的街道之一，牆上滿是藝術家的塗鴉創作，兩旁林立著個性小店、獨立品牌與時尚酒吧，是挖寶與街拍的絕佳去處。",
            food=["Zam Zam 印度煎餅 (Murtabak)", "白蘭閣街蝦麵", "土耳其料理"],
            tips="哈芝巷的許多店鋪下午才會開門，午後前往最為熱鬧。蘇丹回教堂中午有午休時間不開放參觀，請留意時間。"
        )
        render_spot_card(
            "17:30 - 22:00", "牛車水 (Chinatown) & 麥士威熟食中心",
            "華人移民的歷史街區，展現了新加坡的多元融合。您可以參觀莊嚴宏偉的「佛牙寺龍華院」，令人驚訝的是，僅一街之隔就是印度教的「馬里安曼興都廟」，展現了不同宗教的和諧共處。晚上街道上的紅燈籠亮起，充滿濃厚的東方風情。",
            food=["麥士威熟食中心 (天天海南雞飯)", "林志源肉乾", "老伴豆花"],
            tips="天天海南雞飯通常大排長龍，若不想排隊，旁邊的「阿仔海南雞飯」據說是前主廚出來開的，口味也相當棒。"
        )

    # --- Day 3 ---
    with day_tab3:
        st.markdown('<div class="day-header">1/18 (日) 濱海灣核心與超級樹</div>', unsafe_allow_html=True)
        
        render_spot_card(
            "09:00 - 12:00", "新加坡植物園 (Botanic Gardens)",
            "這是新加坡唯一被列入 UNESCO 世界文化遺產的景點，擁有超過 160 年的歷史。這裡不像一般的公園，更像是一座巨大的熱帶森林。重點遊覽需購票的「國家蘭花園」，這裡種植了超過 1000 個原種和 2000 個雜交種的蘭花，色彩斑斕，美不勝收，是與媽媽散步拍照的優雅首選。",
            tips="新加坡天氣炎熱，建議早上前往較為涼爽。園區很大，請穿著舒適好走的鞋子，並攜帶防蚊液。"
        )
        render_spot_card(
            "12:00 - 17:30", "濱海灣地標巡禮 & 老巴剎午餐",
            "前往市中心核心地帶，與著名的「魚尾獅」拍照接水求財，接著步行經過充滿科技感與DNA造型設計的「螺旋橋」，遠眺外型像大榴槤的「濱海藝術中心」。午餐安排在「老巴剎 (Lau Pa Sat)」，這是一座維多利亞時期的鑄鐵建築，在金融摩天大樓包圍下吃著道地路邊攤，有一種時空交錯的獨特美感。",
            food=["老巴剎沙嗲串燒", "福建炒麵", "雷茶飯"]
        )
        render_spot_card(
            "17:30 - 22:00", "濱海灣花園 (Gardens by the Bay)",
            "這是新加坡的重頭戲，將「花園城市」的概念發揮到極致。先參觀兩大冷室：「雲霧林」擁有世界最高的室內瀑布，雲霧繚繞極為壯觀；「花穹」則展示了世界各地的奇花異草。晚上最不能錯過的是躺在巨大的「超級樹」下，欣賞每晚兩場的聲光秀 (Garden Rhapsody)，隨著音樂燈光閃爍，彷彿置身阿凡達電影場景。",
            food=["Satay by the Bay (園區內熟食中心)", "Shake Shack"],
            tips="超級樹燈光秀時間通常為 19:45 和 20:45 (免費)，建議提早 15 分鐘找個好位置席地而坐或躺著觀賞。"
        )

    # --- Day 4 ---
    with day_tab4:
        st.markdown('<div class="day-header">1/19 (一) 海島放鬆與購物</div>', unsafe_allow_html=True)
        
        render_spot_card(
            "09:00 - 13:00", "聖淘沙 (Sentosa) 上午",
            "搭乘纜車入島，從高空俯瞰繁忙的港口與美麗的海岸線。下島後直奔「丹戎海灘 (Tanjong Beach)」，這裡是聖淘沙最寧靜、最有度假感的海灘，遠離了環球影城的喧囂。您可以赤腳踩在細軟的沙灘上，或是找個樹蔭下休息，享受海島的慵懶時光。",
            tips="纜車票建議事先在 Klook 或 KKday 購買，價格通常比現場便宜，且可直接掃碼入場。"
        )
        render_spot_card(
            "13:00 - 18:00", "度假體驗 & SkyHelix",
            "體驗聖淘沙最新的景點「SkyHelix 空中喜立」，這是一個露天的全景熱氣球式設施，雙腳懸空喝著飲料，緩緩旋轉上升到 79 公尺高空，360 度無死角欣賞聖淘沙全景。下午找間氣氛好的海灘俱樂部 (Beach Club)，點杯冰涼的調酒或椰子水，享受真正的度假模式。",
            food=["海灘俱樂部輕食/飲料", "Coastes 餐廳"]
        )
        render_spot_card(
            "18:00 - 22:00", "烏節路 (Orchard Road) 回歸",
            "傍晚回到飯店所在的烏節路，這裡是購物天堂。除了逛逛各大百貨公司（如 ION, Paragon），別忘了前往位於商場內的「烏節圖書館」，其波浪形的書架設計充滿設計感，是文青必訪之地。晚餐享用新加坡著名的肉骨茶，濃郁的胡椒湯頭能驅散一天的疲憊。",
            food=["松發肉骨茶 (Song Fa)", "亞坤咖椰吐司", "麵包夾冰淇淋 (路邊攤)"],
            tips="松發肉骨茶的湯可以無限續加，服務員會提著茶壺巡視，記得多喝幾碗暖胃！"
        )

    # --- Day 5 ---
    with day_tab5:
        st.markdown('<div class="day-header">1/20 (二) 採買、高空觀景與告別</div>', unsafe_allow_html=True)
        
        render_spot_card(
            "09:00 - 11:00", "金沙空中花園 (Sands SkyPark)",
            "在離開前，登上金沙酒店頂樓的觀景台。從 57 層的高空俯瞰整個濱海灣、新加坡海峽，還有昨天去過的超級樹與植物園，將這座城市的美景盡收眼底，為旅程留下最壯闊的記憶。",
            tips="早上人潮較少，且早晨的光線柔和，非常適合拍出清透的城市景觀照。"
        )
        render_spot_card(
            "11:00 - 12:30", "武吉士 (Bugis) 最後採買",
            "前往「武吉士街 (Bugis Street)」，這裡是平價伴手禮的天堂，有點像是有冷氣的夜市。您可以在此買齊要送給親友的紀念品（如魚尾獅巧克力、鑰匙圈等）。午餐在附近享用道地美食，確保離開前沒有遺憾。",
            food=["亮耀海南雞飯", "Zam Zam 印度煎餅", "阿秋甜品"],
            tips="武吉士街人多擁擠，採買時請注意隨身財物。"
        )
        render_spot_card(
            "12:30 - 14:25", "前往機場 & 星耀樟宜 (Jewel)",
            "回 YOTEL 取行李前往機場。務必預留時間去機場旁的「星耀樟宜 (Jewel Changi)」，觀賞世界最大的室內瀑布「雨漩渦 (Rain Vortex)」。看著水流從 40 公尺高空傾瀉而下，搭配周圍的森林谷，震撼人心，是新加坡送給旅客最後的驚喜。",
            tips="瀑布位於 T1 航廈前方，若您的班機在 T3 報到，可以搭乘機場電車前往觀賞。"
        )

elif page == "🗺️ 地圖導航":
    st.markdown('<div class="main-header">🗺️ 行程景點地圖</div>', unsafe_allow_html=True)
    st.markdown("包含：飯店、機場、濱海灣、聖淘沙及各大文化區，紅點代表您將造訪的地點。")
    
    layer = pdk.Layer(
        "ScatterplotLayer",
        locations,
        get_position=["lon", "lat"],
        get_color=[200, 30, 0, 160],
        get_radius=300,
        pickable=True,
    )
    
    view_state = pdk.ViewState(latitude=1.29, longitude=103.85, zoom=11, pitch=50)
    
    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "{name}\n類型: {type}"},
        map_style="mapbox://styles/mapbox/light-v9"
    )
    st.pydeck_chart(r)
    st.caption("您可以直接在地圖上縮放，查看各個景點的相對位置，方便規劃交通。")

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