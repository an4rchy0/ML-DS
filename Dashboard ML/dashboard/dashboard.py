import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from scipy.stats import pearsonr

sns.set(style='dark')

day_df = pd.read_csv(".\main_data\day.csv")
hour_df = pd.read_csv(".\main_data\hour.csv")

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

with st.sidebar:
    st.image("https://th.bing.com/th/id/OIP.9nhStdn8j1pWTD5PQHfJOwHaIB?rs=1&pid=ImgDetMain")
    start_date, end_date = st.date_input("Rentang Waktu", min_value=min_date, max_value=max_date, value=[min_date, max_date])

filtered_day_df = day_df[(day_df["dteday"] >= str(start_date)) & (day_df["dteday"] <= str(end_date))]
filtered_hour_df = hour_df[(hour_df["dteday"] >= str(start_date)) & (hour_df["dteday"] <= str(end_date))]

st.header("Bike Sharing Dashboard 🚲")
st.subheader("Daily Rentals")

col1, col2 = st.columns(2)
with col1:
    total_rentals = filtered_day_df["cnt"].sum()
    st.metric("Total Rentals", value=total_rentals)

with col2:
    avg_rentals = round(filtered_day_df["cnt"].mean(), 2)
    st.metric("Average Rentals per Day", value=avg_rentals)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(filtered_day_df["dteday"], filtered_day_df["cnt"], marker='o', linewidth=2, color="#90CAF9")
ax.set_title("Daily Bike Rentals")
ax.set_xlabel("Date")
ax.set_ylabel("Total Rentals")
st.pyplot(fig)

st.subheader("Rentals by Hour")
avg_hourly_rentals = filtered_hour_df.groupby("hr")["cnt"].mean().reset_index()
fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(x=avg_hourly_rentals["hr"], y=avg_hourly_rentals["cnt"], palette="Blues", ax=ax)
ax.set_title("Average Rentals by Hour")
ax.set_xlabel("Hour")
ax.set_ylabel("Average Rentals")
st.pyplot(fig)

st.subheader("Additional Insights")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data=day_df, x='cnt', bins=30, kde=True, hue='yr', palette='coolwarm', alpha=0.6, ax=ax)
ax.set_title('Distribusi Jumlah Penyewaan Sepeda per Tahun')
ax.set_xlabel('Jumlah Penyewaan Sepeda')
ax.set_ylabel('Frekuensi')
st.pyplot(fig)

seasonal = day_df.groupby(['yr', 'season'])['cnt'].mean().unstack()
fig, ax = plt.subplots(figsize=(10, 6))
seasonal.plot(kind='bar', color=['skyblue', 'lightgreen', 'orange', 'pink'], ax=ax)
ax.set_title('Pola Penggunaan Sepeda per Musim')
ax.set_xlabel('Tahun')
ax.set_ylabel('Rata-rata Penyewaan')
st.pyplot(fig)

st.subheader("Tren Bulanan Penggunaan Sepeda")
monthly_trend = day_df.groupby(['yr', 'mnth'])['cnt'].mean().unstack()
fig, ax = plt.subplots(figsize=(12, 6))
monthly_trend.T.plot(kind='bar', ax=ax, color=['skyblue', 'orange'])
ax.set_title('Tren Bulanan Penggunaan Sepeda Berdasarkan Tahun')
ax.set_xlabel('Bulan')
ax.set_ylabel('Rata-rata Jumlah Penyewaan Sepeda (cnt)')
ax.legend(title='Tahun', labels=['2011', '2012'])
st.pyplot(fig)

trend_2011 = day_df[day_df['yr'] == 0].groupby('dteday')['cnt'].mean()
trend_2012 = day_df[day_df['yr'] == 1].groupby('dteday')['cnt'].mean()
fig, ax = plt.subplots(figsize=(12, 6))
trend_2011.plot(kind='line', label='2011', color='blue', ax=ax)
trend_2012.plot(kind='line', label='2012', color='orange', ax=ax)
ax.set_title('Tren Harian Penyewaan Sepeda')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Rata-rata Penyewaan')
ax.legend()
st.pyplot(fig)

st.subheader("Tren Tahunan Penggunaan Sepeda")
yearly_trend = day_df.groupby('yr')['cnt'].mean()
yearly_trend.index = [2011, 2012]
fig, ax = plt.subplots(figsize=(6, 4))
yearly_trend.plot(kind='bar', ax=ax, color='orange')
ax.set_title('Tren Tahunan Penggunaan Sepeda')
ax.set_xlabel('Tahun')
ax.set_ylabel('Rata-rata Jumlah Penyewaan Sepeda (cnt)')
st.pyplot(fig)

st.subheader("Hubungan Faktor Lingkungan dengan Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(6, 4))
sns.regplot(x='hum', y='cnt', data=day_df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'}, ax=ax)
ax.set_title("Hubungan Kelembapan dengan Penyewaan Sepeda")
ax.set_xlabel("Kelembapan (Normalized)")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)

correlation_temp, _ = pearsonr(day_df['temp'], day_df['cnt'])
correlation_atemp, _ = pearsonr(day_df['atemp'], day_df['cnt'])
st.write(f"Korelasi antara Temperature (temp) dan Penyewaan Sepeda: {correlation_temp:.2f}")
st.write(f"Korelasi antara Feel-like Temperature (atemp) dan Penyewaan Sepeda: {correlation_atemp:.2f}")

fig, ax = plt.subplots(figsize=(6, 4))
sns.regplot(x='temp', y='cnt', data=day_df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'}, ax=ax)
ax.set_title("Hubungan Suhu dengan Penyewaan Sepeda")
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(6, 4))
sns.regplot(x='windspeed', y='cnt', data=day_df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'}, ax=ax)
ax.set_title("Hubungan Kecepatan Angin dengan Penyewaan Sepeda")
ax.set_xlabel("Kecepatan Angin (Normalized)")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)

st.subheader("Pengaruh Cuaca terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='weathersit', y='cnt', data=day_df, palette="Blues", ax=ax)
ax.set_title("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")
ax.set_xlabel("Kondisi Cuaca (1: Cerah, 2: Berkabut, 3: Hujan/Snow)")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)

st.caption("Bike Sharing Data Analysis 2025")
