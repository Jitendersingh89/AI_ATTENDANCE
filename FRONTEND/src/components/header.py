import base64
import os
import streamlit as st


def get_image_base64(file_path):
    """Converts a local image file into a Base64 string for HTML embedding."""
    if os.path.exists(file_path):
        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        return f"data:image/png;base64,{encoded_string}"
    return ""


def header_home():
    # Use raw string (r"...") or double backslashes to avoid escape errors in Windows paths
    logo_path = r"C:\Users\abcfo\installation\first_project\deep learning\RL\PROJECTS\AI_ATTENDANCE\logo.png"

    # Convert image to Base64 data URI
    logo_data_uri = get_image_base64(logo_path)

    if not logo_data_uri:
        st.warning(f"Logo not found at {logo_path}")

    # Fixed syntax errors in CSS string (removed improper commas inside inline styles)
    st.markdown(
        f""" 
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 30px; margin-top: 30px;">
            <img src="{logo_data_uri}" style="height: 100px;" alt="Logo"/>
           <h1 style="margin: 0; padding: 0; line-height: 0.85; color: #1A2B3C ; letter-spacing: 2px;">FLASH</h1>
           <h1 style="margin: 0; padding: 0; line-height: 0.85; color: #1A2B3C ;letter-spacing: 4px; padding-left: 4px;">CLASS</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )


    
def header_dashboard():
    logo_path = r"C:\Users\abcfo\installation\first_project\deep learning\RL\PROJECTS\AI_ATTENDANCE\logo.png"
    logo_data_uri = get_image_base64(logo_path)

    if not logo_data_uri:
        st.warning(f"Logo not found at {logo_path}")

    st.markdown(
        f""" 
        <div style="display: flex; align-items: center; justify-content: center; gap: 15px; margin-bottom: 20px;">
            <img src="{logo_data_uri}" style="height: 65px;" alt="Logo"/>
            <div style="display: flex; flex-direction: column; justify-content: center;">
                <h2 style="margin: 0; padding: 0; line-height: 0.85; color: #1A2B3C; letter-spacing: 2px;">FLASH</h2>
                <h2 style="margin: 0; padding: 0; line-height: 0.85; color: #1A2B3C; letter-spacing: 4px; padding-left: 2px;">CLASS</h2>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )