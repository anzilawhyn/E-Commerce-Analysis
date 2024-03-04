import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk visualisasi pertanyaan 1
def visualize_price_deliverytime_review(df):
    correlation_price = df['price_x'].corr(df['review_score'])
    correlation_delivery = df['delivery_time'].corr(df['review_score'])
    st.write(f'Correlation Price and Review Score: {correlation_price:.5f}')
    st.write(f'Correlation Delivery Time and Review Score: {correlation_delivery:.5f}')
    
    rgb_color = (105/255, 153/255, 221/255) 
    custom_palette = sns.dark_palette(rgb_color, reverse=True, as_cmap=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='price_x', y='delivery_time', hue='review_score', palette=custom_palette, alpha=0.8, ax=ax)
    plt.title('Hubungan antara Harga dan Waktu Pengiriman dengan Skor Review')
    plt.xlabel('Harga')
    plt.ylabel('Waktu Pengiriman')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(title='Skor Review')
    st.pyplot(fig)

# Fungsi untuk visualisasi pertanyaan 2
def visualize_monthly_revenue(df):
    transaction_total = all_df.groupby('year_month').agg({'total_price': 'sum'})
    transaction_total.index = transaction_total.index.astype(str)
    transaction_total_2018 = transaction_total[transaction_total.index.str.startswith('2018')]
    transaction_total_2018.sort_values(by='year_month', ascending=True, inplace=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(transaction_total_2018.index, transaction_total_2018.values, marker='o', linestyle='-')
    ax.set_title('Total Transaksi per Bulan Tahun 2018')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Total Pendapatan')
    plt.xticks(rotation=45)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

# Fungsi untuk visualisasi pertanyaan 3
def visualize_most_popular_category(df):
    monthly_total_sales = data_most_popular_category.groupby(['product_category_name_english'])['total_price'].sum()
    monthly_total_sales_sorted = monthly_total_sales.sort_values(ascending=True)
    top_10_categories = monthly_total_sales_sorted.head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    top_10_categories.plot(kind='barh', color='skyblue', ax=ax)
    plt.title('Top 10 Kategori Produk yang Paling Banyak Diminati')
    plt.xlabel('Total Pendapatan')
    plt.ylabel('Kategori Produk')
    plt.grid(True, linestyle='--', alpha=0.7)
    st.pyplot(fig)

# Load data
# Load data untuk pertanyaan 1
data_price_deliverytime_review = pd.read_csv('all_data.csv')
# Load data untuk pertanyaan 2
all_df = pd.read_csv('all_data.csv')
# Load data untuk pertanyaan 3
data_most_popular_category = pd.read_csv('all_data.csv')

# Main Streamlit app
def main():
    st.title('Dashboard Analisis Data')
    st.sidebar.title('Pertanyaan Analisis Data')

    # Tampilkan pilihan pertanyaan di sidebar
    selected_question = st.sidebar.selectbox('Pilih Pertanyaan:', ['Hubungan antara Harga dan Waktu Pengiriman dengan Skor Review',
                                                                   'Revenue Perusahaan pada Tahun 2018',
                                                                   'Kategori Produk yang Paling Banyak Diminati'])

    if selected_question == 'Hubungan antara Harga dan Waktu Pengiriman dengan Skor Review':
        st.header(selected_question)
        visualize_price_deliverytime_review(data_price_deliverytime_review)
    elif selected_question == 'Revenue Perusahaan pada Tahun 2018':
        st.header(selected_question)
        visualize_monthly_revenue(all_df)
    elif selected_question == 'Kategori Produk yang Paling Banyak Diminati':
        st.header(selected_question)
        visualize_most_popular_category(data_most_popular_category)

if __name__ == '__main__':
    main()


