import streamlit as st
st.title("Substraction")
n1=st.number_input("Enter Number 1: ",min_value=0)
n2=st.number_input("Enter Number 2: ",min_value=0)
btn=st.button("Sub")
if btn:
    result=n1-n2
    st.write("Difference is ",result)