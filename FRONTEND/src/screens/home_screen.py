import os
import streamlit as st
from PIL import Image
from src.components.footer import footer_home
from src.components.header import header_home
from src.ui.base_layout import (
    style_background_dashboard,
    style_background_home,
    style_base_layout,
)


def home_screen():
    header_home()
    style_background_dashboard()
    style_background_home()
    style_base_layout()

    # Goes up two levels from src/screens -> src -> AI_ATTENDANCE
    IMAGE_PATH = os.path.normpath(
        os.path.join(
            os.path.dirname(__file__), "..", "..", "student.png.png"
        )
    )
    IMAGE_PATH_2 = os.path.normpath(
         os.path.join(
            os.path.dirname(__file__), "..", "..", "teacher.png"
         )
      )

    image_exists = os.path.exists(IMAGE_PATH)
    if not image_exists:
        st.error(f"Image not found at {IMAGE_PATH}")

    col1, col2 = st.columns(2)

    with col1:
        st.header("I m Student")
        if image_exists:
            st.image(IMAGE_PATH, width=175)

        if st.button("Student portal", type="primary"):
            st.session_state["login_type"] = "student"
            st.rerun()

    with col2:
        st.header("I m Teacher")
        if image_exists:
            st.image(IMAGE_PATH_2, width=120)

        if st.button(
            "Teacher portal",
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right",
        ):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    footer_home()