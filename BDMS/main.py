from datetime import date
import streamlit as st
from streamlit.elements.widgets import button

from bdms_db import DonorCreateRetrieveUpdateDelete
tab1,tab2,tab3,tab4,tab5=st.tabs(["Add",'Read','Retrieve','Delete','Update'])
b=DonorCreateRetrieveUpdateDelete()
with tab1:
    st.title("Add New Donor")
    name=st.text_input("Enter the Name: ")
    blood_group=st.selectbox("Enter the Blood Group",['A+','A-','B+','B-','AB+','AB-','O+','O-'])
    phone=st.text_input("Enter the Phone Number: ")
    city=st.text_input("Enter the City")
    last_donation=st.date_input("Enter the Date")
    btn=st.button("Add Donor")
    if btn:
        b.post(name,blood_group,phone,city,last_donation)
        st.success("Donor Added")
with tab2:
    st.title("Read All Donors")
    btn=st.button("Read")
    if btn:
        records=b.get()
        st.table(records)
with tab3:
    st.title("Retrieve a User")
    id=st.number_input("Enter the User Id:",min_value=0)
    btn=st.button("Retrieve")
    if btn:
        records=b.get_id(id)
        if records:
            st.subheader("Donor Details")
            st.write("Id: ",records[0])
            st.write("Name: ",records[1])
            st.write("Blood Group: ",records[2])
            st.write("Phone is: ",records[3])
            st.write("City: ",records[4])
            st.write("Last Donation: ",records[5])
        else:
            st.error("No Id Found")
with tab4:
    st.title("Delete User")
    id=st.number_input("Enter the User ID: ",min_value=0)
    btn=st.button("Delete")
    if btn:
        records=b.delete(id)
        if records>0:
            st.success("User Deleted")
        else:
            st.error("No Id Found")
with tab5:
    st.title("Update User")
    id=st.number_input("Enter the Id",min_value=0)
    name=st.text_input("Enter the Name")
    blood_group = st.selectbox("Enter the New Blood Group",['A+','A-','B+','B-','AB+','AB-','O+','O-'])
    phone = st.text_input("Enter the Phone")
    city = st.text_input("Enter the New City")
    last_donation = st.date_input("Enter the New Date",min_value=date(1990,1,1))
    btn=st.button("Update User")
    if btn:
        records=b.put(id,name, blood_group, phone, city, last_donation)
        if records>0:
            st.success("Record Updated")
        else:
            st.error("No Id Found")
