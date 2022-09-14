import streamlit as st

from st_mui_multiselect import st_mui_multiselect

st.subheader("Component:")
options = ["Mayo", "Lettuce", "Pickles", "Tomatoes", "Onions", "Mushrooms", "Ketchup", "Jalapeños"]
selections = st_mui_multiselect(options, size=10)
st.markdown("You selected %s" % ", ".join(selections))
