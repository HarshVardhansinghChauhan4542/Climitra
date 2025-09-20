import streamlit as st
from src.ui.layout import render_main_dashboard

st.set_page_config(page_title="Climitra Dashboard", layout="wide")

def main():
    render_main_dashboard()

if __name__ == "__main__":
    main()
