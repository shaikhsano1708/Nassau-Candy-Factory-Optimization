import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Nassau Candy | Supply Chain Intelligence",
    page_icon="🍬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.stApp {
    background: #f5f7fb;
}

.main .block-container {
    max-width: 1500px;
    padding: 28px 38px 45px 38px;
}

[data-testid="stSidebar"] {
    background: #0b1424;
    border-right: 1px solid #1e293b;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: #dbe5f1 !important;
}

[data-testid="stSidebar"] span {
    color: #dbe5f1 !important;
}

.header-box {
    background: linear-gradient(
        135deg,
        #08111f 0%,
        #102a43 55%,
        #087f9c 100%
    );
    border-radius: 22px;
    padding: 30px 34px;
    margin-bottom: 25px;
    box-shadow: 0 12px 30px rgba(15,23,42,0.16);
}

.header-tag {
    color: #67e8f9 !important;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.header-title {
    color: #ffffff !important;
    font-size: 35px;
    font-weight: 800;
    line-height: 1.2;
}

.header-subtitle {
    color: #dbeafe !important;
    font-size: 15px;
    margin-top: 7px;
}

.section-title {
    color: #111827 !important;
    font-size: 23px;
    font-weight: 800;
    margin-top: 22px;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #64748b !important;
    font-size: 14px;
    margin-bottom: 18px;
}

.kpi-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 20px;
    min-height: 135px;
    box-shadow: 0 7px 22px rgba(15,23,42,0.06);
}

.kpi-icon {
    font-size: 25px;
    margin-bottom: 7px;
}

.kpi-label {
    color: #64748b !important;
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.7px;
}

.kpi-value {
    color: #111827 !important;
    font-size: 29px;
    font-weight: 800;
    margin-top: 6px;
}

.kpi-note {
    color: #94a3b8 !important;
    font-size: 11px;
    margin-top: 3px;
}

.status-box {
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    border-left: 5px solid #10b981;
    border-radius: 14px;
    padding: 15px 18px;
    margin: 20px 0;
}

.status-title {
    color: #047857 !important;
    font-size: 14px;
    font-weight: 800;
}

.status-text {
    color: #065f46 !important;
    font-size: 13px;
    margin-top: 4px;
}

.info-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 17px;
    padding: 21px 23px;
    margin: 15px 0;
    box-shadow: 0 5px 18px rgba(15,23,42,0.05);
}

.info-title {
    color: #111827 !important;
    font-size: 17px;
    font-weight: 800;
    margin-bottom: 7px;
}

.info-text {
    color: #64748b !important;
    font-size: 14px;
    line-height: 1.6;
}

.result-card {
    background: linear-gradient(
        135deg,
        #ecfeff,
        #eff6ff
    );
    border: 1px solid #bae6fd;
    border-left: 5px solid #0891b2;
    border-radius: 16px;
    padding: 18px 20px;
    margin: 18px 0;
}

.result-title {
    color: #0e7490 !important;
    font-size: 15px;
    font-weight: 800;
}

.result-text {
    color: #334155 !important;
    font-size: 14px;
    line-height: 1.6;
    margin-top: 5px;
}

.warning-card {
    background: #fff7ed;
    border: 1px solid #fed7aa;
    border-left: 5px solid #f97316;
    border-radius: 15px;
    padding: 17px 20px;
    margin-top: 20px;
}

.warning-title {
    color: #c2410c !important;
    font-size: 14px;
    font-weight: 800;
}

.warning-text {
    color: #7c2d12 !important;
    font-size: 13px;
    line-height: 1.6;
    margin-top: 5px;
}

.nav-box {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 15px;
    padding: 8px 10px;
    margin-bottom: 20px;
    box-shadow: 0 4px 15px rgba(15,23,42,0.05);
}

div[data-testid="stRadio"] label {
    color: #334155 !important;
    font-weight: 700 !important;
}

div[data-testid="stRadio"] p {
    color: #334155 !important;
    font-weight: 700 !important;
}

div[data-testid="stRadio"] span {
    color: #334155 !important;
}

div[data-testid="stSelectbox"] label p {
    color: #475569 !important;
    font-weight: 700 !important;
}

div[data-testid="stSlider"] label p {
    color: #475569 !important;
    font-weight: 700 !important;
}

div[data-testid="stMetric"] {
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 16px !important;
    padding: 17px !important;
}

div[data-testid="stMetric"] label {
    color: #64748b !important;
}

div[data-testid="stMetric"] label p {
    color: #64748b !important;
    font-weight: 700 !important;
}

div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #111827 !important;
}

div[data-testid="stMetric"] [data-testid="stMetricValue"] div {
    color: #111827 !important;
}

div[data-baseweb="select"] > div {
    background: #ffffff !important;
    border: 1px solid #dbe3ed !important;
    border-radius: 10px !important;
}

div[data-baseweb="select"] span {
    color: #111827 !important;
}

div[data-baseweb="select"] input {
    color: #111827 !important;
}

[data-testid="stDataFrame"] {
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    overflow: hidden;
}

.stButton > button {
    background: #0891b2 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 9px !important;
    font-weight: 700 !important;
}

.footer {
    text-align: center;
    color: #94a3b8 !important;
    font-size: 12px;
    padding-top: 35px;
}

</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    recommendations = pd.read_csv("dashboard_recommendations.csv")
    clusters = pd.read_csv("route_cluster_analysis.csv")
    kpi = pd.read_csv("project_kpi_summary.csv")
    return recommendations, clusters, kpi


try:
    recommendations, clusters, kpi = load_data()
except Exception as e:
    st.error("Dashboard files could not be loaded.")
    st.code(str(e))
    st.stop()


numeric_columns = [
    "Current Lead Time (days)",
    "Alternative Lead Time (days)",
    "Lead Time Saving (days)",
    "Lead Time Reduction (%)",
    "Current Distance (km)",
    "Alternative Distance (km)",
    "Distance Saving (km)",
    "Distance Reduction (%)",
    "Profit Margin (%)",
    "Scenario Confidence Score",
    "Final Recommendation Score"
]

for column in numeric_columns:
    if column in recommendations.columns:
        recommendations[column] = pd.to_numeric(
            recommendations[column],
            errors="coerce"
        )


st.markdown("""
<div class="header-box">
    <div class="header-tag">
        SUPPLY CHAIN ANALYTICS • DECISION INTELLIGENCE
    </div>
    <div class="header-title">
        🍬 Nassau Candy Factory Optimization
    </div>
    <div class="header-subtitle">
        Factory Reallocation & Shipping Optimization Recommendation System
    </div>
</div>
""", unsafe_allow_html=True)


st.sidebar.markdown("""
<div style="padding:8px 4px 18px 4px;">
    <div style="
        color:white;
        font-size:24px;
        font-weight:800;
    ">
        🍬 Nassau Candy
    </div>
    <div style="
        color:#94a3b8;
        font-size:12px;
        margin-top:5px;
    ">
        Supply Chain Intelligence
    </div>
</div>
""", unsafe_allow_html=True)


st.sidebar.markdown(
    """
    <div style="
        color:#67e8f9;
        font-size:12px;
        font-weight:800;
        letter-spacing:0.8px;
        margin-bottom:12px;
    ">
        SCENARIO FILTERS
    </div>
    """,
    unsafe_allow_html=True
)


product_options = [
    "All Products"
] + sorted(
    recommendations["Product Name"]
    .dropna()
    .unique()
    .tolist()
)

region_options = [
    "All Regions"
] + sorted(
    recommendations["Region"]
    .dropna()
    .unique()
    .tolist()
)

ship_options = [
    "All Ship Modes"
] + sorted(
    recommendations["Ship Mode"]
    .dropna()
    .unique()
    .tolist()
)

factory_options = [
    "All Factories"
] + sorted(
    recommendations["Current Factory"]
    .dropna()
    .unique()
    .tolist()
)

alternative_options = [
    "All Factories"
] + sorted(
    recommendations["Alternative Factory"]
    .dropna()
    .unique()
    .tolist()
)


selected_product = st.sidebar.selectbox(
    "🍫 Product",
    product_options
)

selected_region = st.sidebar.selectbox(
    "🌎 Region",
    region_options
)

selected_ship = st.sidebar.selectbox(
    "🚚 Ship Mode",
    ship_options
)

selected_current_factory = st.sidebar.selectbox(
    "🏭 Current Factory",
    factory_options
)

selected_alternative_factory = st.sidebar.selectbox(
    "📍 Alternative Factory",
    alternative_options
)


speed_priority = st.sidebar.slider(
    "⚡ Speed Priority",
    min_value=0,
    max_value=100,
    value=70,
    step=5
)

profit_priority = 100 - speed_priority


st.sidebar.markdown("---")

st.sidebar.markdown(
    f"""
    <div style="
        background:#111c2e;
        border:1px solid #263750;
        border-radius:14px;
        padding:15px;
    ">
        <div style="
            color:#67e8f9;
            font-size:12px;
            font-weight:800;
        ">
            OPTIMIZATION BALANCE
        </div>

        <div style="
            color:#dbeafe;
            font-size:13px;
            line-height:1.9;
            margin-top:7px;
        ">
            ⚡ Speed Priority: <b>{speed_priority}%</b><br>
            💰 Profit Priority: <b>{profit_priority}%</b>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


filtered = recommendations.copy()


if selected_product != "All Products":
    filtered = filtered[
        filtered["Product Name"] == selected_product
    ]


if selected_region != "All Regions":
    filtered = filtered[
        filtered["Region"] == selected_region
    ]


if selected_ship != "All Ship Modes":
    filtered = filtered[
        filtered["Ship Mode"] == selected_ship
    ]


if selected_current_factory != "All Factories":
    filtered = filtered[
        filtered["Current Factory"] == selected_current_factory
    ]


if selected_alternative_factory != "All Factories":
    filtered = filtered[
        filtered["Alternative Factory"] == selected_alternative_factory
    ]


if filtered.empty:
    st.warning("No scenarios match the selected filters.")
    st.stop()


scenario_summary = (
    filtered
    .groupby(
        [
            "Product Name",
            "Current Factory",
            "Alternative Factory",
            "Region",
            "Ship Mode"
        ],
        as_index=False
    )
    .agg(
        Orders=("Order ID", "nunique"),
        Current_Distance_km=(
            "Current Distance (km)",
            "mean"
        ),
        Alternative_Distance_km=(
            "Alternative Distance (km)",
            "mean"
        ),
        Distance_Saving_km=(
            "Distance Saving (km)",
            "mean"
        ),
        Distance_Reduction_pct=(
            "Distance Reduction (%)",
            "mean"
        ),
        Current_Lead_Time_days=(
            "Current Lead Time (days)",
            "mean"
        ),
        Alternative_Lead_Time_days=(
            "Alternative Lead Time (days)",
            "mean"
        ),
        Lead_Time_Saving_days=(
            "Lead Time Saving (days)",
            "mean"
        ),
        Lead_Time_Reduction_pct=(
            "Lead Time Reduction (%)",
            "mean"
        ),
        Profit_Margin_pct=(
            "Profit Margin (%)",
            "mean"
        ),
        Confidence=(
            "Scenario Confidence Score",
            "mean"
        ),
        Recommendation_Score=(
            "Final Recommendation Score",
            "mean"
        )
    )
)


scenario_summary["Priority Score"] = (
    scenario_summary["Lead_Time_Reduction_pct"]
    * speed_priority / 100
    +
    scenario_summary["Profit_Margin_pct"]
    * profit_priority / 100
)


scenario_summary = scenario_summary.sort_values(
    "Priority Score",
    ascending=False
).reset_index(drop=True)


total_candidates = len(scenario_summary)

avg_lead_reduction = scenario_summary[
    "Lead_Time_Reduction_pct"
].mean()

avg_distance_saving = scenario_summary[
    "Distance_Saving_km"
].mean()

avg_profit_margin = scenario_summary[
    "Profit_Margin_pct"
].mean()


st.markdown(
    "<div class='section-title'>📊 Executive Overview</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-subtitle">
        Current scenario performance and optimization indicators
    </div>
    """,
    unsafe_allow_html=True
)


c1, c2, c3, c4 = st.columns(4)


with c1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon">🎯</div>
            <div class="kpi-label">Scenario Candidates</div>
            <div class="kpi-value">{total_candidates:,}</div>
            <div class="kpi-note">Available combinations</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with c2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon">⚡</div>
            <div class="kpi-label">Lead-Time Reduction</div>
            <div class="kpi-value">{avg_lead_reduction:.1f}%</div>
            <div class="kpi-note">Average modeled improvement</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with c3:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon">🚚</div>
            <div class="kpi-label">Distance Saving</div>
            <div class="kpi-value">{avg_distance_saving:,.0f} km</div>
            <div class="kpi-note">Average scenario saving</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with c4:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon">💰</div>
            <div class="kpi-label">Profit Margin</div>
            <div class="kpi-value">{avg_profit_margin:.1f}%</div>
            <div class="kpi-note">Average product margin</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown(
    f"""
    <div class="status-box">
        <div class="status-title">
            ✓ Optimization Engine Active
        </div>
        <div class="status-text">
            {total_candidates:,} factory reallocation scenarios are
            currently available for analysis, with an average modeled
            lead-time reduction of {avg_lead_reduction:.1f}%.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    "<div class='nav-box'>",
    unsafe_allow_html=True
)

page = st.radio(
    "Dashboard Navigation",
    [
        "🏭 Factory Optimization",
        "🔬 What-If Analysis",
        "🎯 Recommendations",
        "⚠️ Risk & Impact"
    ],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)


if page == "🏭 Factory Optimization":

    st.markdown(
        "<div class='section-title'>🏭 Factory Optimization Simulator</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-subtitle">
            Compare current factory assignments with alternative
            factory scenarios.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-card">
            <div class="info-title">
                Factory Reallocation Opportunity
            </div>
            <div class="info-text">
                Evaluate alternative factory assignments using distance,
                modeled lead time, profitability and scenario scoring.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    table = scenario_summary[
        [
            "Product Name",
            "Current Factory",
            "Alternative Factory",
            "Region",
            "Ship Mode",
            "Orders",
            "Distance_Saving_km",
            "Distance_Reduction_pct",
            "Lead_Time_Saving_days",
            "Lead_Time_Reduction_pct",
            "Profit_Margin_pct",
            "Priority Score"
        ]
    ].copy()


    table.columns = [
        "Product",
        "Current Factory",
        "Alternative Factory",
        "Region",
        "Ship Mode",
        "Orders",
        "Distance Saving (km)",
        "Distance Reduction (%)",
        "Lead Saving (days)",
        "Lead Reduction (%)",
        "Profit Margin (%)",
        "Priority Score"
    ]


    table["Distance Saving (km)"] = table[
        "Distance Saving (km)"
    ].round(0)

    table["Distance Reduction (%)"] = table[
        "Distance Reduction (%)"
    ].round(1)

    table["Lead Saving (days)"] = table[
        "Lead Saving (days)"
    ].round(2)

    table["Lead Reduction (%)"] = table[
        "Lead Reduction (%)"
    ].round(1)

    table["Profit Margin (%)"] = table[
        "Profit Margin (%)"
    ].round(1)

    table["Priority Score"] = table[
        "Priority Score"
    ].round(1)


    st.dataframe(
        table.head(15),
        use_container_width=True,
        hide_index=True
    )


    st.markdown(
        "<div class='section-title'>📈 Lead-Time Improvement</div>",
        unsafe_allow_html=True
    )


    chart_data = scenario_summary.head(10).copy()

    chart_data["Scenario"] = (
        chart_data["Product Name"].str[:24]
        + " → "
        + chart_data["Alternative Factory"].str[:16]
    )

    chart_data = chart_data.set_index("Scenario")


    st.bar_chart(
        chart_data["Lead_Time_Reduction_pct"]
    )


elif page == "🔬 What-If Analysis":

    st.markdown(
        "<div class='section-title'>🔬 What-If Scenario Analysis</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-subtitle">
            Simulate the effect of moving a product from its current
            factory to an alternative factory.
        </div>
        """,
        unsafe_allow_html=True
    )


    scenario_names = (
        scenario_summary["Product Name"]
        + " | "
        + scenario_summary["Current Factory"]
        + " → "
        + scenario_summary["Alternative Factory"]
    ).tolist()


    selected_scenario = st.selectbox(
        "Select Scenario",
        scenario_names
    )


    selected_index = scenario_names.index(
        selected_scenario
    )

    selected_row = scenario_summary.iloc[
        selected_index
    ]


    a, b, c, d = st.columns(4)


    with a:
        st.metric(
            "Current Distance",
            f"{selected_row['Current_Distance_km']:,.0f} km"
        )


    with b:
        st.metric(
            "Alternative Distance",
            f"{selected_row['Alternative_Distance_km']:,.0f} km"
        )


    with c:
        st.metric(
            "Distance Reduction",
            f"{selected_row['Distance_Reduction_pct']:.1f}%"
        )


    with d:
        st.metric(
            "Lead-Time Saving",
            f"{selected_row['Lead_Time_Saving_days']:.2f} days"
        )


    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-title">
                🎯 Scenario Result
            </div>
            <div class="result-text">
                <b>{selected_row['Product Name']}</b>
                can be evaluated for movement from
                <b>{selected_row['Current Factory']}</b>
                to
                <b>{selected_row['Alternative Factory']}</b>.
                The modeled lead-time reduction is
                <b>{selected_row['Lead_Time_Reduction_pct']:.1f}%</b>.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    comparison = pd.DataFrame(
        {
            "Metric": [
                "Distance (km)",
                "Lead Time (days)"
            ],
            "Current": [
                selected_row["Current_Distance_km"],
                selected_row["Current_Lead_Time_days"]
            ],
            "Alternative": [
                selected_row["Alternative_Distance_km"],
                selected_row["Alternative_Lead_Time_days"]
            ]
        }
    )


    st.bar_chart(
        comparison.set_index("Metric")
    )


elif page == "🎯 Recommendations":

    st.markdown(
        "<div class='section-title'>🎯 Recommendation Dashboard</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-subtitle">
            Prioritized factory reallocation opportunities based on
            speed and profitability priorities.
        </div>
        """,
        unsafe_allow_html=True
    )


    recommendation_view = scenario_summary.copy()


    recommendation_view["Recommendation"] = np.select(
        [
            recommendation_view["Priority Score"] >= 70,
            recommendation_view["Priority Score"] >= 50
        ],
        [
            "High Potential",
            "Moderate Potential"
        ],
        default="Review Required"
    )


    recommendation_view = recommendation_view[
        [
            "Product Name",
            "Current Factory",
            "Alternative Factory",
            "Region",
            "Ship Mode",
            "Lead_Time_Reduction_pct",
            "Distance_Reduction_pct",
            "Profit_Margin_pct",
            "Confidence",
            "Priority Score",
            "Recommendation"
        ]
    ].copy()


    recommendation_view.columns = [
        "Product",
        "Current Factory",
        "Alternative Factory",
        "Region",
        "Ship Mode",
        "Lead Reduction (%)",
        "Distance Reduction (%)",
        "Profit Margin (%)",
        "Confidence",
        "Priority Score",
        "Recommendation"
    ]


    for column in [
        "Lead Reduction (%)",
        "Distance Reduction (%)",
        "Profit Margin (%)",
        "Confidence",
        "Priority Score"
    ]:
        recommendation_view[column] = recommendation_view[
            column
        ].round(1)


    st.dataframe(
        recommendation_view.head(20),
        use_container_width=True,
        hide_index=True
    )


    st.markdown(
        "<div class='section-title'>🏆 Priority Score Comparison</div>",
        unsafe_allow_html=True
    )


    top = scenario_summary.head(10).copy()


    top["Scenario"] = (
        top["Product Name"].str[:22]
        + " → "
        + top["Alternative Factory"].str[:16]
    )


    top = top.set_index("Scenario")


    st.bar_chart(
        top["Priority Score"]
    )


elif page == "⚠️ Risk & Impact":

    st.markdown(
        "<div class='section-title'>⚠️ Risk & Impact Panel</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-subtitle">
            Review scenario categories, route clusters and modeling
            considerations before operational implementation.
        </div>
        """,
        unsafe_allow_html=True
    )


    high = (
        scenario_summary["Priority Score"] >= 70
    ).sum()


    moderate = (
        (scenario_summary["Priority Score"] >= 50)
        &
        (scenario_summary["Priority Score"] < 70)
    ).sum()


    review = (
        scenario_summary["Priority Score"] < 50
    ).sum()


    r1, r2, r3 = st.columns(3)


    with r1:
        st.metric(
            "High Potential",
            f"{high:,}"
        )


    with r2:
        st.metric(
            "Moderate Potential",
            f"{moderate:,}"
        )


    with r3:
        st.metric(
            "Review Required",
            f"{review:,}"
        )


    st.markdown(
        "<div class='section-title'>🧩 Route Cluster Analysis</div>",
        unsafe_allow_html=True
    )


    if "Route Cluster" in clusters.columns:

        cluster_summary = (
            clusters
            .groupby("Route Cluster")
            .agg(
                Route_Groups=(
                    "Product Name",
                    "count"
                ),
                Avg_Distance_km=(
                    "Avg_Distance_km",
                    "mean"
                ),
                Avg_Lead_Time_days=(
                    "Avg_Lead_Time_days",
                    "mean"
                ),
                Avg_Lead_Time_Saving_days=(
                    "Avg_Lead_Time_Saving_days",
                    "mean"
                ),
                Avg_Distance_Reduction_pct=(
                    "Avg_Distance_Reduction_pct",
                    "mean"
                )
            )
            .reset_index()
        )


        cluster_summary.columns = [
            "Route Cluster",
            "Route Groups",
            "Avg Distance (km)",
            "Avg Lead Time (days)",
            "Avg Lead Saving (days)",
            "Avg Distance Reduction (%)"
        ]


        st.dataframe(
            cluster_summary.round(2),
            use_container_width=True,
            hide_index=True
        )


    st.markdown(
        """
        <div class="warning-card">
            <div class="warning-title">
                ⚠️ Modeling Assumption
            </div>
            <div class="warning-text">
                Lead-time values shown in this dashboard are
                scenario-based estimates derived from distance and
                shipping-mode assumptions. They should not be interpreted
                as historical observed transit performance. Factory
                reallocation scenarios also require operational validation
                before implementation.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown(
    """
    <div class="footer">
        Nassau Candy Factory Optimization
        • Data Analytics & Decision Intelligence
        <br>
        Scenario-based supply-chain analysis
    </div>
    """,
    unsafe_allow_html=True
)