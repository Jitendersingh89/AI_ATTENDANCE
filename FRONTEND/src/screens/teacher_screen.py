import streamlit as st
from src.components.footer import footer_dashboard
from src.components.header import header_dashboard
from src.screens.home_screen import home_screen
from src.ui.base_layout import style_background_dashboard, style_base_layout


def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if (
        "teacher_login_type" not in st.session_state
        or st.session_state.teacher_login_type == "login"
    ):
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()


def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button(
            "Go back to home", shortcut="Ctrl+Backspace", key="back_home_login"
        ):
            st.session_state["login_type"] = "home"
            st.rerun()

    st.markdown(
        "<h2 style='text-align: center;'>Login using Password</h2>",
        unsafe_allow_html=True,
    )

    teacher_username = st.text_input(
        "Enter the username", placeholder="ananyaroy", key="login_user"
    )
    teacher_pass = st.text_input(
        "Enter the password", type="password", key="login_pass"
    )
    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button(
            "Login",
            shortcut="Enter",
            use_container_width=True,
            key="btn_login",
        ):
            pass
    with btnc2:
        if st.button(
            "Register",
            shortcut="Ctrl+Enter",
            use_container_width=True,
            type = "primary",
            key="btn_goto_reg",
        ):
            st.session_state["teacher_login_type"] = "register"
            st.rerun()

    footer_dashboard()


def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button(
            "Go back to home", shortcut="Ctrl+Backspace", key="back_home_reg"
        ):
            st.session_state["login_type"] = "home"
            st.rerun()

    st.markdown(
        "<h2 style='text-align: center;'>Register Teacher Profile</h2>",
        unsafe_allow_html=True,
    )

    teacher_username = st.text_input(
        "Enter the username", placeholder="ananyaroy", key="reg_user"
    )
    teacher_name = st.text_input(
        "Enter name", placeholder="Ananya Roy", key="reg_name"
    )
    teacher_pass = st.text_input(
        "Enter the password",
        type="password",
        placeholder="Enter the password",
        key="reg_pass",
    )
    teacher_pass_confirm = st.text_input(
        "Confirm your password",
        type="password",
        placeholder="Enter the password to confirm",
        key="reg_pass_conf",
    )
    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button(
            "Register now",
            shortcut="Ctrl+Enter",
            use_container_width=True,
            key="btn_goto_login",
        ):
            st.session_state["teacher_login_type"] = "login"
            st.rerun()
    with btnc2:
        if st.button(
            "Login Instead",
            type = "primary",
            use_container_width=True,
            key="btn_register",
        ):
            st.session_state.teacher_login_type = 'login'

    footer_dashboard()