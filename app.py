import streamlit as st
from detector import get_risk_score
import time

# Page Configuration
st.set_page_config(page_title="Phishing Shield Pro", page_icon="🛡️", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #008080; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# UI Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2906/2906274.png", width=150)
    st.title("Phishing Shield")
    st.write("---")
    st.info("**Tool Features:**\n- 🔍 Domain Age Analysis\n- 🛡️ Keyword Threat Detection\n- 🌐 IP Address Pattern Matching")

with col2:
    st.subheader("URL Security Scanner")
    url_input = st.text_input("Paste the URL below to check for threats:", placeholder="https://example.com")
    
    if st.button("🚀 Analyze Now"):
        if url_input:
            with st.spinner('Scanning for security threats...'):
                time.sleep(1.5) # Pro animation delay
                score = get_risk_score(url_input)
                
            # Displaying Risk Score
            st.write(f"### Risk Score: {score}%")
            st.progress(score / 100)
            
            # Logic for Warnings
            if score >= 70:
                st.error("🚨 CRITICAL DANGER: This link is highly suspicious!")
                st.write("Reason: Multiple phishing indicators found. Please avoid this site.")
            elif score >= 40:
                st.warning("⚠️ WARNING: Suspicious activity detected.")
                st.write("Reason: Some risk factors identified. Proceed with extreme caution.")
            else:
                st.success("✅ SAFE: No threats detected.")
                st.balloons()
                st.write("This website appears to be secure.")
        else:
            st.warning("Please enter a URL first!")

# Footer
st.write("---")
st.caption("Cybersecurity Project | Built with Python & Streamlit")