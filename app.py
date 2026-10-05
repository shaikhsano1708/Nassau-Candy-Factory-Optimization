import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Nassau Candy AI Factory Optimization",
    page_icon="🍬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #07111f;
    color: #eef5ff;
}

[data-testid="stHeader"] {
    background: #07111f;
}

[data-testid="stSidebar"] {
    background:
        radial-gradient(circle at 10% 0%, rgba(37,99,235,.22), transparent 34%),
        radial-gradient(circle at 95% 30%, rgba(124,58,237,.13), transparent 30%),
        linear-gradient(180deg,#071321 0%,#0a1728 52%,#081321 100%);
    border-right: 1px solid #203b58;
    min-width: 300px;
}

[data-testid="stSidebar"] > div:first-child { padding-top: 1rem; }

[data-testid="stSidebar"] * { color: #dce9f8; }

.sidebar-brand {
    background: linear-gradient(145deg,rgba(18,48,78,.95),rgba(8,27,46,.96));
    border: 1px solid #28506f;
    border-radius: 20px;
    padding: 19px 16px 16px;
    margin: 0 0 18px;
    box-shadow: 0 12px 30px rgba(0,0,0,.22);
}
.sidebar-brand-row { display:flex; align-items:center; gap:11px; }
.sidebar-logo {
    display:flex; align-items:center; justify-content:center;
    width:45px; height:45px; border-radius:14px;
    background:linear-gradient(135deg,#2563eb,#7c3aed);
    font-size:25px; box-shadow:0 5px 20px rgba(37,99,235,.25);
}
.sidebar-title { color:#f6fbff; font-size:21px; font-weight:800; line-height:1.15; }
.sidebar-sub { color:#9bb7d2; font-size:10px; margin-top:5px; line-height:1.4; }
.sidebar-engine {
    display:flex; align-items:center; gap:7px; margin-top:16px;
    padding:9px 10px; border:1px solid rgba(34,211,238,.25);
    background:rgba(8,145,178,.10); border-radius:10px;
    color:#7eeaff; font-size:9px; font-weight:800; letter-spacing:.8px;
}
.sidebar-engine-dot {
    width:7px; height:7px; background:#34d399; border-radius:50%;
    box-shadow:0 0 10px rgba(52,211,153,.8);
}
.sidebar-section {
    color:#6f91b3; font-size:10px; font-weight:800; letter-spacing:1.5px;
    text-transform:uppercase; margin:20px 0 9px;
}
.sidebar-filter-box {
    background:rgba(12,31,51,.72); border:1px solid #1d3b58;
    border-radius:15px; padding:12px 12px 2px; margin-top:4px;
}
.sidebar-status {
    background:linear-gradient(145deg,rgba(8,47,56,.78),rgba(10,27,46,.92));
    border:1px solid #17616b; border-radius:15px; padding:14px; margin-top:20px;
}
.sidebar-status-title { color:#78f0dc; font-size:10px; font-weight:800; letter-spacing:.7px; }
.sidebar-status-text { color:#9db7cb; font-size:11px; line-height:1.5; margin:8px 0 12px; }
.sidebar-mini {
    display:flex; justify-content:space-between; gap:8px;
    border-top:1px solid rgba(105,157,183,.16); padding-top:8px;
    margin-top:8px; color:#8da9c0; font-size:10px;
}
.sidebar-mini b { color:#5ce7b0; font-size:9px; letter-spacing:.5px; }
[data-testid="stSidebar"] [data-testid="stRadio"] > label { display:none; }
[data-testid="stSidebar"] [data-testid="stRadio"] > div { gap:5px; }
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    border:1px solid transparent; border-radius:11px; padding:9px 10px;
    transition:all .18s ease;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background:rgba(36,99,235,.13); border-color:rgba(64,133,205,.35);
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {
    background:linear-gradient(100deg,rgba(37,99,235,.28),rgba(124,58,237,.20));
    border-color:#3569a2; box-shadow:inset 3px 0 0 #48d9ff;
}
[data-testid="stSidebar"] [data-testid="stSelectbox"] > div > div,
[data-testid="stSidebar"] [data-testid="stSlider"] { border-radius:10px; }

.block-container {
    max-width: 1550px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

.hero {
    background: linear-gradient(110deg,#071728 0%,#08243d 48%,#063b4e 100%);
    border: 1px solid #174b68;
    border-radius: 24px;
    padding: 28px 34px;
    margin-bottom: 22px;
    box-shadow: 0 15px 50px rgba(0,0,0,.28);
}

.hero-top {
    color:#63dcff;
    font-size:12px;
    font-weight:800;
    letter-spacing:1.8px;
}

.hero-title {
    font-size:42px;
    font-weight:800;
    margin:6px 0;
    background:linear-gradient(90deg,#ffffff,#57d6ff,#b995ff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-sub {
    color:#a9c1d9;
    font-size:15px;
}

.pill {
    display:inline-block;
    background:#162f55;
    color:#75ddff;
    border:1px solid #24628c;
    border-radius:20px;
    padding:5px 12px;
    font-size:11px;
    font-weight:700;
    margin-right:8px;
}

.section-title {
    font-size:24px;
    font-weight:800;
    margin:14px 0 4px;
}

.section-sub {
    color:#8098b1;
    margin-bottom:16px;
}

.card {
    background:linear-gradient(145deg,#0d2035,#0a1728);
    border:1px solid #1c3a56;
    border-radius:17px;
    padding:18px;
    min-height:126px;
    box-shadow:0 10px 30px rgba(0,0,0,.16);
}

.card-blue { border-top:3px solid #3b82f6; }
.card-cyan { border-top:3px solid #22d3ee; }
.card-green { border-top:3px solid #22c55e; }
.card-gold { border-top:3px solid #fbbf24; }
.card-pink { border-top:3px solid #ec4899; }
.card-purple { border-top:3px solid #a855f7; }

.card-label {
    color:#8199b4;
    font-size:11px;
    font-weight:800;
    letter-spacing:.7px;
    text-transform:uppercase;
}

.card-value {
    color:#f6fbff;
    font-size:28px;
    font-weight:800;
    margin-top:8px;
}

.card-note {
    color:#54e39a;
    font-size:11px;
    margin-top:7px;
}

.panel {
    background:linear-gradient(145deg,#0b1d31,#091625);
    border:1px solid #1b3853;
    border-radius:18px;
    padding:20px;
    margin-top:18px;
}

.panel-title {
    font-size:18px;
    font-weight:800;
    color:#f5fbff;
}

.panel-sub {
    font-size:12px;
    color:#7f98b2;
}

.ai-box {
    background:linear-gradient(135deg,#062f38,#08263e);
    border:1px solid #13c8d7;
    border-radius:15px;
    padding:18px;
}

.ai-score {
    font-size:44px;
    font-weight:800;
    color:#42e8ff;
}

.badge-high {
    display:inline-block;
    background:#0c593f;
    color:#68f5b4;
    border:1px solid #1b9d70;
    border-radius:15px;
    padding:4px 10px;
    font-size:11px;
    font-weight:700;
}

.badge-medium {
    display:inline-block;
    background:#59420c;
    color:#ffd76a;
    border:1px solid #a67b18;
    border-radius:15px;
    padding:4px 10px;
    font-size:11px;
    font-weight:700;
}

.badge-review {
    display:inline-block;
    background:#571d32;
    color:#ff86a9;
    border:1px solid #a6385e;
    border-radius:15px;
    padding:4px 10px;
    font-size:11px;
    font-weight:700;
}

div[data-testid="stMetric"] {
    background:#0c1d31;
    border:1px solid #1c3a56;
    padding:14px;
    border-radius:14px;
}

div[data-testid="stMetricLabel"] {
    color:#8199b4;
}

div[data-testid="stMetricValue"] {
    color:#f6fbff;
}

.stButton > button {
    border-radius:10px;
    border:1px solid #24648d;
    background:linear-gradient(90deg,#2563eb,#7c3aed);
    color:white;
    font-weight:700;
}

[data-testid="stDataFrame"] {
    border:1px solid #1c3a56;
    border-radius:12px;
}

footer {
    visibility:hidden;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    scenario = pd.read_csv("dashboard_recommendations.csv")
    clusters = pd.read_csv("route_cluster_analysis.csv")
    kpi = pd.read_csv("project_kpi_summary.csv")
    try:
        models = pd.read_csv("ml_model_comparison.csv")
    except:
        models = pd.DataFrame()
    return scenario, clusters, kpi, models

scenario, clusters, kpi, models = load_data()

def col(df, names, default=0):
    for n in names:
        if n in df.columns:
            return df[n]
    return pd.Series(default, index=df.index)

scenario["Lead Reduction"] = pd.to_numeric(col(scenario, ["Lead Time Reduction (%)","Lead_Reduction_pct"]), errors="coerce").fillna(0)
scenario["Distance Reduction"] = pd.to_numeric(col(scenario, ["Distance Reduction (%)","Distance_Reduction_pct"]), errors="coerce").fillna(0)
scenario["Distance Saving"] = pd.to_numeric(col(scenario, ["Distance Saving (km)","Distance_Saving_km"]), errors="coerce").fillna(0)
scenario["Profit Margin"] = pd.to_numeric(col(scenario, ["Profit Margin (%)","Profit_Margin_pct"]), errors="coerce").fillna(0)
scenario["Confidence"] = pd.to_numeric(col(scenario, ["Scenario Confidence Score","Confidence"]), errors="coerce").fillna(.7)
scenario["AI Score"] = (
    scenario["Lead Reduction"].clip(0,100)*.35 +
    scenario["Distance Reduction"].clip(0,100)*.30 +
    scenario["Profit Margin"].clip(0,100)*.20 +
    scenario["Confidence"].clip(0,1)*100*.15
)

products = ["All Products"] + sorted(scenario["Product Name"].dropna().unique().tolist()) if "Product Name" in scenario else ["All Products"]
regions = ["All Regions"] + sorted(scenario["Region"].dropna().unique().tolist()) if "Region" in scenario else ["All Regions"]
ship_modes = ["All Ship Modes"] + sorted(scenario["Ship Mode"].dropna().unique().tolist()) if "Ship Mode" in scenario else ["All Ship Modes"]
factories = sorted(set(scenario["Current Factory"].dropna().unique().tolist()+scenario["Alternative Factory"].dropna().unique().tolist()))

with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-brand-row">
            <div class="sidebar-logo">🍬</div>
            <div>
                <div class="sidebar-title">Nassau Candy</div>
                <div class="sidebar-sub">Sweet Solutions. Smarter Supply Chains.</div>
            </div>
        </div>
        <div class="sidebar-engine">
            <span class="sidebar-engine-dot"></span>
            AI OPTIMIZATION ENGINE ONLINE
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section">Workspace Navigation</div>', unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "🤖 AI Decision Center",
            "🏭 Factory Optimization",
            "🔬 What-If Analysis",
            "🎯 Recommendations",
            "⚠️ Risk & Impact",
            "📊 Data Insights",
            "🧠 ML Performance",
            "🧩 Route Clustering",
            "📤 Reports & Export"
        ],
        label_visibility="collapsed"
    )

    st.markdown('<div class="sidebar-section">Scenario Filters</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-filter-box">', unsafe_allow_html=True)
    product = st.selectbox("Product", products)
    region = st.selectbox("Region", regions)
    ship_mode = st.selectbox("Ship Mode", ship_modes)
    current_factory = st.selectbox("Current Factory", ["All Factories"] + factories)
    alternative_factory = st.selectbox("Alternative Factory", ["All Factories"] + factories)
    priority = st.slider("⚡ Speed Priority", 0, 100, 70)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-status">
        <div class="sidebar-status-title">✦ LIVE DECISION INTELLIGENCE</div>
        <div class="sidebar-status-text">
            Scenario engine is analyzing factory routes, delivery speed and profitability.
        </div>
        <div class="sidebar-mini"><span>Engine Status</span><b>● ACTIVE</b></div>
        <div class="sidebar-mini"><span>AI Recommendations</span><b>READY</b></div>
        <div class="sidebar-mini"><span>Scenario Engine</span><b>ONLINE</b></div>
    </div>
    """, unsafe_allow_html=True)

filtered = scenario.copy()

if product != "All Products":
    filtered = filtered[filtered["Product Name"] == product]
if region != "All Regions" and "Region" in filtered:
    filtered = filtered[filtered["Region"] == region]
if ship_mode != "All Ship Modes" and "Ship Mode" in filtered:
    filtered = filtered[filtered["Ship Mode"] == ship_mode]
if current_factory != "All Factories":
    filtered = filtered[filtered["Current Factory"] == current_factory]
if alternative_factory != "All Factories":
    filtered = filtered[filtered["Alternative Factory"] == alternative_factory]

if len(filtered) == 0:
    filtered = scenario.copy()

avg_lead = filtered["Lead Reduction"].mean()
avg_distance = filtered["Distance Saving"].mean()
avg_margin = filtered["Profit Margin"].mean()
coverage = (filtered["Distance Saving"] > 0).mean()*100

st.markdown("""
<div class="hero">
<div class="hero-top">AI-POWERED • SUPPLY CHAIN DECISION INTELLIGENCE</div>
<div class="hero-title">🍭 Nassau Candy <span>AI Factory Optimization</span></div>
<div class="hero-sub">Smart Factory Reallocation &nbsp;|&nbsp; Optimized Shipping &nbsp;|&nbsp; Higher Profitability</div>
<br>
<span class="pill">Better Routes</span>
<span class="pill">Lower Costs</span>
<span class="pill">Faster Delivery</span>
<span class="pill">AI Recommendations</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">📊 Executive Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">AI-assisted scenario performance across the selected factory network.</div>', unsafe_allow_html=True)

c1,c2,c3,c4,c5,c6 = st.columns(6)

cards = [
    ("📦","TOTAL ORDERS", "10,194", "card-blue"),
    ("🍬","TOTAL PRODUCTS", str(scenario["Product Name"].nunique()), "card-purple"),
    ("📍","AVG DISTANCE", f"{scenario['Distance Saving'].mean():,.0f} km", "card-cyan"),
    ("⏱️","LEAD-TIME REDUCTION", f"{avg_lead:.1f}%", "card-green"),
    ("🚚","AVG DISTANCE SAVING", f"{avg_distance:,.0f} km", "card-gold"),
    ("🎯","RECOMMENDATION COVERAGE", f"{coverage:.1f}%", "card-pink")
]

for container, (icon,label,value,style) in zip([c1,c2,c3,c4,c5,c6], cards):
    with container:
        st.markdown(f"""
        <div class="card {style}">
        <div style="font-size:22px">{icon}</div>
        <div class="card-label">{label}</div>
        <div class="card-value">{value}</div>
        <div class="card-note">AI scenario intelligence</div>
        </div>
        """, unsafe_allow_html=True)

if page in ["🏠 Home","🤖 AI Decision Center"]:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">🤖 AI Decision Center</div><div class="panel-sub">Recommendation engine powered by scenario metrics and ML outputs.</div>', unsafe_allow_html=True)

    top = filtered.sort_values("AI Score", ascending=False).iloc[0]

    a,b,c,d,e = st.columns([1.2,1,1,1,1])
    with a:
        st.markdown('<div class="ai-box"><div class="card-label">TOP AI RECOMMENDATION</div><div style="font-size:20px;font-weight:800;margin:7px 0">🏆 '+str(top["Product Name"])+'</div><span class="badge-high">HIGH POTENTIAL</span></div>', unsafe_allow_html=True)
    with b:
        st.metric("AI Score", f"{top['AI Score']:.1f}/100")
    with c:
        st.metric("Lead Reduction", f"{top['Lead Reduction']:.1f}%")
    with d:
        st.metric("Distance Reduction", f"{top['Distance Reduction']:.1f}%")
    with e:
        st.metric("Profit Margin", f"{top['Profit Margin']:.1f}%")

    st.markdown(f"""
    <div class="ai-box" style="margin-top:14px">
    <b>💡 AI Insight</b><br>
    Moving <b>{top["Product Name"]}</b> from <b>{top["Current Factory"]}</b> to <b>{top["Alternative Factory"]}</b>
    shows a modeled lead-time reduction of <b>{top["Lead Reduction"]:.1f}%</b> and distance reduction of
    <b>{top["Distance Reduction"]:.1f}%</b>, with a modeled profit margin of <b>{top["Profit Margin"]:.1f}%</b>.
    This is a scenario recommendation and should be validated against factory capacity and operational constraints.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    left,right = st.columns([1.4,1])

    with left:
        st.markdown('<div class="panel"><div class="panel-title">🎯 Top AI-Ranked Scenarios</div><div class="panel-sub">Ranked by combined lead-time, distance, margin and confidence factors.</div>', unsafe_allow_html=True)
        show = filtered.sort_values("AI Score", ascending=False).head(8).copy()
        show["AI Score"] = show["AI Score"].round(1)
        show["Lead Reduction"] = show["Lead Reduction"].round(1)
        show["Distance Reduction"] = show["Distance Reduction"].round(1)
        show = show[["Product Name","Current Factory","Alternative Factory","AI Score","Lead Reduction","Distance Reduction"]]
        st.dataframe(show, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="panel"><div class="panel-title">🏭 Factory Network</div><div class="panel-sub">Scenario opportunities by origin and destination factory.</div>', unsafe_allow_html=True)
        route = filtered.groupby(["Current Factory","Alternative Factory"], as_index=False)["Distance Saving"].mean().sort_values("Distance Saving", ascending=False).head(10)
        route["Route"] = route["Current Factory"] + " → " + route["Alternative Factory"]

        import matplotlib.pyplot as plt

        factory_colors = {
            "Sugar Shack": "#22c55e",
            "Secret Factory": "#ef4444",
            "Lot's O' Nuts": "#94a3b8",
            "Wicked Choccy's": "#94a3b8",
            "The Other Factory": "#22c55e"
        }

        route_colors = [
            factory_colors.get(str(x), "#38bdf8")
            for x in route["Current Factory"]
        ]

        fig, ax = plt.subplots(figsize=(7.5, 4.8))
        fig.patch.set_facecolor("#0b1d31")
        ax.set_facecolor("#0b1d31")

        bars = ax.barh(
            route["Route"].iloc[::-1],
            route["Distance Saving"].iloc[::-1],
            color=route_colors[::-1],
            height=0.58
        )

        ax.tick_params(axis="x", colors="#dce9f8", labelsize=9)
        ax.tick_params(axis="y", colors="#dce9f8", labelsize=8)
        ax.set_xlabel("Distance Saving (km)", color="#dce9f8")
        ax.grid(axis="x", alpha=0.12)
        ax.set_axisbelow(True)

        for spine in ax.spines.values():
            spine.set_visible(False)

        for bar, value in zip(bars, route["Distance Saving"].iloc[::-1]):
            ax.text(
                bar.get_width(),
                bar.get_y() + bar.get_height() / 2,
                f" {value:,.0f}",
                va="center",
                ha="left",
                color="#eef5ff",
                fontsize=8,
                fontweight="bold"
            )

        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)
        st.markdown('</div>', unsafe_allow_html=True)

if page == "🏭 Factory Optimization":
    st.markdown('<div class="panel"><div class="panel-title">🏭 Factory Optimization</div><div class="panel-sub">Identify factory moves with strong geographic and operational impact.</div>', unsafe_allow_html=True)
    st.dataframe(
        filtered.sort_values("AI Score", ascending=False)[
            ["Product Name","Current Factory","Alternative Factory","Distance Saving","Distance Reduction","Lead Reduction","Profit Margin","AI Score"]
        ].head(20).round(2),
        use_container_width=True,
        hide_index=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel"><div class="panel-title">🏭 Factory Performance Profile</div><div class="panel-sub">Current-factory performance based on the scenario dataset and modeled operational indicators.</div>', unsafe_allow_html=True)

    profile = filtered.copy()
    if len(profile):
        profile["Risk Level"] = np.select(
            [
                profile["AI Score"] >= 75,
                profile["AI Score"] >= 55
            ],
            [
                "High Potential",
                "Moderate Potential"
            ],
            default="Review Required"
        )

        profile_agg = profile.groupby("Current Factory", as_index=False).agg(
            Orders=("Product Name", "size"),
            Avg_Distance_Saving_km=("Distance Saving", "mean"),
            Avg_Distance_Reduction_pct=("Distance Reduction", "mean"),
            Avg_Lead_Reduction_pct=("Lead Reduction", "mean"),
            Avg_Profit_Margin_pct=("Profit Margin", "mean"),
            Avg_AI_Score=("AI Score", "mean")
        )

        profile_agg["Performance"] = np.select(
            [
                profile_agg["Avg_AI_Score"] >= 75,
                profile_agg["Avg_AI_Score"] >= 55
            ],
            [
                "Strong",
                "Moderate"
            ],
            default="Review"
        )

        profile_agg = profile_agg.sort_values("Avg_AI_Score", ascending=False)

        st.dataframe(
            profile_agg.rename(columns={
                "Current Factory": "Factory",
                "Orders": "Scenario Records",
                "Avg_Distance_Saving_km": "Avg Distance Saving (km)",
                "Avg_Distance_Reduction_pct": "Avg Distance Reduction (%)",
                "Avg_Lead_Reduction_pct": "Avg Lead Reduction (%)",
                "Avg_Profit_Margin_pct": "Avg Profit Margin (%)",
                "Avg_AI_Score": "Avg AI Score"
            }).round(2),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No factory profile data is available for the selected filters.")

    st.markdown('</div>', unsafe_allow_html=True)


if page == "🔬 What-If Analysis":
    st.markdown('<div class="panel"><div class="panel-title">🔬 What-If Analysis</div><div class="panel-sub">Simulate a product and factory reassignment scenario.</div>', unsafe_allow_html=True)
    p = st.selectbox("Select Product", sorted(scenario["Product Name"].dropna().unique()), key="whatif_product")
    one = scenario[scenario["Product Name"] == p].copy()
    if len(one):
        best = one.sort_values("AI Score", ascending=False).iloc[0]
        x,y,z = st.columns(3)
        x.metric("Current Factory", str(best["Current Factory"]))
        y.metric("Alternative Factory", str(best["Alternative Factory"]))
        z.metric("AI Score", f"{best['AI Score']:.1f}/100")
        a,b,c = st.columns(3)
        a.metric("Lead-Time Reduction", f"{best['Lead Reduction']:.1f}%")
        b.metric("Distance Saving", f"{best['Distance Saving']:,.0f} km")
        c.metric("Profit Margin", f"{best['Profit Margin']:.1f}%")
    st.markdown('</div>', unsafe_allow_html=True)

if page == "🎯 Recommendations":
    st.markdown('<div class="panel"><div class="panel-title">🎯 Recommendations</div><div class="panel-sub">Actionable factory-product scenarios generated from the decision engine.</div>', unsafe_allow_html=True)
    rec = filtered.sort_values("AI Score", ascending=False).copy()
    rec["Recommendation"] = np.select(
        [rec["AI Score"] >= 75, rec["AI Score"] >= 55],
        ["High Potential","Moderate Potential"],
        default="Review Required"
    )
    st.dataframe(
        rec[["Product Name","Current Factory","Alternative Factory","AI Score","Recommendation","Lead Reduction","Distance Saving","Profit Margin"]].head(30).round(2),
        use_container_width=True,
        hide_index=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

if page == "⚠️ Risk & Impact":
    st.markdown('<div class="panel"><div class="panel-title">⚠️ Risk & Impact Analysis</div><div class="panel-sub">Review opportunity levels before operational validation.</div>', unsafe_allow_html=True)
    high = int((filtered["AI Score"] >= 75).sum())
    medium = int(((filtered["AI Score"] >= 55) & (filtered["AI Score"] < 75)).sum())
    review = int((filtered["AI Score"] < 55).sum())
    a,b,c = st.columns(3)
    a.metric("🟢 High Potential", high)
    b.metric("🟡 Moderate Potential", medium)
    c.metric("🔴 Review Required", review)

    st.markdown('<div class="panel-title" style="margin-top:20px">🔥 Factory Risk Heatmap</div><div class="panel-sub">Scenario opportunity level by current factory. Higher AI scores indicate stronger modeled opportunities, not operational approval.</div>', unsafe_allow_html=True)

    heat_df = filtered.copy()
    heat_df["Risk Level"] = np.select(
        [
            heat_df["AI Score"] >= 75,
            heat_df["AI Score"] >= 55
        ],
        [
            "High Potential",
            "Moderate Potential"
        ],
        default="Review Required"
    )

    heat = pd.crosstab(heat_df["Current Factory"], heat_df["Risk Level"])
    for category in ["High Potential", "Moderate Potential", "Review Required"]:
        if category not in heat.columns:
            heat[category] = 0
    heat = heat[["High Potential", "Moderate Potential", "Review Required"]]

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 4.5))
    fig.patch.set_facecolor("#07111f")
    ax.set_facecolor("#07111f")

    matrix = heat.values
    image = ax.imshow(matrix, cmap="YlOrRd", aspect="auto")

    ax.set_xticks(range(len(heat.columns)))
    ax.set_xticklabels(heat.columns, color="#dce9f8", fontsize=9)
    ax.set_yticks(range(len(heat.index)))
    ax.set_yticklabels(heat.index, color="#dce9f8", fontsize=9)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            ax.text(
                j, i, f"{matrix[i, j]:,}",
                ha="center", va="center",
                color="#111827" if matrix[i, j] > matrix.max() * 0.55 else "#f8fafc",
                fontsize=10, fontweight="bold"
            )

    ax.set_xlabel("Scenario Opportunity Level", color="#dce9f8", fontsize=10)
    ax.set_ylabel("Current Factory", color="#dce9f8", fontsize=10)

    for spine in ax.spines.values():
        spine.set_visible(False)

    cbar = fig.colorbar(image, ax=ax, fraction=0.035, pad=0.03)
    cbar.ax.tick_params(colors="#9fb5ca", labelsize=8)

    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    st.warning("These are analytical scenarios. Validate factory capacity, product feasibility, production constraints and real transport costs before implementation.")
    st.markdown('</div>', unsafe_allow_html=True)

if page == "📊 Data Insights":
    st.markdown('<div class="panel"><div class="panel-title">📊 Data Insights</div><div class="panel-sub">Product, factory and route-level scenario intelligence.</div>', unsafe_allow_html=True)
    if "Product Name" in filtered:
        prod = filtered.groupby("Product Name", as_index=False)["Distance Saving"].mean().sort_values("Distance Saving", ascending=False).head(10)
        st.bar_chart(prod.set_index("Product Name")["Distance Saving"])
    st.markdown('</div>', unsafe_allow_html=True)

if page == "🧠 ML Performance":
    st.markdown('<div class="panel"><div class="panel-title">🧠 ML Model Performance</div><div class="panel-sub">Comparison of trained regression models used in the project.</div>', unsafe_allow_html=True)
    if len(models):
        st.dataframe(models.round(4), use_container_width=True, hide_index=True)
        if "Model" in models.columns and "R2" in models.columns:
            st.bar_chart(models.set_index("Model")["R2"])
    else:
        st.info("ml_model_comparison.csv not found.")

    st.markdown('<div class="panel-title" style="margin-top:20px">🎯 Recommendation Driver Importance</div><div class="panel-sub">Weights used by the final decision score to balance speed, distance, profitability and scenario confidence.</div>', unsafe_allow_html=True)

    driver_df = pd.DataFrame({
        "Decision Driver": [
            "Lead-Time Reduction",
            "Distance Reduction",
            "Profit Margin",
            "Scenario Confidence"
        ],
        "Weight": [35, 30, 20, 15]
    })

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8.5, 3.8))
    fig.patch.set_facecolor("#07111f")
    ax.set_facecolor("#07111f")

    bars = ax.barh(
        driver_df["Decision Driver"].iloc[::-1],
        driver_df["Weight"].iloc[::-1],
        color=["#22d3ee", "#3b82f6", "#a855f7", "#22c55e"]
    )

    ax.set_xlim(0, 40)
    ax.set_xlabel("Decision Weight (%)", color="#dce9f8")
    ax.tick_params(axis="x", colors="#9fb5ca")
    ax.tick_params(axis="y", colors="#dce9f8", labelsize=9)
    ax.grid(axis="x", alpha=0.12)
    ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_visible(False)

    for bar, value in zip(bars, driver_df["Weight"].iloc[::-1]):
        ax.text(
            value + 0.7,
            bar.get_y() + bar.get_height() / 2,
            f"{value}%",
            va="center",
            color="#eef5ff",
            fontsize=10,
            fontweight="bold"
        )

    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    st.caption("This chart shows recommendation-score weights, not raw feature importance from a separately deployed model artifact.")
    st.markdown('</div>', unsafe_allow_html=True)


if page == "🧩 Route Clustering":
    st.markdown('<div class="panel"><div class="panel-title">🧩 Route Clustering</div><div class="panel-sub">Explore product-region-shipping groups and their modeled delivery characteristics.</div>', unsafe_allow_html=True)
    if len(clusters):
        st.dataframe(clusters, use_container_width=True, hide_index=True)
        numeric_cols = [c for c in clusters.columns if "Avg_" in c and pd.api.types.is_numeric_dtype(clusters[c])]
        if "Route Cluster" in clusters.columns and numeric_cols:
            metric_col = st.selectbox("Cluster metric", numeric_cols, key="cluster_metric")
            cluster_plot = clusters.groupby("Route Cluster", as_index=False)[metric_col].mean().sort_values(metric_col, ascending=True)

            import matplotlib.pyplot as plt

            factory_colors = {
                "Sugar Shack": "#22c55e",
                "Secret Factory": "#ef4444",
                "Lot's O' Nuts": "#94a3b8",
                "Wicked Choccy's": "#94a3b8",
                "The Other Factory": "#22c55e"
            }

            if "Current Factory" in clusters.columns:
                labels = clusters.groupby("Route Cluster")["Current Factory"].first()
                colors = [
                    factory_colors.get(labels.get(cluster, ""), "#94a3b8")
                    for cluster in cluster_plot["Route Cluster"]
                ]
            else:
                colors = ["#94a3b8"] * len(cluster_plot)

            fig, ax = plt.subplots(figsize=(9, 4.2))
            fig.patch.set_facecolor("#07111f")
            ax.set_facecolor("#07111f")

            bars = ax.barh(
                cluster_plot["Route Cluster"].astype(str),
                cluster_plot[metric_col],
                color=colors,
                height=0.62
            )

            ax.tick_params(axis="x", colors="#dce9f8", labelsize=10)
            ax.tick_params(axis="y", colors="#dce9f8", labelsize=10)
            ax.xaxis.label.set_color("#dce9f8")
            ax.set_xlabel(metric_col.replace("_", " "), fontsize=11)
            ax.set_ylabel("Route Cluster", fontsize=11)
            ax.grid(axis="x", alpha=0.12)
            ax.set_axisbelow(True)

            for spine in ax.spines.values():
                spine.set_visible(False)

            for bar, value in zip(bars, cluster_plot[metric_col]):
                ax.text(
                    bar.get_width(),
                    bar.get_y() + bar.get_height() / 2,
                    f" {value:,.0f}",
                    va="center",
                    ha="left",
                    color="#eef5ff",
                    fontsize=10,
                    fontweight="bold"
                )

            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

            st.markdown("""
            <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:6px">
                <span class="pill" style="border-color:#22c55e;color:#69f0a8">● Green = Sugar / Other Factory</span>
                <span class="pill" style="border-color:#ef4444;color:#ff8585">● Red = Secret Factory</span>
                <span class="pill" style="border-color:#64748b;color:#cbd5e1">● Grey = Lot's O' Nuts / Wicked Choccy's</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("route_cluster_analysis.csv is not available.")
    st.markdown('</div>', unsafe_allow_html=True)

if page == "📤 Reports & Export":
    st.markdown('<div class="panel"><div class="panel-title">📤 Reports & Export</div><div class="panel-sub">Download the currently filtered scenario results and available project summaries.</div>', unsafe_allow_html=True)
    export_df = filtered.copy()
    st.metric("Rows available for export", f"{len(export_df):,}")
    st.download_button(
        "⬇️ Download filtered recommendations (CSV)",
        data=export_df.to_csv(index=False).encode("utf-8"),
        file_name="nassau_candy_filtered_recommendations.csv",
        mime="text/csv",
        use_container_width=True
    )
    if len(kpi):
        st.download_button(
            "⬇️ Download project KPI summary (CSV)",
            data=kpi.to_csv(index=False).encode("utf-8"),
            file_name="project_kpi_summary.csv",
            mime="text/csv",
            use_container_width=True
        )
    if len(models):
        st.download_button(
            "⬇️ Download ML model comparison (CSV)",
            data=models.to_csv(index=False).encode("utf-8"),
            file_name="ml_model_comparison.csv",
            mime="text/csv",
            use_container_width=True
        )
    st.info("Lead-time and reallocation figures are scenario-based estimates. Validate factory capacity, product feasibility and real shipping costs before implementation.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;color:#58728d;font-size:11px;margin-top:30px">
Nassau Candy Factory Optimization • AI/ML Decision Support • Scenario-based analysis
</div>
""", unsafe_allow_html=True)
