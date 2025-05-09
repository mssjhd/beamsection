import streamlit as st

st.title("Reinforcement Bar Calculator")

# Initialize session state defaults only once
if "b" not in st.session_state:
    st.session_state.b = 600
    st.session_state.h = 300
    st.session_state.cover = 30
    st.session_state.bar_bottom = 16
    st.session_state.num_bar_bottom = 6
    st.session_state.bar_top = 12
    st.session_state.num_bar_top = 6
    st.session_state.stirrups = 8

with st.form("bar_input_form"):
    b = st.number_input("b (mm)", value=st.session_state.b, key="b")
    h = st.number_input("h (mm)", value=st.session_state.h, key="h")
    cover = st.number_input("cover (mm)", value=st.session_state.cover, key="cover")
    bar_bottom = st.number_input("Bar Bottom Diameter (mm)", value=st.session_state.bar_bottom, key="bar_bottom")
    num_bar_bottom = st.number_input("Number of Bottom Bars", value=st.session_state.num_bar_bottom, step=1, key="num_bar_bottom")
    bar_top = st.number_input("Bar Top Diameter (mm)", value=st.session_state.bar_top, key="bar_top")
    num_bar_top = st.number_input("Number of Top Bars", value=st.session_state.num_bar_top, step=1, key="num_bar_top")
    stirrups = st.number_input("Stirrups (mm)", value=st.session_state.stirrups, key="stirrups")

    submitted = st.form_submit_button("Calculate")

if submitted:
    total_bars = int(num_bar_bottom + num_bar_top)
    st.success(f"Total Bars = {total_bars}")
    
    # Show copyable code box (works on all devices)
    st.code(str(total_bars), language="text")
    st.info("📋 Copy the value above manually (works on mobile & desktop)")

    # Optionally attempt desktop clipboard copy
    try:
        import pyperclip
        pyperclip.copy(str(total_bars))
        st.success("✅ Total number of bars also copied to clipboard (desktop only).")
    except:
        st.warning("⚠️ Could not copy to clipboard (this is expected on mobile or web deployment).")

