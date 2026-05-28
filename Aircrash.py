import streamlit as st
import pandas as pd
import altair as alt

def load_data():

    df = pd.read_csv("Air Crashes Full Data 1908 -2024 python project.csv")

 # convert the date col to datatime datatype
    df.Date = pd.to_datetime(df.Date, format="%d/%m/%Y")
    return df

df = load_data()    
# App title
st.title("GLOBAL AIRCRASH APP") 

# create filters
filters= {
"Country/Region": df["Country/Region"].unique(),
"Aircraft":df["Aircraft"]. unique(),
"Aircraft Manufacturer": df["Aircraft Manufacturer"].unique(),    
"Fatalities (air)": df["Fatalities (air)"].unique(),
"Ground": df["Ground"].unique(),
"Casualties": df["Casualties"].unique(),
"Date": df["Date"].unique(),
"Month": df["Month"].unique(),
"Quarter": df["Quarter"].unique(),
"Year": df["Year"].unique(),
"Location": df["Location"].unique(),
"Operator": df["Operator"].unique(),
"Aboard": df["Aboard"].unique()
} 

# store user selction
selected_filters = {}
# generate multi_selected widgets dynamically
for key, options in filters.items():
    selected_filters[key]=st.sidebar.multiselect(key,options)

# lets have the full data
filtered_df = df.copy()

# apply filter sesection to the data
for key, selected_values in selected_filters.items():
    if selected_values:
        filtered_df = filtered_df[filtered_df[key].isin(selected_values)]
st.dataframe(filtered_df.head())

# calculations 
no_of_aircrafts = len(filtered_df)
total_crashes = filtered_df["Aircraft"].nunique()
total_aboard = filtered_df["Aboard"].sum()
total_fatalities = filtered_df["Fatalities (air)"].sum()
total_ground = filtered_df["Ground"].sum()

# streamlit column component
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Total Aircrafts", no_of_aircrafts)
with col2:
    st.metric("Total Crashes", total_crashes)
with col3:
    st.metric("Total Aboard", total_aboard)
with col4:
    st.metric("Total Fatalities (air)", total_fatalities)
with col5:
    st.metric("Total Ground",total_ground)
    
    # chart

st.subheader("Countries with Largest Crashes")
top_crashes = filtered_df.groupby("Country/Region")["Aircraft"].nunique().nlargest(5).reset_index()
st.write(top_crashes) 

st.subheader("Top 5 Countries by Crashes")                                                                                                    
# configure the bar chart

chart1 = alt.Chart(top_crashes).mark_bar().encode(
    x=alt.X('Aircraft:Q', title="Crashes"),
    y=alt.Y("Country/Region:N"),
    color=alt.Color("Country/Region:N",legend=None)).properties(height=300)
# display the chart

st.altair_chart(chart1, use_container_width=True)

# Top 5 days of crashes
st.subheader("Top 5 Days of Crashes")
top_days_crashes = filtered_df.groupby("Date")["Aircraft"].nunique().nlargest(5).reset_index()
st.write(top_days_crashes)

# Top 5days of casualties
st.subheader("Top 5 Days of Highest Casualties")
top_days_casualties = filtered_df.groupby("Date")["Casualties"].sum().nlargest(5).reset_index()
st.write(top_days_casualties)

# Top 5  months of crashes
st.subheader("Top 5 Months of Crashes")
top_months_crashes = filtered_df.groupby("Month")["Aircraft"].nunique().nlargest(5).reset_index()
st.write(top_months_crashes)

# Top 5 months of casualties
st.subheader("Top 5 Months of Highest Casualties")
top_months_casualties = filtered_df.groupby("Month")["Casualties"].sum().nlargest(5).reset_index()
st.write(top_months_casualties)

# Quarter with the Highest crashes
st.subheader("Quarter with Highest Crashes")
top_quarter_crashes = filtered_df.groupby("Quarter")["Aircraft"].nunique().nlargest(1).reset_index()
st.write(top_quarter_crashes)

# Quarter with the highest casualties
st.subheader("Quarter with Highest Casualties")
top_quarter_casualties = filtered_df.groupby("Quarter")["Casualties"].sum().nlargest(1).reset_index()
st.write(top_quarter_casualties)

# 5 Aircraft Manufacturers with the highest crashes
st.subheader("Top 5 Manufacturers by Crashes")
top_manufacturers_crashes = filtered_df.groupby("Aircraft Manufacturer")["Aircraft"].nunique().nlargest(5).reset_index()
st.write(top_manufacturers_crashes)

# 5 Aircraft Manufacturers with the highest casualties
st.subheader("Top 5 Manufacturers by Casualties")
top_manufacturers_casualties = filtered_df.groupby("Aircraft Manufacturer")["Casualties"].sum().nlargest(5).reset_index()
st.write(top_manufacturers_casualties)

# 5 highest crashes by location
st.subheader("Top 5 Locations by Crashes")
top_location_crashes = filtered_df.groupby("Location")["Aircraft"].nunique().nlargest(5).reset_index()
st.write(top_location_crashes)

# 5 highest casualties by loation
st.subheader("Top 5 Locations by Casualties")
top_location_casualties = filtered_df.groupby("Location")["Casualties"].sum().nlargest(5).reset_index()
st.write(top_location_casualties)

# 5 highest crashes by Opreators
st.subheader("Top 5 Operators by Crashes")
top_operator_crashes = filtered_df.groupby("Operator")["Aircraft"].nunique().nlargest(5).reset_index()
st.write(top_operator_crashes)

# 5 highest casualties by Operators
st.subheader("Top 5 Operators by Casualties")
top_operator_casualties = filtered_df.groupby("Operator")["Casualties"].sum().nlargest(5).reset_index()
st.write(top_operator_casualties)



























































































































































































































































