import streamlit as st

st.set_page_config(page_title="Data Visualisatie", page_icon="📊")

st.title("Welkom bij de Data Visualisatie App")

keuze = st.radio("Over welk geslacht wil je informatie?", ["Man", "Vrouw"])
st.session_state["keuze"] = keuze  # Opslaan in session state

origin = st.radio("Ben je allochtoon?", ["Ja", "Nee"])
st.session_state["origin"] = origin  # Opslaan

education = st.radio("Wat is je opleidingsniveau?", ["Hoogopgeleid", "Laagopgeleid"])
st.session_state["education"] = education  # Opslaan

if st.button("Toon Resultaten"):
    st.switch_page("pages/1_resultaten.py")  # Ga naar de resultatenpagina
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Resultatenpagina")

# Laad de dataset
df = pd.read_csv("data.csv", names=["Geslacht", "Afkomst", "Opleidingsniveau"])

# Haal de gebruikerskeuzes op uit session state
keuze = st.session_state.get("keuze", "Man")
origin = st.session_state.get("origin", "Ja")
education = st.session_state.get("education", "Hoogopgeleid")

# Filter de dataset op basis van de keuzes
filtered_df = df[
    (df["Geslacht"] == keuze) &
    (df["Afkomst"] == origin) &
    (df["Opleidingsniveau"] == education)
]

st.write(f"**Aantal personen die voldoen aan jouw criteria:** {len(filtered_df)}")

# Geslacht verdeling grafiek
fig, ax = plt.subplots()
df["Geslacht"].value_counts().plot(kind="bar", ax=ax, color=["blue", "pink"])
ax.set_title("Verdeling Geslacht")
ax.set_ylabel("Aantal")
st.pyplot(fig)

# Afkomst verdeling grafiek
fig, ax = plt.subplots()
df["Afkomst"].value_counts().plot(kind="bar", ax=ax, color=["green", "red"])
ax.set_title("Verdeling Afkomst")
ax.set_ylabel("Aantal")
st.pyplot(fig)

# Opleidingsniveau verdeling grafiek
fig, ax = plt.subplots()
df["Opleidingsniveau"].value_counts().plot(kind="bar", ax=ax, color=["purple", "orange"])
ax.set_title("Verdeling Opleidingsniveau")
ax.set_ylabel("Aantal")
st.pyplot(fig)

# Knop om terug te gaan naar de vragen
if st.button("Terug naar vragen"):
    st.switch_page("app.py")  # Terug naar de vragenpagina
