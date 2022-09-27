import streamlit as st

from st_mui_multiselect import st_mui_multiselect

st.subheader("Demo of Streamlit Material UI Multiselect Component")

options = ["Mayo", "Lettuce", "Pickles", "Tomatoes", "Onions", "Mushrooms", "Ketchup", "Jalapeños"]
select_size = st.slider(
    "The size can be adjusted",
    1,
    10,
    4,
)
st.write("Select options below. Hold ⌘ on Mac or [Ctrl] on windows to select multiple.")
selections = st_mui_multiselect(options, size=select_size)
st.markdown("You selected %s" % ", ".join(selections))

with st.form("try_a_form"):
    sel_size = st.slider(
        "The size can be adjusted",
        1,
        10,
        4,
    )
    st.write("Select options below. Hold ⌘ on Mac or [Ctrl] on windows to select multiple.")
    sel = st_mui_multiselect(options, size=sel_size, key="second")
    sub = st.form_submit_button("Submit")
    if sub:
        st.write("You selected %s" % ", ".join(sel))
