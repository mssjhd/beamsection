import streamlit as st
import pyperclip

st.title("Reinforcement Bar Calculator")

with st.form("bar_input_form"):
    b = st.number_input("b (mm)", value=300)
    h = st.number_input("h (mm)", value=500)
    cover = st.number_input("cover (mm)", value=25)
    bar_bottom = st.number_input("Bar Bottom Diameter (mm)", value=16)
    num_bar_bottom = st.number_input("Number of Bottom Bars", value=3, step=1)
    bar_top = st.number_input("Bar Top Diameter (mm)", value=12)
    num_bar_top = st.number_input("Number of Top Bars", value=2, step=1)
    stirrups = st.number_input("Stirrups (mm)", value=8)

    submitted = st.form_submit_button("Calculate")

    if submitted:
        total_bars = int(num_bar_bottom + num_bar_top)
        st.success(f"Total Bars = {total_bars}")
        
        # Copy to clipboard using pyperclip
        try:
            pyperclip.copy(str(total_bars))
            st.info("✅ Total number of bars copied to clipboard!")
        except:
            st.warning("⚠️ Could not copy to clipboard. Make sure you're running this locally and pyperclip is supported.")
