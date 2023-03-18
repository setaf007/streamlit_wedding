import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image, ImageDraw
import time
import base64

st.set_page_config(page_title='Floor Seating Plan', page_icon='🤍')

st.write("<center><span style='font-size: 60px; font-family: Allura; color: white; text-shadow: 3px 3px black;'>WELCOME</span></center>", unsafe_allow_html=True)
st.write("<center><span style='font-size: 25px; font-family: Allura; color: pink; text-shadow: 3px 3px black;'>TO THE WEDDING OF</span></center>", unsafe_allow_html=True)
st.write("<center><span style='font-size: 35px; font-family: Allura; color: white; text-shadow: 3px 3px black;'>M AHMED TUSHAR</span></center>", unsafe_allow_html=True)
st.write("<center><span style='font-size: 20px; font-family: Allura; color: pink; text-shadow: 3px 3px black;'>&</span></center>", unsafe_allow_html=True)
st.write("<center><span style='font-size: 35px; font-family: Allura; color: white; text-shadow: 3px 3px black;'>SUROVI ISLAM</span></center>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("<center><span style='font-size: 30px; font-family: Allura; color: pink; text-shadow: 3px 3px black;'>Please enter phone number for seating information</span></center>", unsafe_allow_html=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(
            rgba(0, 0, 0, 0.5),
            rgba(0, 0, 0, 0.5)
        ), url(data:image/png;base64,{encoded_string.decode()});
        background-size: cover;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('holudpic.jpg')

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       header {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


excel_file = 'Tushars guest list.xlsx'
sheet_name = 'QR Code data'
floorplan = Image.open('floorplan.png')

number = st.text_input('Enter phone number')



df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:C',
                   header=0)
df = df.astype({'Phone Number':'str'})

# Define a function to draw a circle on the image
def draw_circle(image, xy, radius, color, thickness=1):
    draw = ImageDraw.Draw(image)
    draw.ellipse((xy[0]-radius, xy[1]-radius, xy[0]+radius, xy[1]+radius), outline=color, width=thickness)

#dict with table locations
table_locations = {
    1: (215, 182), 2: (155, 182), 3: (90, 182), 4: (28, 187), 5: (215, 246), 6: (153, 249), 7: (92, 251), 8: (28, 248), 9: (214, 308), 10: (151, 306),
    11: (215, 366), 12: (155, 368), 13: (94, 362), 14: (29, 360), 15: (214, 432), 16: (153, 433), 17: (97, 425), 18: (32, 427), 19: (215, 492), 20: (151, 492),
    21: (219, 553), 22: (156, 551), 23: (97, 527), 24: (32, 526), 25: (219, 616), 26: (155, 616), 27: (97, 594), 28: (33, 594), 29: (218, 676), 30: (155, 675),
    31: (98, 692), 32: (215, 734), 33: (155, 738), 34: (99, 758), 35: (36, 722), 36: (317, 184), 37: (379, 183), 38: (441, 186), 39: (506, 183), 40: (318, 247),
    41: (381, 250), 42: (442, 251), 43: (506, 252), 44: (316, 310), 45: (378, 311), 46: (319, 368), 47: (378, 371), 48: (438, 355), 49: (503, 356), 50: (318, 433),
    51: (381, 434), 52: (442, 423), 53: (507, 423), 54: (316, 492), 55: (378, 493), 56: (321, 555), 57: (384, 556), 58: (438, 524), 59: (503, 526), 60: (323, 617),
    61: (383, 619), 62: (442, 589), 63: (507, 593), 64: (316, 677), 65: (382, 676), 66: (443, 691), 67: (320, 739), 68: (382, 738), 69: (444, 756), 70: (500, 723)
}

if st.button('Enter'):
    if number in df['Phone Number'].values:
        progress_text = "Fetching your designated table."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)

        table_number = df.loc[df['Phone Number'] == number, 'Table Number'].values[0]
        name = df.loc[df['Phone Number'] == number, 'Name'].values[0]

        if table_number in table_locations:
            draw_circle(floorplan, table_locations[table_number], 40, "blue", thickness=5)

        if table_number == '20 and 21':
            draw_circle(floorplan, table_locations[20], 40, "blue", thickness=5)
            draw_circle(floorplan, table_locations[21], 40, "blue", thickness=5)
        if table_number == '30 and 31':
            draw_circle(floorplan, table_locations[30], 40, "blue", thickness=5)
            draw_circle(floorplan, table_locations[31], 40, "blue", thickness=5)
        if table_number == '34 and 35':
            draw_circle(floorplan, table_locations[34], 40, "blue", thickness=5)
            draw_circle(floorplan, table_locations[35], 40, "blue", thickness=5)
        if table_number == '51 and 52':
            draw_circle(floorplan, table_locations[51], 40, "blue", thickness=5)
            draw_circle(floorplan, table_locations[52], 40, "blue", thickness=5)
        if table_number == '69 and 70':
            draw_circle(floorplan, table_locations[69], 40, "blue", thickness=5)
            draw_circle(floorplan, table_locations[70], 40, "blue", thickness=5)


        st.write("")
        st.write("")
        st.write("")
        st.write("<center><span style='font-size: 30px; font-family: Allura; color: white; text-shadow: 3px 3px black;'>Enjoy the Wedding celebration!</span></center>", unsafe_allow_html=True)
        st.write("<center><span style='font-size: 30px; font-family: Allura; color: white; text-shadow: 3px 3px black;'> ", name, "</span></center>", unsafe_allow_html=True)
        st.write("<center><span style='font-size: 30px; font-family: Allura; color: white; text-shadow: 3px 3px black;'>Please proceed to table number</span></center>", unsafe_allow_html=True)
        st.write("<center><span style='font-size: 50px; font-family: Allura; color: gold; text-shadow: 3px 3px black;'><b> ", table_number, "</b></span></center>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")
        st.image(floorplan, caption='Floorplan in OCC', use_column_width=True)
        st.write("<center><span style='font-size: 30px; font-family: Allura; color: white; text-shadow: 3px 3px black;'>Copyright ©️ HanKin Software, 2023</span></center>", unsafe_allow_html=True)

    else:
        st.write("Your Phone number was not found. Please proceed to the counter for assistance!")

