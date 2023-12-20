import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv", sep=";")
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.png")

with col2:
    st.title("Mohammed Arsac")
    comment = """
Welcome to my programming portfolio! I'm a highly experienced software developer proficient in Python, Java, Spring, Hibernate, and database management, with a track record of creating over 20 successful applications. As a dedicated professional, I'm not only passionate about coding but also driven to maximize financial growth and stability in this dynamic field. My commitment to excellence and continuous learning ensures that I'm always ready to take on challenging projects and explore new opportunities for professional development. Thank you for visiting my webpage, and I look forward to collaborating with you on exciting ventures in the world of software development.
"""  #
    st.info(comment)

content = """Here you can find  some of the apps that I have built in python """
st.write(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
with col3:
    for index, row in df[0:10].iterrows():
        st.write(index, row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"Source Code: ({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.write(index, row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"Source Code: ({row['url']})")
