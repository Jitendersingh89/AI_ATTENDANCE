import streamlit as st


def style_background_home():
   st.markdown(
        """
        <style>
        .stApp {
            background: #FFDBFE !important;
        }

        /* Target each individual column box */
        div[data-testid="stColumn"] {
            background-color: #FFFFFF !important;
            padding: 2.5rem !important;
            border-radius: 1.5rem !important; /* Set to 0rem for sharp square corners */
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05) !important;
            text-align: center !important;
        }
        </style>
        """,
        unsafe_allow_html=True,)

def style_background_dashboard():
    st.markdown(
        """
        <style>
        .stApp {
            background: #FFDBFE !important;
        }

        
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def style_base_layout():

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Lilita+One&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Lilita+One&family=Oswald:wght@200..700&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Lilita+One&family=Oswald:wght@200..700&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Lilita+One&family=Oswald:wght@200..700&family=Outfit:wght@100..900&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');


          /* Hide Top Bar of streamlit */

            #MainMenu, footer, header{
                  visibility: hidden;
            }

            .block-container{
                padding-top: 1.5rem !important;
            }

            h1{
            
                font-family: "Lilita One", sans-serif !important;
                font-weight: 400 !important;
                font-style: normal !important;
                font-size: 4rem !important;
            }


            h2{
             
                font-family: "Lilita One", sans-serif !important;
                font-style: normal !important;
                font-size: 3rem !important;
                line-height:0.9 !important;
                margin-bottom: 0rem !important;
                color: #1E3A8A !important;
            }

            h3 , h4 , p {
                font-family: 'Outfit' , sans-serif;

            }

            button{
                border-radius: 1.5rem !important;
                background: #3B82F6 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind ="secondary"]{
                border-radius: 1.5rem !important;
                background: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }
             button[kind ="tertiary"]{
                border-radius: 1.5rem !important;
                background: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform:scale(1.05)
            }

        

        </style>
            """ , unsafe_allow_html= True)