import streamlit as st
st.title("Age Checker")

st.text_input('First Name')
st.text_input('Middle Name')
st.text_input('Last Name')
age= st.text_input('Enter age')
if st.button("Check Age"):
        try:
            # Try to convert the input to an integer
            age = int(age)

            # Perform the age check
            if age <= 18:
                st.write("Kojoa ulale babaa!.")
            else:
                st.write("Wee mzee rada?.")
        except ValueError:
            # If the input cannot be converted to an integer, show an error message
            st.write("Invalid input. Please enter a valid age as a number.")
