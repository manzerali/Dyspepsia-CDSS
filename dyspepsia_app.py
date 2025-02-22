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
    **🔍 Why is this important?**  
    Alarm symptoms suggest **serious pathology** requiring urgent investigation, including:  
    - **Gastric cancer:** Persistent dyspepsia in older adults, weight loss, early satiety.  
    - **Peptic ulcer complications:** GI bleeding, perforation, anemia.  
    - **Esophageal malignancy or strictures:** Progressive dysphagia, odynophagia.  

    **Next Step:** If alarm symptoms are present, **urgent esophagogastroduodenoscopy (EGD) is required.**
    """)
    alarm_symptoms = st.radio("❗ Does the patient have **alarm symptoms**?", ["Yes", "No"])
    if alarm_symptoms == "Yes":
        st.error("🔴 **Urgent Endoscopy Needed! Refer immediately.**")
        return

    # Step 2: NSAID Use
    st.write("## **Step 2: Assess NSAID Use**")
    st.info("""
    **💊 Why assess NSAID use?**  
    NSAIDs are a major cause of **peptic ulcer disease and gastropathy**, leading to:  
    - **Gastric/duodenal ulcers** (direct mucosal injury + reduced prostaglandins).  
    - **Upper GI bleeding** (especially with concurrent corticosteroid or anticoagulant use).  

    **Next Step:** If NSAID use is present, consider **discontinuation + PPI therapy** for at least **8 weeks**.
    """)
    nsaid_use = st.radio("💊 Is the patient taking **NSAIDs or aspirin** regularly?", ["Yes", "No"])
    if nsaid_use == "Yes":
        st.warning("⚠ **Stop NSAIDs if possible and start PPI therapy for at least 8 weeks.**")

    # Step 3: GERD vs. Dyspepsia
    st.write("## **Step 3: GERD vs. Dyspepsia**")
    st.info("""
    **🔥 How to differentiate GERD from dyspepsia?**  
    - **GERD:** Classic symptoms include **heartburn, regurgitation, chest discomfort**, worse when lying down.  
    - **Dyspepsia:** Epigastric discomfort, **bloating, postprandial fullness, nausea**, not necessarily acid-related.  

    **Next Step:** If GERD symptoms are present, initiate an **8-week trial of PPI therapy** before considering further testing.
    """)
    gerd_symptoms = st.radio("🔥 Does the patient have **classic GERD symptoms**?", ["Yes", "No"])
    if gerd_symptoms == "Yes":
        st.success("✅ **Start an 8-week PPI trial.**")
        return

    # Step 4: H. pylori Testing Considerations
    st.write("## **Step 4: H. pylori Testing Considerations**")
    st.info("""
    **🦠 Why is H. pylori testing important?**  
    - H. pylori is a major cause of **peptic ulcers and gastric cancer**.  
    - Eradication reduces recurrence of ulcers and improves dyspepsia symptoms.  

    **🚫 Pre-Test Considerations:**  
    - **PPIs within 2 weeks**, **antibiotics or bismuth in the last 4 weeks** can cause **false-negative results**.  
    - **Next Step:** Stop PPIs **2 weeks before testing**.
    """)
    recent_ppi = st.radio("🛑 Has the patient taken **a PPI in the last 2 weeks**?", ["Yes", "No"])
    if recent_ppi == "Yes":
        st.warning("⚠ **Stop PPI for 2 weeks before H. pylori testing to avoid false negatives.**")

    # Step 5: H. pylori Testing
    st.write("## **Step 5: H. pylori Testing**")
    st.info("""
    **🧪 Which H. pylori test is best?**  
    - **Urea Breath Test (UBT):** Most accurate, non-invasive, and best for initial diagnosis and post-treatment follow-up.  
    - **Stool Antigen Test:** Reliable, non-invasive, useful if UBT is unavailable.  
    - **Biopsy-Based Tests (RUT, Histology, Culture):** Used only when endoscopy is needed.  

    **Next Step:** Choose UBT or Stool Antigen Test for initial diagnosis.
    """)
    hpylori_test = st.radio("🦠 Which test is available for H. pylori?", ["Urea Breath Test (UBT)", "Stool Antigen Test", "Biopsy-Based Test"])

    if hpylori_test in ["Urea Breath Test (UBT)", "Stool Antigen Test"]:
        hpylori_result = st.radio("📊 **H. pylori Test Result**:", ["Positive", "Negative"])

        if hpylori_result == "Positive":
            st.write("## **Step 6: H. pylori Eradication Therapy**")
            st.success("🦠 **Start H. pylori eradication therapy!**")
            st.info("""
            **🚑 Why treat H. pylori?**  
            - Prevents ulcer recurrence.  
            - Reduces risk of gastric cancer.  
            - Improves dyspepsia symptoms.  

            **Treatment Options:**  
            - **Triple Therapy:** PPI + Clarithromycin + Amoxicillin (or Metronidazole).  
            - **Quadruple Therapy:** PPI + Bismuth + Metronidazole + Tetracycline.  

            **Follow-Up:** Retest with UBT or Stool Antigen **4 weeks after completion**.
            """)

        else:
            st.write("## **Step 6: Functional Dyspepsia Management**")
            st.warning("⚠ **H. pylori Negative → Likely Functional Dyspepsia**")
            st.info("""
            **🔍 Next Steps:**  
            - Assess for **stress, anxiety, and dietary triggers**.  
            - Consider **neuromodulators** (low-dose TCAs, Buspirone).  
            - If symptoms persist, consider **EGD evaluation**.
            """)

# Run the CDSS function
dyspepsia_cdss()

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>⚠ This is an experimental clinical decision model intended **only for use by doctors**.</p>", unsafe_allow_html=True)
