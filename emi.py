import streamlit as st
from cal import *

st.header('EMI Calculator')
st.write("This is the app for EMI calculation")
a = st.number_input("Enter Amount:")
b = st.number_input("Enter Tenure:")
c = st.number_input("Enter interest rate:")

submit = st.button('Answer')
st.write(submit)
if submit:
    ans = simple_interest(a,b,c)
    total = total_amnt(a,b,c)
    st.write(f'Interest amount is {ans}')
    st.write(f'Total amount to pay is {total}')
    