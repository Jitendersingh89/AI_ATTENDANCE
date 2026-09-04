import streamlit as st


def footer_home():
    st.markdown(
        """ 
        <div style="display: flex; justify-content: center; align-items: center; margin-top: 40px; padding-bottom: 20px;">
            <p style="font-family: 'Outfit', sans-serif; font-size: 14px; color: #475569; margin: 0; font-weight: 500;">
                Created by Jitender Singh
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def footer_dashboard():
    st.markdown(
        """ 
        <div style="display: flex; justify-content: center; align-items: center; margin-top: 40px; padding-bottom: 20px;">
            <p style="font-family: 'Outfit', sans-serif; font-size: 14px; color: #000000 ; margin: 0; font-weight: 500;">
                Created by Jitender Singh
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )