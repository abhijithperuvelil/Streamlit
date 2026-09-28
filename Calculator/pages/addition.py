import streamlit as st
st.title("Addition")
n1=st.number_input("Enter Number 1: ",min_value=0)
print(n1)
n2=st.number_input("Enter Number 2: ",min_value=0)
print(n2)
btn=st.button("Add")
if btn:
    result=n1+n2
    print("Result is ",result)
    st.write("Result is ",result)
# st.title("BMI")
# w=st.number_input("Enter the Weight: ",min_value=0)
# h=st.number_input("Enter the Height: ",min_value=0)
# btn=st.button("Calculate BMI")
# if btn:
#     bmi=w/((h/100)**2)
#     if bmi<18.5:
#         st.info("Under Weight")
#     elif 18.5 <=bmi <25:
#         st.success("Normal Weight")
#     elif 25<=bmi <30:
#         st.warning("Over Weight")
#     else:
#         st.error("Obesity")
