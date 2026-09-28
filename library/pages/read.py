import streamlit as st
st.title("Read All Book Record")
from library_db import BookListCreateRetrieveUpdateDelete
b=BookListCreateRetrieveUpdateDelete()
records=b.list()
st.table(records)

