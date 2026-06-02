import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



data=pd.read_csv("weatherHistory.csv")
df=pd.DataFrame(data)
print(df.isnull().sum())
df=df.dropna()
print(df.head())
print(df.info())

# Convert "Formatted Date" to datetime

df["Formatted Date"]= pd.to_datetime(df["Formatted Date"],utc= True)
df["Monthly"]=df["Formatted Date"].dt.month
df["Year"]=df["Formatted Date"].dt.year

# average temperature by month
monthly_avg=df.groupby("Monthly")["Temperature (C)"].mean()
print(monthly_avg)


#  highest average temperature in month
print("Month having highest avg temperature :",monthly_avg.idxmax())


# minimum, maximum, and average temperature for each weather summary
avg_temp_weather_summary=df.groupby("Summary")["Temperature (C)"].mean()
min_temp_weather_summary=df.groupby("Summary")["Temperature (C)"].min()
max_temp_weather_summary=df.groupby("Summary")["Temperature (C)"].max()

print("Average temperature:",avg_temp_weather_summary)
print("Minimum Temperature:",min_temp_weather_summary)
print("Maximum Temperature :",max_temp_weather_summary)

#mean, median, and standard deviation of temperature using NumPy

print("Mean of the temperature:",np.mean(df["Temperature (C)"]))
print("Median of the temperature:",np.median(df["Temperature (C)"]))
print("standard deviation  of the temperature:",np.std(df["Temperature (C)"]))

# correlation between temperature and humidity using NumPy
tempr=df["Temperature (C)"]
humidity=df["Humidity"]
corr=np.corrcoef(tempr,humidity)[0,1]
print("correlation between temperature and humidity :",corr)
if corr < 0:
    print("Temperature and humidity show a negative correlation.")
else:
    print("Temperature and humidity show a positive correlation.")


#  Visualization
# line chart of temperature over time

plt.figure(figsize=(12,6))
plt.plot(monthly_avg.index.astype(str), monthly_avg.values)
plt.title("Average Monthly Temperature Trend")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.savefig("images/monthly_avg_trend.png")
plt.tight_layout()
plt.show()

# scatter plot of temperature vs humidity
plt.figure(figsize=(12,8))

plt.scatter(tempr, df["Humidity"], alpha=0.1, s=8)

plt.title("Scatter Plot: Temperature vs Humidity")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("images/scattertemperature_humidity.png")

plt.show()



# Barchart showing the average temperature for each month.

plt.figure(figsize=(10,5))
plt.bar(monthly_avg.index, monthly_avg.values)

plt.title("Average Temperature by Month")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.xticks(rotation=45) 
plt.savefig("images/barcharttemperature_month.png")
plt.tight_layout()
plt.show()

# Wind speed distribution (histogram)
plt.hist(df["Wind Speed (km/h)"],bins=30, edgecolor="black")
plt.title("Wind speed distribution (histogram)")
plt.xlabel("Wind Speed (Km/h)")
plt.ylabel("Frequency")
plt.savefig("images/windspeed_hist.png")
plt.show()
