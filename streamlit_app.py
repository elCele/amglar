import streamlit as st
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('amglar.sql')

st.set_page_config(
    page_icon = '🎵',
    page_title = 'A.M.G.L.A.R.',
    layout = 'wide'
)

st.title("🎵 A.M.G.L.A.R.")

dataframe = pd.read_sql("SELECT * FROM tbl_generi_musicali", engine)

st.write(dataframe)
st.write(f"Numero di righe: {len(dataframe)}")