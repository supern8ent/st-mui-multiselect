import streamlit as st

from st_mui_multiselect import st_mui_multiselect

st.subheader("Component:")

# Create an instance of our component with a constant `name` arg, and
# print its output value.
options = list("wilycote")
selections = st_mui_multiselect(options)
st.markdown("You selected %s" % ", ".join(selections))
