import streamlit as st
from cal import *

st.header('Calculator')
st.write("This is the app for calculation")
a = st.number_input("Enter first number:")
b = st.number_input("Enter second number:")
operator = st.selectbox("operator",['+','-','*','/','**','%'])

submit = st.button('Answer')
st.write(submit)
if submit:
    if operator=='+':
        ans = add(a,b)
    elif operator == '-':
        ans = subtract(a,b)
    elif operator == '*':
        ans = multiply(a,b)
    elif operator == '/':
        ans = divide(a,b)
    elif operator == '%':
        ans = mod(a,b)
    elif operator == '**':
        ans = exp(a,b)
    
    st.write(f'answer is {ans}')
