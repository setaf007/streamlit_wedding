import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image, ImageDraw
import time

st.set_page_config(page_title='Floor Seating Plan', page_icon='🤍')

st.write("<center><span style='font-size: 100px; font-family: Allura;'>WELCOME</span></center>", unsafe_allow_html=True)
st.write("<center><span style='font-size: 25px; font-family: Allura;'>TO THE WEDDING OF</span></center>", unsafe_allow_html=True)
st.write("<center><span style='font-size: 40px; font-family: Allura;'>M AHMED TUSHAR</span></center>", unsafe_allow_html=True)
st.write("<center><span style='font-size: 20px; font-family: Allura;'>&</span></center>", unsafe_allow_html=True)
st.write("<center><span style='font-size: 40px; font-family: Allura;'>SHUROBI ISLAM</span></center>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("<center><span style='font-size: 30px; font-family: Allura;'>Please enter phone number for seating information</span></center>", unsafe_allow_html=True)

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


excel_file = 'seating_plan.xlsx'
sheet_name = 'sheets'
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

        st.write("")
        st.write("")
        st.write("")
        st.write("<center><span style='font-size: 40px; font-family: Allura;'>Enjoy the Wedding celebration!</span></center>", unsafe_allow_html=True)
        st.write("<center><span style='font-size: 30px; font-family: Allura;'> ", name, "</span></center>", unsafe_allow_html=True)
        st.write("<center><span style='font-size: 40px; font-family: Allura;'>Please proceed to table number ", table_number, "!</span></center>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")
        st.image(floorplan, caption='Floorplan in OCC', use_column_width=True)

    else:
        st.write("Your Phone number is invalid or not given")

