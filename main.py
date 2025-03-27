import streamlit as st # for creeate web interface
import pandas as pd # for data manipulation
import datetime # for handling dates
import csv # for reading and write CSV file
import os # for file operations

# Define the file name for starting mood data
MOOD_FILE = "mood_log.csv"

# function to read mood data from the csv file
def load_mood_data():
    if not os.path.exists(MOOD_FILE): #
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE)

# 
def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", ) as file:

        writer = csv.writer(file)

        writer.writerow([date, mood])

# streamlit app title
st.title("Mood Tracker")

# get todays date
today = datetime.date.today()

# create sub header for mood input
st.subheader("How are your feeling today?")

# create dropdown for mood selection
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# create button to save mood
if st.button("Log Mood"):
    # 
    save_mood_data(today, mood)
    st.success("Mood logged successfully!")

data = load_mood_data()

# if there is data to display
if not data.empty:
    # create section for visualization
    st.subheader("Mood Trends Over Time")
    # convert date strings to datetime Object
    data["Date"] = pd.to_datetime(data["Date"])

    # count frequency for each mood
    mood_counts = data.groupby("Mood").count()["Date"]

    # create bar chart
    st.bar_chart(mood_counts)

