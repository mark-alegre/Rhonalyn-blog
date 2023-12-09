import base64
import plotly.express as px
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Rhona's Blog", page_icon="🥰", layout="wide")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()


img = get_img_as_base64("me.jpg")
page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-position: center; 
    background-repeat: no-repeat;
    background-size: 110%;
    background-attachment: local;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style.css")


# ---- HEADER SECTION ----

with st.container():
    cols1, cols2 = st.columns([3,1])
    with cols1:
        st.title("Hi there!, Welcome to my Blog🥳")
        st.write("---") 
        st.subheader("An Active Student of SNSU")
        st.write(
            "Being a role model is about being true to myself."
        )
    with cols2:
        st.image("me.png")
        st.write("[Learn More About](https://www.facebook.com/rhonalyn.mags.08)")
# ---- WHAT I DO ----
with st.container():
    st.write("---")
    st.title("📣Select Category📣")
    left_column, right_column = st.columns(2)
    with left_column:
         col1, col2 = st.columns(2)
        
    v1 = col1.button("About Me😎")
    if v1:
            with st.container():
                cal1, cal2 = st.columns(2)
            
            with cal1:
                st.image("me.png")
        
            with cal2:
            
                st.header("📝My Personal Info:")
                st.markdown("---")
                with open('sytle.css') as source_des:
                    st.markdown(f'<style>{source_des.read()}</style>', unsafe_allow_html=True)
                st.write("#")
                st.subheader("📝Full Name:")
                st.write(
                    """
                    - ✅ Rhonalyn B. Magdula
                    """
                    )
                st.subheader("📝Age & Birthday:")
                st.write(
                    """
                    - ✅ 19 Years Old
                    - ✅ December 18, 2023
                    """
                    )
                st.subheader("📝Address:")
                st.write(
                    """
                    - ✅ Rizal st, Washington, Surigao City
                    
                    """
                    )
            with st.container():
                st.markdown("---")
                st.subheader("📝School Attended:")
                st.write(
                        """
                        - ✅ SURIGAO DEL NORTE NATIONAL HIGHSCHOOL
                        
                        
                        """
                        )
                st.subheader("📝Status:")
                st.write(
                        """
                        - ✅ Single
                        
                        
                        """
                        )
    v2 = col2.button("Content📕")
    if v2:
            with st.container():
                col1, col2,  = st.columns(2)
                # Replace 'your_video_file1.mp4' and 'your_video_file2.mp4' with the paths to your video files
                with col1:
                   st.title("Modeling👄")
                   st.write("""
                             - Creating a website about modeling involves showcasing portfolios,
                             - tips, and possibly a blog section. Include high-quality images, contact information, and a bio for each model.
                             - Consider incorporating a user-friendly design for easy navigation
                             Modeling, in various contexts, refers to the process of creating a representation or simulation of a system, concept, or object to analyze, understand, or predict its behavior. 
                             - In the fashion industry, modeling involves individuals showcasing clothing or accessories to demonstrate style and aesthetic appeal     
                            
                            """)
                with col2:
                    st.image("model.jpg")
            st.write("[Read More >](https://www.pinterest.ph/pin/88453580172778786/)")
# ---- CONTACT ----
# ---- CONTACT ----
st.markdown("---")    
st.header(":mailbox: Get In Touch With Me!")
contact_form = """
        <form action="https://formsubmit.co/magdularhonalyn@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
        </form>
        """
st.markdown(contact_form, unsafe_allow_html=True)

 # Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("sytle.css")