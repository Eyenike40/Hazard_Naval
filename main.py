# Import Required Packages
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
from annotated_text import annotated_text
import Spill_and_fall
import Electrical
import Mooring_Operation
import Ship_flooding
import Fire



# Create the data for the graph
data = {'Accident Type': ['Slip and fall', 'Capsize/Listing', 'Cargo Handling Failure', 'Mooring operation Accident', 'Hazardous incidents', 'Escape of Harmful Substance', 'Contact', 'Foundering', 'Electrical Accident', 'Ship Flooding/Water Ingress', 'Heavy Weather Damage', 'Hull Failure', 'Fire Accidents', 'Missing Vessel', 'Capsize/Listing', 'Pollution'],
        'Number of Accidents': [8848, 390, 110, 1566, 1310, 110, 593, 524, 1802, 1425, 86, 39, 1390, 6, 926, 50],
        'Percentage of Occurrence (%)': [46.14, 2.03, 0.57, 8.17, 6.83, 0.57, 3.09, 2.73, 9.40, 7.43, 0.45, 0.20, 7.25, 0.03, 4.83, 0.26]}
df = pd.DataFrame(data)
df = df.sort_values('Number of Accidents', ascending=True)  # sort data in ascending order
df1 = df.sort_values('Number of Accidents', ascending=False)  # sort data in descending order

# Create the data for the ship names
ship_names = ['NNS OKPABANA', 'NNS THUNDER', 'NNS UNITY', 'NNS OLOGBO', 'NNS NWABA', 'NNS KYANWA', 'NNS OBULA', 'NNS MAKURDI', 'NNS BURUTU', 'NNS SAGBAMA', 'NNS ANDONI']
ship_df = pd.DataFrame(ship_names, columns=['Name'])

def main():

    # Title of the Project
    col1, col2 = st.columns((3,1.4))

    col1.write("# Naval Ship Risk Assessment App")

    ship_image = Image.open("naval_ship.jpg")
    with col2:
        col2.text("")
        col2.image(ship_image)

    st.write("")
    st.write("")

    st.sidebar.title("Navigation Bar")
    st.sidebar.write("Navigate through the site by selecting the area of interest")
    nav_opt = st.sidebar.selectbox("Select to Navigate", ["Home", "Slip and Fall Accidents", "Electrical Accidents", "Mooring Operations", "Ship Flooding", "Fire Accidents"])
    
    ship_sidebar_image = Image.open("naval_ship.jpg")
    st.sidebar.image(ship_sidebar_image)

    st.sidebar.title("Ships Operating in Base")
    st.sidebar.dataframe(ship_df)

    if nav_opt == "Home":
        annotated_text(("Naval Ship Risk Assessment App", "", "#000000", "#00FF00"))
        st.write("""
        Naval Ship Risk Assessment provides a comprehensive means of identifying and quantifying potential 
        hazards which may pose a risk to personnel and equipment on the ship. The outcomes of this risk 
        assessment enables organizations to develop appropriate preventive and protective measures.
        """)
        st.write("")
        st.write("")
        st.write("")
        # Create and display the graph
        fig = px.bar(df, y='Accident Type', x='Number of Accidents', orientation='h', text='Percentage of Occurrence (%)', title='The Most Common Accidents onboard Naval Ships', labels={'Number of Accidents':'Number of Accidents', 'Accident Type':'Accident Type'}, color='Percentage of Occurrence (%)', height=700)
        fig.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
        fig.update_layout(title_font_size=18, xaxis_title_font_size=18, yaxis_title_font_size=18, autosize=False)
        st.plotly_chart(fig)
        # Add an expander for explaining the graph and listing the 5 most prevalent accidents
        with st.expander("See Explanation & The 5 Most Prevalent Accidents"):
            st.write("""
            The graph above represents the most common types of accidents occurring on naval ships. 
            The number of accidents per type is presented, along with the percentage of occurrence. 
            Here are the five most prevalent accidents:
            """)
            for i in range(5):
                st.write(f"{i+1}. {df1.iloc[i]['Accident Type']} with {df1.iloc[i]['Number of Accidents']} accidents.")

        annotated_text(("Source: (Naval Safety Ledger, 2010-2019)", "", "#000000", "#FF0000"))
        st.write("")
        st.write("")
        st.write("")
        st.write("")

       
        col1 , col2 = st.columns((1,1))
        col1.subheader("Slip/Fall Accident Hazards")
        col2.subheader("Electrical Accident Hazards")
        with col1.container():
                st.write("""
                🔴 Consumption of Alcohol and hard-drugs.\n
                🔴 Working at height.\n
                🔴 Unsafe behaviour due to fatigue.\n
                🔴 Poor warning signage.\n
                🔴 Ship manoeuvre errors.\n
                🔴 Improper use of safety equipment.\n
                🔴 Slippery deck.\n
                🔴 Lack of safety awareness and conscious.\n
                🔴 Violation of the rules of accident prevention in ship.\n
                🔴 Poor weather condition.\n
                🔴 Poor visibility.\n
                """)

        with col2.container():
                st.write("""
                🔴 Poor electrical connections\n
                🔴 Unsafe behaviour due to fatigue\n
                🔴 Poor warning signage\n
                🔴 Exposure to unsafe electrical surface\n
                🔴 Lack of personal protection equipment\n
                🔴 Poorly Insulated live Electrical-wires\n
                🔴 Working at confine space\n
                🔴 Moisture on electric circuits\n
                🔴 Lack of safety awareness and conscious\n
                🔴 Violation of the rules of accident on-board\n 
                🔴	Improper use of safety equipment\n
                🔴	Alcohol and drugs\n
                """)
        st.write("")
        st.write("")
        col1 , col2 = st.columns((1,1))
        col1.subheader("Mooring Operation Accident Hazards")
        col2.subheader("Ship Flooding/Water Ingress Accident Hazards")
        with col1.container():
                st.write("""
                🔴 Improper positioning and posture while working\n
                🔴 Unsafe behaviour due to fatigue\n
                🔴 Poor warning signage\n 
                🔴 Alcohol and drugs\n
                🔴 Improper use of safety equipment\n
                🔴 Lack of personal protection equipment\n
                🔴 Lack of safety awareness and consciousness\n
                🔴 Violation of rules of accidents preventions\n 
                🔴 Unsafe handling of equipment and machines\n 
                🔴 Poor work schedule\n
                """) 


        with col2.container():
                st.write("""
                🔴 Cabinet Leakage due to rusting\n 
                🔴 Cabinet Leakage due to chemical \n
                🔴 Cabinet Leakage due to explosion\n
                🔴 Adverse  Weather\n 
                🔴 Corrosion attack\n
                🔴 Collision \n
                """)

        st.write("")
        st.write("")
        col1, col2 = st.columns((1, 1))
        col1.subheader("Fire Accident Hazards")
        with col1.container():
                st.write("""
                🔴 Working at confined space\n
                🔴 Unsafe behaviour due to fatigue\n
                🔴 Lack of safety awareness and consciousness\n
                🔴 Inappropriate use of electrical equipment\n
                🔴 Poor electrical connections\n
                🔴 Exposed hot surfaces\n
                🔴 Poor warming Signage\n
                🔴 Alcohol and drugs\n
                🔴 Improper use of safety equipment\n	
                🔴 Violation of rules of accident prevention\n
                🔴 Unsafe handling of Flammables\n
                🔴	Un-Insulated live-wires\n
                🔴	Unsafe handling of explosive/armaments\n
                """) 



    elif nav_opt == "Slip and Fall Accidents":
        # Add your functionalities here
        Spill_and_fall.conventional_risk()
    elif nav_opt == "Electrical Accidents":
        # Add your functionalities here
        Electrical.conventional_risk()
    elif nav_opt == "Mooring Operations":
        # Add your functionalities here
        Mooring_Operation.conventional_risk()
    elif nav_opt == "Ship Flooding":
        # Add your functionalities here
         Ship_flooding.conventional_risk()
    elif nav_opt == "Fire Accidents":
        # Add your functionalities here
        Fire.conventional_risk()

if __name__ == "__main__":
    main()
