import streamlit as st

#===================================== 
# PAGE CONFIG
#===================================== 
st.set_page_config(
    page_title="Temperature Calculator",
    page_icon="🌡️",
    layout="centered"
)

#===================================== 
#   LOAD FILE CSS
#===================================== 
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#===================================== 
#   HEADER
#===================================== 
st.markdown("""
<div class="title">
    🌡️ Temperature Calculator
</div>
<div class="subtitle">
    General Process Engineering Tool
</div>
""", unsafe_allow_html=True )

#===================================== 
#   INPUT CARD
#===================================== 
st.markdown('<div class="card">', unsafe_allow_html=True)

m_dot = st.number_input("Mass Flow Rate (kg/s)", min_value=0.01, value=2.0)
cp = st.number_input("Specific heat Cp (kJ/kg.°C)", min_value=0.01, value=4.18)     
Q = st.number_input ("Heat Duty Q (KW)", value=50.0)     
t_in = st.number_input ("Inlet Temperature (°C)", value=30.0)  

st.markdown('</div>', unsafe_allow_html=True)

#===================================== 
#   CALCULATION
#===================================== 
st.markdown("<br>", unsafe_allow_html=True)

if st.button(" 🔍 Calculate"):
    t_out = t_in + Q / (m_dot * cp)
   
    st.markdown(
        f"""
        <div class="result">
            🔥Outlet Temperature <br>
             <span>{t_out:.2f} °C</span>
        </div>
        """,  
        unsafe_allow_html=True
)

