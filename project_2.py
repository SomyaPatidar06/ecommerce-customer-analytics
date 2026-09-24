import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="E-Commerce Analytics Dashboard", layout="wide", initial_sidebar_state="expanded")

st.title("E-Commerce Customer & Order Analytics")

@st.cache_data
def load_data():
    file_path = "data/ecommerce_orders_2.csv"
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return pd.DataFrame()

df = load_data()

if df.empty:
    st.warning("Data not found. Please ensure data/ecommerce_orders_2.csv exists.")
    st.stop()

# Sidebar filters
st.sidebar.header("Dashboard Filters")
selected_regions = st.sidebar.multiselect("Select Region", df["Region"].unique(), default=df["Region"].unique())
selected_segments = st.sidebar.multiselect("Customer Segment", df["Customer_Segment"].unique(), default=df["Customer_Segment"].unique())

filtered_df = df[df["Region"].isin(selected_regions) & df["Customer_Segment"].isin(selected_segments)]

# KPIs
st.header("Executive Overview")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Revenue", f"${filtered_df['Revenue'].sum():,.2f}")
kpi2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.2f}")
kpi3.metric("Total Orders", f"{len(filtered_df):,}")
avg_order = filtered_df['Revenue'].sum() / len(filtered_df) if len(filtered_df) > 0 else 0
kpi4.metric("Average Order Value (AOV)", f"${avg_order:.2f}")

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["Customer Behavior & Segmentation", "Product, Discount & Profitability", "Delivery, Satisfaction & Logistics"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        segment_rev = filtered_df.groupby("Customer_Segment")["Revenue"].sum().reset_index()
        fig_seg = px.pie(segment_rev, names="Customer_Segment", values="Revenue", title="Revenue by Customer Segment", hole=0.3)
        st.plotly_chart(fig_seg, use_container_width=True)
    with col2:
        region_rev = filtered_df.groupby("Region")["Revenue"].sum().reset_index()
        fig_reg = px.bar(region_rev, x="Region", y="Revenue", title="Revenue by Region", color="Region")
        st.plotly_chart(fig_reg, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        cat_profit = filtered_df.groupby("Category")["Profit"].sum().reset_index()
        fig_cat = px.bar(cat_profit, x="Profit", y="Category", orientation="h", title="Profit by Category", color="Profit", color_continuous_scale="Viridis")
        st.plotly_chart(fig_cat, use_container_width=True)
    with col2:
        fig_scatter = px.scatter(filtered_df, x="Discount", y="Profit", color="Region", title="Impact of Discount on Profitability", opacity=0.7)
        st.plotly_chart(fig_scatter, use_container_width=True)

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        delivery_dist = px.histogram(filtered_df, x="Delivery_Days", nbins=14, title="Distribution of Delivery Days")
        st.plotly_chart(delivery_dist, use_container_width=True)
    with col2:
        delivered_only = filtered_df[filtered_df["Order_Status"] == "Delivered"]
        avg_rating = delivered_only.groupby("Delivery_Days")["Customer_Rating"].mean().reset_index()
        fig_rating = px.line(avg_rating, x="Delivery_Days", y="Customer_Rating", markers=True, title="Average Rating by Delivery Days")
        fig_rating.update_yaxes(range=[1, 5])
        st.plotly_chart(fig_rating, use_container_width=True)
