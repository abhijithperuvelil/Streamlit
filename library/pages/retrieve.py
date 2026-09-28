import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title("Read a Book Record")
id=st.number_input("Enter the Id",min_value=0)
btn= st.button("Retrieve")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    records=b.retrieve(id)
    if records:
        print("Book Record")
        st.write("id: ",records[0])
        st.write("Title: ",records[1])
        st.write("Author: ",records[2])
        st.write("Price: ",records[3])
        st.write("Pages: ",records[4])
        st.write("Language: ",records[5])
    else:
     st.error("Book Not Found")