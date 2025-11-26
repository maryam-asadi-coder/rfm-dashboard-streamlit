import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="تحلیل RFM 360 درجه - مریم اسدی", layout="wide", page_icon="rocket")

st.title("تحلیل RFM 360 درجه | مریم اسدی")
st.markdown("### داشبورد تعاملی مشتریان - دیتاست Online Retail")

uploaded_file = st.file_uploader("فایل CSV دیتاست رو آپلود کن", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='latin1')
    st.success(f"دیتاست با موفقیت لود شد! ({df.shape[0]:,} ردیف)")

    # پیش‌پردازش
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
    df = df[~df['Description'].astype(str).str.contains('Adjust bad debt|Manual|POSTAGE', case=False, na=True)]

    df_clean = df.dropna(subset=['CustomerID']).copy()
    df_clean['CustomerID'] = df_clean['CustomerID'].astype(int)

    # حذف آوت‌لایر — نسخه امن
    q_low_qty = df_clean['Quantity'].quantile(0.01)
    q_high_qty = df_clean['Quantity'].quantile(0.99)
    q_low_price = df_clean['TotalPrice'].quantile(0.01)
    q_high_price = df_clean['TotalPrice'].quantile(0.99)

    df_clean = df_clean[
        (df_clean['Quantity'] >= q_low_qty) & (df_clean['Quantity'] <= q_high_qty) &
        (df_clean['TotalPrice'] >= q_low_price) & (df_clean['TotalPrice'] <= q_high_price)
    ]

    snapshot_date = df_clean['InvoiceDate'].max() + pd.Timedelta(days=1)

    # RFM
    rfm = df_clean.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'InvoiceNo': 'nunique',
        'TotalPrice': 'sum'
    }).reset_index()
    rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

    # امتیازدهی امن
    rfm['R'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1], duplicates='drop').astype('Int64')
    rfm['F'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5], duplicates='drop').astype('Int64')
    rfm['M'] = pd.qcut(rfm['Monetary'].rank(method='first'), 5, labels=[1,2,3,4,5], duplicates='drop').astype('Int64')
    rfm['RFM_Score'] = rfm['R'].fillna(3).astype(int) + rfm['F'].fillna(3).astype(int) + rfm['M'].fillna(3).astype(int)

    # Clustering
    scaler = StandardScaler()
    scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    rfm['Cluster'] = kmeans.fit_predict(scaled)
    rfm['Cluster_Name'] = rfm['Cluster'].map({0:'خوابیده', 1:'وفادار', 2:'قهرمان', 3:'در خطر'})

    # Pareto
    rfm_sorted = rfm.sort_values('Monetary', ascending=False).reset_index(drop=True)
    rfm_sorted['Cum_Revenue_%'] = (rfm_sorted['Monetary'].cumsum() / rfm_sorted['Monetary'].sum()) * 100
    rfm_sorted['Cum_Customers_%'] = (rfm_sorted.index + 1) / len(rfm_sorted) * 100
    pareto_80 = rfm_sorted[rfm_sorted['Cum_Revenue_%'] <= 80]['Cum_Customers_%'].max() if len(rfm_sorted) > 0 else 0

    # نمایش
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("تعداد مشتری", f"{len(rfm):,}")
    col2.metric("درآمد کل", f"£{rfm['Monetary'].sum():,.0f}")
    col3.metric("پارتو 80/20", f"{pareto_80:.1f}% مشتری")
    col4.metric("قهرمانان", len(rfm[rfm['RFM_Score'] >= 13]))

    tab1, tab2, tab3 = st.tabs(["توزیع RFM", "قانون پارتو", "خوشه‌بندی 3D"])

    with tab1:
        fig = make_subplots(rows=1, cols=3, subplot_titles=("Recency", "Frequency", "Monetary"))
        fig.add_trace(go.Histogram(x=rfm['Recency'], nbinsx=50), row=1, col=1)
        fig.add_trace(go.Histogram(x=rfm['Frequency'], nbinsx=50), row=1, col=2)
        fig.add_trace(go.Histogram(x=rfm['Monetary'], nbinsx=50), row=1, col=3)
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=rfm_sorted['Cum_Customers_%'], y=rfm_sorted['Cum_Revenue_%'], mode='lines+markers'))
        fig.add_hline(y=80, line_dash="dash", line_color="red")
        fig.add_vline(x=pareto_80, line_dash="dash", line_color="green")
        fig.update_layout(title="قانون پارتو", xaxis_title="درصد مشتریان", yaxis_title="درصد درآمد")
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        fig = px.scatter_3d(rfm, x='Recency', y='Frequency', z='Monetary', color='Cluster_Name',
                           size='Monetary', hover_data=['CustomerID', 'RFM_Score'])
        st.plotly_chart(fig, use_container_width=True)

    st.success("تحلیل با موفقیت انجام شد! این داشبورد رو با همه به اشتراک بذار")

else:
    st.info("فایل CSV دیتاست Online Retail رو آپلود کن تا داشبورد فعال بشه")
    st.image("https://imgur.com/a/0rK8X5j.png")  # عکس خوشگل

st.markdown("---")
st.caption("ساخته شده توسط مریم اسدی | [GitHub](https://github.com/maryam-asadi-coder) | [YouTube](https://youtube.com/@maryamasadiiiii)")
