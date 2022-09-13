import streamlit as st
from my_component import my_component

st.subheader("Component:")

# Create an instance of our component with a constant `name` arg, and
# print its output value.
options = list("wilycote")
selections = my_component(options)
st.markdown("You selected %s" % ", ".join(selections))
