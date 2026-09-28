import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete


st.title("Delete Book Record")
id=st.number_input("Enter the Id: ",min_value=0)
btn=st.button("Submit")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    a=b.delete(id)
    if a > 0:
        st.success("Deleted ")
    else:
        st.error("No Records Found")