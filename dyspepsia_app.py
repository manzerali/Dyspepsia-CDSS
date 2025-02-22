import streamlit as st

# Set page config
st.set_page_config(page_title="Dyspepsia CDSS", layout="wide")

# Title with disclaimer
st.markdown("<h1 style='text-align: center; color: #2E8B57;'>Dyspepsia Clinical Decision Support System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>⚠ This is an experimental clinical decision model intended **only for use by doctors**. Not for direct patient use.</p>", unsafe_allow_html=True)
st.markdown("---")

def dyspepsia_cdss():
    # Step 1: Alarm Symptoms
    st.write("## **Step 1: Check for Alarm Symptoms**")
    st.info("""
    **Why is this important?**  
    Alarm symptoms suggest **serious pathology** such as:  
    - **Gastric cancer** (especially in older patients)  
    - **Peptic ulcer complications (e.g., bleeding, perforation)**  
    - **Esophageal strictures or malignancy**  

    **Next Step:** If alarm symptoms are present, urgent **esophagogastroduodenoscopy (EGD)** is required.
    """)
    alarm_symptoms = st.radio("❗ Does the patient have **alarm symptoms**?", ["Yes", "No"])
    if alarm_symptoms == "Yes":
        st.error("🔴 **Urgent Endoscopy Needed! Refer immediately.**")
        return

    # Step 2: NSAID Use
    st.write("## **Step 2: Assess NSAID Use**")
    nsaid_use = st.radio("💊 Is the patient taking **NSAIDs or aspirin** regularly?", ["Yes", "No"])
    if nsaid_use == "Yes":
        st.warning("⚠ **Stop NSAIDs if possible and start PPI therapy for at least 8 weeks.**")

    # Step 3: GERD vs. Dyspepsia
    st.write("## **Step 3: GERD vs. Dyspepsia**")
    gerd_symptoms = st.radio("🔥 Does the patient have **classic GERD symptoms**?", ["Yes", "No"])
    if gerd_symptoms == "Yes":
        st.success("✅ **Start an 8-week PPI trial.**")
        return

    # Step 4: H. pylori Testing Considerations
    st.write("## **Step 4: H. pylori Testing Considerations**")
    recent_ppi = st.radio("🛑 Has the patient taken **a PPI in the last 2 weeks**?", ["Yes", "No"])
    if recent_ppi == "Yes":
        st.warning("⚠ **Stop PPI for 2 weeks before H. pylori testing to avoid false negatives.**")

    # Step 5: H. pylori Eradication Therapy
    st.write("## **Step 5: H. pylori Eradication Therapy**")
    hpylori = st.radio("📌 Is the patient H. pylori positive?", ["Yes", "No"])
    if hpylori == "Yes":
        st.success("✅ **Start eradication therapy:**")
        st.markdown("""
        **Triple Therapy (14 days) - First Line:**  
        - PPI (Omeprazole 20 mg BID) + Clarithromycin 500 mg BID + Amoxicillin 1 g BID  

        **Quadruple Therapy (for resistance or previous failure):**  
        - PPI (Omeprazole 20 mg BID) + Bismuth subsalicylate 525 mg QID + Metronidazole 500 mg TID + Tetracycline 500 mg QID  
        """)

    # Step 6: Functional Dyspepsia
    st.write("## **Step 6: Functional Dyspepsia**")
    persistent_symptoms = st.radio("🔄 Do symptoms persist after **H. pylori eradication or PPI trial**?", ["Yes", "No"])
    if persistent_symptoms == "No":
        st.success("✅ **Continue maintenance therapy if needed.**")
        return

    # Step 7: Lifestyle Modifications
    st.write("## **Step 7: Lifestyle Modifications & Risk Factors**")
    st.markdown("""
    - **🛑 NSAID Use?** Stop NSAIDs and initiate PPI therapy.  
    - **🥗 Diet?** Avoid fatty/spicy foods, caffeine, alcohol. Consider a **low-FODMAP diet** for functional dyspepsia.  
    - **🚬 Smoking & Alcohol?** Encourage cessation.  
    """)

    # Step 8: Managing Refractory Dyspepsia
    st.write("## **Step 8: Managing Refractory Dyspepsia**")
    st.info("""
    **If symptoms persist despite PPI and H. pylori treatment, consider:**  
    - **Neuromodulators:** Mirtazapine, Buspirone, SSRIs (for visceral hypersensitivity).  
    - **Gastric emptying studies** (if gastroparesis suspected, especially in diabetics).  
    - **Esophageal manometry or pH monitoring** (if atypical reflux symptoms).  
    """)

    # Step 9: Post-Treatment Follow-Up
    st.write("## **Step 9: Post-Treatment Follow-Up & Monitoring**")
    st.info("""
    - **H. pylori retesting**: UBT or stool antigen **4 weeks after therapy completion**.  
    - **Stepping down PPI therapy**: Gradual dose reduction to prevent rebound acid hypersecretion.  
    - **Long-term PPI risks**: Increased risk of osteoporosis, kidney disease, and infections.  
    """)

    # Step 10: Special Populations
    st.write("## **Step 10: Special Populations & Considerations**")
    st.markdown("""
    - **Pregnancy:** Sucralfate is safest; PPIs are category B (except omeprazole - category C).  
    - **Elderly:** Avoid long-term PPIs due to fracture risk. Consider H2 blockers.  
    - **Diabetes:** High prevalence of gastroparesis. Consider **prokinetics like metoclopramide.**  
    """)

# Run the CDSS function
dyspepsia_cdss()

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>⚠ This is an experimental clinical decision model intended **only for use by doctors**.</p>", unsafe_allow_html=True)
