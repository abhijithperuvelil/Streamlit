import streamlit as st
from datetime import date


st.title("Student Registration Form")
name=st.text_input("Enter Your Name")
age=st.number_input("Enter Your Age",min_value=0)
dob=st.date_input("Enter Your Date of Birth",min_value=date(1990,1,1,),max_value=date.today())
email=st.text_input("Enter Your Email")
gender=st.radio("Select Gender",["Male","Female"])
course=st.selectbox("Select Your Course",['Python','Java','Dotnet','Testing'])
bt=st.button("Submit")
if bt:
    st.write("Name is ", name)
    st.write("Age is",age)
    st.write("Dob is",dob)
    st.write("Email is",email)
    st.write("Gender is",gender)
    st.write("Course",course)

