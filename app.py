import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(
    page_title="Data Cleanse Pro", 
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Premium Custom CSS Styling
st.markdown("""
    <style>
    /* Main Background and text adjustments */
    .main { background-color: #0f1116; }
    
    /* Metrics Custom Glassmorphism Styling */
    .metric-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        transition: transform 0.2s ease-in-out;
    }
    .metric-card:hover {
        transform: translateY(-3px);
        border-color: #4f46e5;
    }
    .metric-title { font-size: 14px; color: #a1a1aa; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;}
    .metric-value { font-size: 32px; font-weight: 700; color: #ffffff; }
    .metric-delta { font-size: 13px; font-weight: 600; margin-top: 5px; }
    .delta-green { color: #10b981; }
    .delta-purple { color: #818cf8; }
    
    /* Elegant Sidebar modifications */
    section[data-testid="stSidebar"] {
        background-color: #11141a;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Panel
with st.sidebar:
    st.markdown("<h2 style='color:#818cf8; margin-bottom:0;'>✨ CleansePro</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#71717a; font-size:13px; margin-top:0;'>Smart Engine v2.0</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("### 📁 Input Source")
    uploaded = st.file_uploader("Drop your messy file here", type=["xlsx", "csv"])
    
    if uploaded:
        st.success("File uploaded successfully!")
        st.info(f"📄 **Filename:** {uploaded.name}")

# 4. Main Hero Header Section
st.markdown("<h1 style='font-weight: 800; letter-spacing: -1px; margin-bottom: 0;'>🧼 Interactive Data Cleaning Studio</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #a1a1aa; font-size: 16px; margin-top: 4px;'>An automated end-to-end processing pipeline for instant dataset optimization.</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if uploaded:
    # Read Dataset
    if uploaded.name.endswith(".csv"):
        df_raw = pd.read_csv(uploaded)
    else:
        df_raw = pd.read_excel(uploaded)
        
    df = df_raw.copy()

    # Metrics Compilation
    orig_rows = df.shape[0]
    orig_cols = df.shape[1]
    orig_missing = df.isna().sum().sum()
    orig_dupes = df.duplicated().sum()

    # --- Pipeline Processing Engine ---
    df.drop_duplicates(inplace=True)
    df.ffill(inplace=True)
    df.columns = df.columns.str.strip()

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip().str.title()

    outliers_removed = 0
    if "Sales" in df.columns:
        Q1 = df["Sales"].quantile(0.25)
        Q3 = df["Sales"].quantile(0.75)
        IQR = Q3 - Q1
        lower_limit = Q1 - 1.5 * IQR
        upper_limit = Q3 + 1.5 * IQR
        
        df_filtered = df[(df["Sales"] >= lower_limit) & (df["Sales"] <= upper_limit)]
        outliers_removed = df.shape[0] - df_filtered.shape[0]
        df = df_filtered

    final_rows = df.shape[0]
    rows_removed = orig_rows - final_rows

    # 5. UI Custom Cards Row (Replaces basic st.metric)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Optimized Rows</div>
                <div class="metric-value">{final_rows:,}</div>
                <div class="metric-delta delta-purple">📉 Kept {((final_rows/orig_rows)*100):.1f}% of data</div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Duplicates Purged</div>
                <div class="metric-value">{int(orig_dupes)}</div>
                <div class="metric-delta {"delta-green" if orig_dupes > 0 else "delta-purple"}">✨ Redundancy Free</div>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Missing Values Fixed</div>
                <div class="metric-value">{int(orig_missing)}</div>
                <div class="metric-delta {"delta-green" if orig_missing > 0 else "delta-purple"}">🛠️ Imputed via FFill</div>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Outliers Filtered</div>
                <div class="metric-value">{int(outliers_removed)}</div>
                <div class="metric-delta {"delta-green" if outliers_removed > 0 else "delta-purple"}">📊 Sales Column Scaled</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 6. Data Profiling & Action Split Screen Layout
    left_col, right_col = st.columns([3, 2])

    with left_col:
        st.markdown("<h3 style='margin-bottom:15px;'>⚡ Live Inspection Profile</h3>", unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["✨ Cleaned Master Dataset", "⏳ Original Raw Dataset"])
        
        with tab1:
            st.dataframe(df, use_container_width=True, height=380)
            
            # High-end Custom Action (Download) Area
            st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
            csv_data = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Export Optimized Production Dataset (CSV)",
                data=csv_data,
                file_name=f"cleanse_pro_{uploaded.name.split('.')[0]}.csv",
                mime="text/csv",
                use_container_width=True
            )

        with tab2:
            st.dataframe(df_raw, use_container_width=True, height=380)

    with right_col:
        st.markdown("<h3 style='margin-bottom:15px;'>📈 Distribution Analytics</h3>", unsafe_allow_html=True)
        
        with st.container(border=True):
            if "Sales" in df.columns:
                # Plotly distribution chart matching a clean theme layout
                fig = px.histogram(
                    df, x="Sales", 
                    nbins=20, 
                    title="Cleaned Sales Distribution (Outliers Excluded)",
                    color_discrete_sequence=['#818cf8']
                )
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font_color='#ffffff',
                    margin=dict(l=20, r=20, t=40, b=20),
                    height=360
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                # Fallback chart if "Sales" isn't present
                numeric_cols = df.select_dtypes(include='number').columns
                if len(numeric_cols) > 0:
                    fig = px.bar(
                        df, x=df.index[:15], y=numeric_cols[0],
                        title=f"Sample Track: Overview of {numeric_cols[0]}",
                        color_discrete_sequence=['#4f46e5']
                    )
                    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#ffffff', height=360)
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.info("ℹ️ Upload data containing numerical columns to populate visual distribution insights.")

else:
    # High-end welcome empty state
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.html(
        """
        <div style="border: 2px dashed rgba(255,255,255,0.1); border-radius: 16px; padding: 60px; text-align: center;">
            <p style="font-size: 48px; margin: 0;">⚡</p>
            <h3 style="margin-top: 10px; font-weight: 600;">Workspace Empty</h3>
            <p style="color: #71717a; max-width: 420px; margin: 0 auto 20px auto;">
                Please select or drag a CSV or Excel template into the left sidebar panel to trigger the data processing matrix pipeline.
            </p>
        </div>
        """
    )