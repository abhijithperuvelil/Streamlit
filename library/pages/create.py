import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title("Create Book Record")
title=st.text_input("Enter the Book Title")
author=st.text_input("Enter the Author Name")
price=st.number_input("Enter the Price",min_value=0)
page=st.number_input("Enter the Page",min_value=0)
language=st.text_input("Enter the Language")
btn=st.button("Add Book")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    b.create(title,author,price,page,language)
    st.success("Record Created Successfully")
