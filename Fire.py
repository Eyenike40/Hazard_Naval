import streamlit as st
import pandas as pd
from annotated_text import annotated_text
import matplotlib.pyplot as plt


def conventional_risk():
    annotated_text(("Risk Analysis", "", "#000000", "#00FF00"))
    st.write("")
    # Step 1: Load the Excel files
    annotated_text(("Import Excel Files", "", "#000000", "#FFFF00"))
    hazard_file = st.file_uploader("Upload the 'Fire Hazard' file", type=['xlsx'])
    consequence_file = st.file_uploader("Upload the 'Fire Consequence' file", type=['xlsx'])
    st.write("")
    st.write("")

    if hazard_file and consequence_file:
        hazard_df = pd.read_excel(hazard_file)
        consequence_df = pd.read_excel(consequence_file)

        # Step 2: Compute average scores for hazards and consequences
        hazard_avg_scores = hazard_df.iloc[:, 1:].mean().tolist()
        consequence_avg_scores = consequence_df.iloc[:, 1:].mean().tolist()

        # Step 3: Compute risk score
        risk_scores = [h * c for h, c in zip(hazard_avg_scores, consequence_avg_scores)]

        # Step 4: Associate each risk score with its hazard
        hazards = [
            "Working at confined space",
            "Unsafe behaviour due to fatigue",
            "Lack of safety awareness and consciousness",
            "Inappropriate use of electrical equipment",
            "Poor electrical connections",
            "Exposed hot surfaces",
            "Poor warming Signage",
            "Alcohol and drugs",
            "Improper use of safety equipment",
            "Violation of rules of accident prevention",
            "Unsafe handling of Flammables",
            "Un-Insulated live-wires",
            "Unsafe handling of explosive/armaments"
        ]

        # Step 5: Create a dataframe to tabulate risk scores and hazards
        risk_df = pd.DataFrame({
            'Hazard': hazards,
            'Risk Score': risk_scores
        })

        # Add rank column
        risk_df['Rank'] = risk_df['Risk Score'].rank(ascending=False)

        # Step 6: Display the result
        st.write("#### Risk Score For HazardFire Accident")
        annotated_text(("Conventional Method", "", "#000000", "#FFFF00"))
        st.dataframe(risk_df)

        # Define the weights for each officer
        weights = {'EX1': 0.4, 'EX2': 0.3, 'EX3': 0.2, 'EX4': 0.1}

        # Assign weights to officers in the dataframe
        hazard_df['Weights'] = hazard_df['Officers'].map(weights)
        consequence_df['Weights'] = consequence_df['Officers'].map(weights)

        # Compute average scores for hazards and consequences for each officer
        hazard_avg_scores = (hazard_df.iloc[:, 1:-1].multiply(hazard_df['Weights'], axis=0)).mean()
        consequence_avg_scores = (consequence_df.iloc[:, 1:-1].multiply(consequence_df['Weights'], axis=0)).mean()

        # Compute risk score for each officer and hazard
        risk_scores = hazard_avg_scores * consequence_avg_scores

        # Create a dataframe to tabulate average risk scores and hazards
        risk_df_weighted = pd.DataFrame({
            'Hazard': hazards,
            'Weighted Risk Score': risk_scores.values
        })

        # Add rank column
        risk_df_weighted['Weighted Rank'] = risk_df_weighted['Weighted Risk Score'].rank(ascending=False)

        # Display the result
        annotated_text(("Weighted Risk Method", "", "#000000", "#FFFF00"))
        st.dataframe(risk_df_weighted)

        # Plot the ranks of the two methods
        st.write("")
        annotated_text(("Comparison of Risk Ranks for Conventional and Weighted Method", "", "#000000", "#FFFF00"))
        fig, ax = plt.subplots()

        ax.plot(risk_df['Hazard'], risk_df['Rank'], label='Conventional Method', marker="o", markerfacecolor="white", markeredgecolor="red", color="red", lw=0.75, linestyle="--")
        ax.plot(risk_df_weighted['Hazard'], risk_df_weighted['Weighted Rank'], label='Weighted Method', marker="s", markerfacecolor="white", markeredgecolor="blue", color="blue", lw=0.75)

        ax.set_xlabel('Hazard', labelpad=10)
        ax.set_ylabel('Rank', labelpad=10)
        ylim1, ylim2 = ax.get_ylim()
        ax.set_ylim(ylim1, ylim2*1.25)
        ax.set_axisbelow("True")
        ax.grid(axis="y", linestyle="--", lw=0.5, alpha=0.6)
        ax.set_xticklabels(["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "F13"])
        ax.set_title('Risk Rank Comparison')
        ax.legend()

        st.pyplot(fig)


      
