import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.ticker as ticker

#Header
st.header('Brazil E-commerce Dashboard :sparkles:')

#function
def create_monthly_orders_df(df):
    monthly_orders_df = df.resample(rule='M', on='order_purchase_timestamp').agg({
        'order_id':'nunique',
        'price':'sum'
    })

    monthly_orders_df.index = monthly_orders_df.index.strftime('%Y-%m')
    monthly_orders_df=monthly_orders_df.reset_index()
    monthly_orders_df.rename(columns={
        'order_id':'order_count',
        'price':'purchase'
    }, inplace=True)

    return monthly_orders_df

def create_daily_orders_df(df):
    daily_orders_df = df.resample(rule='D', on='order_purchase_timestamp').agg({
        'order_id': 'nunique',
        'price': 'sum'
    })

    daily_orders_df = daily_orders_df.reset_index()
    daily_orders_df.rename(columns={
        'order_id': 'order_count',
        'price': 'purchase'
    }, inplace=True)

    return daily_orders_df

def create_customers_city(df):
    customers_city_df = df.groupby(by=['customer_city']).agg({
        'customer_id': 'nunique'}).rename(columns={
        'customer_id':'Total',
        'customer_city':'Customer City',
    }).sort_values(by='Total', ascending=False).reset_index()

    return customers_city_df

def create_product_category(df):
    most_bought_df = df.groupby(by='product_category_name_english').agg({
        'order_id':'nunique'
    }).rename(columns={
        'order_id':'order_count',
        'product_category_name_english':'product_name'
    }).sort_values(by='order_count', ascending=False).reset_index()

    return most_bought_df

def create_rfm_rank(df):
    filtered_rfm_rank_df = df[['customer_id', 'frequency', 'monetary', 'recency', 'RFM_scores', 'segment', 'rank']]
    
    #display the highest customers based on RFM scores
    filtered_rfm_rank_df = filtered_rfm_rank_df.sort_values(by='RFM_scores', ascending=False)
    filtered_rfm_rank_df = filtered_rfm_rank_df.reset_index()
    return filtered_rfm_rank_df

def create_customer_segmentation(df):
    cust_classification = df.groupby(by=['rank','segment']).agg({
        'customer_id':'nunique'
    }, inplace=True).sort_values(by='rank', ascending=True)

    cust_classification = cust_classification.reset_index()
    cust_classification.rename(columns={
        'customer_id':'customers'
    }, inplace=True)

    return cust_classification

def create_delivery_time(df):
    delivery_time = df['order_delivered_customer_date'] - df['order_purchase_timestamp']

    #convert to seconds
    delivery_time_seconds = delivery_time.apply(lambda x: x.total_seconds())

    #convert seconds to days
    delivery_time['delivery_time_days'] = round(delivery_time_seconds/86400, 2)
    return delivery_time

#configuration path
all_df = pd.read_csv('ecommerce_datasets.csv')
rfm_df = pd.read_csv('rfm_datasets.csv')
datetime_columns = ['order_purchase_timestamp','order_approved_at',
                    'order_delivered_carrier_date','order_delivered_customer_date',
                    'order_estimated_delivery_date']
all_df.sort_values(by='order_purchase_timestamp',inplace=True)
all_df.reset_index(inplace=True)

#convert datatype of date columns
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

#create time filter for daily orders
min_date = all_df['order_purchase_timestamp'].min()
max_date = all_df['order_purchase_timestamp'].max()

start_date, end_date = st.date_input(
    label = 'Rentang Waktu(Harian)', min_value=min_date,
    max_value=max_date,
    value=[min_date,max_date])

main_df = all_df[(all_df['order_purchase_timestamp'] >= str(start_date))&
                 (all_df['order_purchase_timestamp'] <= str(end_date))]

#initiate the variable
monthly_orders_df = create_monthly_orders_df(all_df)
daily_orders_df = create_daily_orders_df(main_df)
customers_city_df = create_customers_city(all_df)
most_bought_df = create_product_category(all_df)
rfm_rank_df = create_rfm_rank(rfm_df)
cust_classification_df = create_customer_segmentation(rfm_df)
delivery_time_df = create_delivery_time(all_df)

#total order and purchase in monthly
st.subheader('Monthly Orders and Purchases')

#calculate monthly orders and purchased between sept 2016 - okt 2018
total_orders = monthly_orders_df.order_count.sum()
total_purchased = monthly_orders_df.purchase.sum()
avg_delivery_time = delivery_time_df.delivery_time_days.mean()

#create columns that contains monthly order and purchased
col1, col2, col3 = st.columns(3)

with col1:
    st.metric('Total Orders', value=total_orders)
with col2:
    st.metric('Purchase Value', value=total_purchased)
with col3:
    st.metric('Average Delivery Time', value=f'{avg_delivery_time:.2f}')

#create columns that contains graph monthly order as a whole and some description
col1, col2 = st.columns(2)

with col1 :
    #line graph
    fig, ax = plt.subplots(figsize=(16,8))
    ax.plot(
        monthly_orders_df['order_purchase_timestamp'],
        monthly_orders_df['order_count'],
        marker='o',
        linewidth=2,
        color='#72BCD4'
    )

    #add annotations
    for i, (x,y) in enumerate(zip(monthly_orders_df['order_purchase_timestamp'], monthly_orders_df['order_count'])):
        ax.text(x,y,f'{y}', fontsize=12, ha='center', va='bottom')

    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.xticks(rotation=45)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    ax.set_xlabel('Monthly', fontsize=20)
    ax.set_ylabel('Total Orders', fontsize=15)
    st.pyplot(fig)

with col2:
    #description
    st.caption('Sebanyak 99.441 order dibuat antara bulan September 2016 - Oktober 2018 dengan total pembelian mencapai 13.591.643 BRL (Brazilian Real), sementara durasi rata-rata aktual pengiriman barang ke pelanggan adalah 12 hari.')


#Break monthly orders into daily orders
st.subheader('Daily Orders')

#create line graph for daily orders 
fig, ax = plt.subplots(figsize=(16,8))
ax.plot(
    daily_orders_df['order_purchase_timestamp'],
    daily_orders_df['order_count'],
    marker='o',
    linewidth=2,
    color='#72BCD4'
)
total_daily_orders = daily_orders_df.order_count.sum()
total_daily_purchased = daily_orders_df.purchase.sum()

col1, col2 = st.columns(2)
with col1:
    st.metric('Total Orders', value=total_daily_orders)
with col2:
    st.metric('Total Purchased', value=f'{total_daily_purchased: .2f}')

#add annotations
for i, (x,y) in enumerate(zip(daily_orders_df['order_purchase_timestamp'], daily_orders_df['order_count'])):
    ax.text(x,y,f'{y}', fontsize=12, ha='center', va='bottom')

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xticks(rotation=45)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.set_xlabel('Daily', fontsize=20)
ax.set_ylabel('Total Orders', fontsize=15)
st.pyplot(fig)

#description about monthly and daily recap
st.markdown('Tren order dan pembelian (bulanan ataupun harian) menunjukkan bahwa PEAK SEASON terjadi pada November 2017, yaitu bertepatan dengan Event Black Friday. Tren tersebut menunjukkan peningkatan hingga bulan Januari 2018, diikuti dengan pola yang konsisten hingga bulan Agustus 2018. Penurunan yang signifikan pada bulan September-Oktober 2018 menunjukkan kemungkinan adanya ketidaklengkapan data.')

#Customers demographics
st.subheader('Customers Data')
tab1, tab2, tab3 = st.tabs(['Customers City', 'Most Sold Product Categories by Customers', 'Customers RFM'])

with tab1:
    st.table(customers_city_df.head(10))
    #description customer city
    st.markdown('Mayoritas pelanggan berlokasi di Sao Paulo, Rio De Janeiro, dan Belo Horizonte. Tingginya kontribusi kota Sao Paulo memiliki peran besar terhadap perputaran jual-beli di ecommerce. Ini juga didukung oleh mayoritas seller yang berlokasi di Sao Paulo.')

with tab2:
    #create graph most bought categories product by customers
    fig, ax = plt.subplots(figsize=(16,8))

    sns.barplot(
        x=most_bought_df['product_category_name_english'][:10],
        y=most_bought_df['order_count'][:10],
        ax=ax,
        linewidth=2,
        color='#72BCD4'
    )

    for i, (x,y) in enumerate(zip(most_bought_df['product_category_name_english'][:10], most_bought_df['order_count'][:10])):
        ax.text(x,y,f'{y}', fontsize=12, ha='center', va='bottom')

    plt.xticks(fontsize=15, rotation=45)
    plt.yticks(fontsize=15)
    ax.set_xlabel('Product Categories', fontsize=20)
    ax.set_ylabel('Total Orders', fontsize=15)
    st.pyplot(fig)

    #description about product categories
    st.markdown('bed_bath_table menjadi katagori produk yang paling diminati oleh pelanggan, disusul dengan health_beauty, sport_leisure, computer_accessories, dan furniture decor. Lima kategori teratas menunjukkan adanya tren pemenuhan gaya hidup yang menjadi kebutuhan.')

with tab3:
    #customers segmentation
    st.markdown('Berikut merupakan ranking dan segmentasi pelanggan yang dinilai berdasarkan skor RFM (Recency, Frequency, Monetary).')
    st.table(cust_classification_df)
    st.markdown('Setiap segmen memiliki jumlah pelanggan yang hampir sama. Ini menunjukkan bahwa persebaran segmentasi cukup merata. Untuk menambah pelanggan setia, perusahaan dapat fokus menaikkan loyalitas segmen New Customers dan Promising.')
    
    #top 10 customers profile based on RFM scores
    st.markdown('Berikut profil RFM dari 10 pelanggan teratas yang memiliki rank segmentasi tertinggi.')
    st.table(rfm_rank_df.head(10))

#Summary
st.subheader('Summary')
st.markdown('Dengan total 99.441 order dan pembelian senilai 13.591.643 BRL, menampilkan tren yang menarik. Salah satunya adalah puncak aktivitas terjadi pada November 2017, seiring Black Friday, dengan peningkatan konsisten hingga Januari 2018. Meski demikian, penurunan signifikan pada September-Oktober 2018 menunjukkan potensi ketidaklengkapan data. Berdasarkan demografi pelanggan, mayoritas pelanggan berasal dari Sao Paulo, Rio De Janeiro, dan Belo Horizonte. Ini menunjukkan Kota Sao Paulo memainkan peran sentral dalam perputaran jual-beli. Kategori produk paling diminati pelanggan adalah bed_bath_table, health_beauty, sport_leisure, computer_accessories, dan furniture decor, menandakan tren pemenuhan gaya hidup. Segmentasi pelanggan saat ini memiliki persebaran yang cukup merata. Upaya peningkatan loyalitas khusus segmentasi New Customers dan Promising dapat menjadi strategi yang efektif menambah jumlah pelanggan setia.')    
st.caption('--------------')
st.caption('Created by: Tania Syifa Utami')