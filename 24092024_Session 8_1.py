import pandas as pd
import streamlit as smt

url = "https://raw.githubusercontent.com/us-26/Population-graph_streamlit-from-session-8_1/refs/heads/main/population.csv"
data = pd.read_csv(url)
data = data.drop(columns = ["Unnamed: 0"])

unique_countries = data["country"].unique().tolist()
years = data["year"].unique()

my_df = pd.DataFrame(years, columns= ["Year"])

for country_name in unique_countries:
    my_df[country_name] = data[data["country"] == country_name]["pop"].values

# Make interactive graphs using streamlit library (29.b)

smt.title("Population Plot")
columns = smt.multiselect("countries: ", unique_countries)

smt.line_chart(my_df,x = "Year", y = columns, y_label = "Population", x_label = "Year")


