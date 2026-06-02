# 🌦️ Weather Data Analysis Project

## 📌 Overview

This project performs **Exploratory Data Analysis (EDA)** on a historical weather dataset using Python. The goal is to clean, analyze, and visualize weather data to identify trends and relationships between different weather variables.

The analysis includes temperature trends, weather condition summaries, wind speed distribution, and correlation analysis between temperature and humidity.

---

## 🛠️ Tools & Libraries Used

- Python 🐍
- Pandas 📊
- NumPy 🔢
- Matplotlib 📈

---

## 📂 Dataset

The dataset (`weatherHistory.csv`) contains historical weather information, including:

- Formatted Date
- Temperature (C)
- Apparent Temperature (C)
- Humidity
- Wind Speed (km/h)
- Wind Bearing (degrees)
- Visibility (km)
- Pressure (millibars)
- Weather Summary
- Daily Summary

---

## 📊 Analysis Performed

### Data Preparation

- Loaded the dataset using Pandas
- Checked for missing values
- Removed rows containing missing data
- Converted the `Formatted Date` column to datetime format
- Extracted month and year information from the date column

### Temperature Analysis

- Calculated average monthly temperatures
- Identified the month with the highest average temperature
- Calculated:
  - Mean temperature
  - Median temperature
  - Standard deviation of temperature

### Weather Summary Analysis

For each weather condition, calculated:

- Average temperature
- Minimum temperature
- Maximum temperature

### Correlation Analysis

- Calculated the correlation between Temperature and Humidity using NumPy
- Determined whether the relationship is positive or negative

### Wind Speed Analysis

- Analyzed the distribution of wind speed values using a histogram

---

## 📈 Visualizations

### 1. Monthly Average Temperature Trend

A line chart showing the average temperature for each month.

### 2. Temperature vs Humidity Scatter Plot

A scatter plot used to visualize the relationship between temperature and humidity.

### 3. Average Temperature by Month

A bar chart displaying average monthly temperatures.

### 4. Wind Speed Distribution

A histogram showing the frequency distribution of wind speed values.

---

## 💡 Key Insights

-Month With Highest Average Temperature

- Temperature and humidity exhibit a measurable correlation.
- Wind speed distribution helps identify common weather conditions within the dataset.

---

## 📁 Project Structure

```text
Weather-Data-Analysis/
│
├── weatherHistory.csv
├── analysis.py
│
├── images/
│   ├── monthly_avg_trend.png
│   ├── scattertemperature_time.png
│   ├── barcharttemperature_month.png
│   └── windspeed_hist.png
│
└── README.md
```

---

## 🚀 How to Run the Project

### Install Required Libraries

```bash
pip install pandas numpy matplotlib
```

### Run the Script

```bash
python analysis.py
```

---

## 📌 Future Improvements

- Add yearly temperature trend analysis
- Create a correlation matrix for all numerical features using seaborn
- Build an interactive dashboard using Streamlit
- Perform predictive weather analysis using machine learning

---

## 👨‍💻 Author

**Jiya Singh**

Computer Engineering Student

Interested in:

- Data Science
- Data Analytics
- Python Development

---

⭐ If you found this project useful, consider giving the repository a star!
