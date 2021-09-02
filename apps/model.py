import streamlit as st
import pickle
import numpy as np
import pandas as pd

def app():
    # Title of Predictive Analysis
    st.title("Predictive Analysis")

    #Create a function to load the model weights
    def load_model():
        result = pickle.load(open("xgboost_regressor_model.pkl" , "rb"))
        return result
    model = load_model()
    def load_label_encoder():
        le = pickle.load(open("encoding_dictionary.pkl", "rb"))
        return le
    label_enc = load_label_encoder()

    # Create a Project Code and Country option
    col1 , col2 = st.columns([2,2])
    Project_Code = col1.selectbox("Project Code" , ["116-ZA-T30","104-CI-T30","151-NG-T30","114-UG-T30","108-VN-T30"])
    Country = col2.selectbox("Country", ["South Africa","Nigeria","C�te d'Ivoire","Uganda","Vietnam","Haiti"])

    # Create a Managed By and Fulfill Via option
    col3 , col4 = st.columns([2,2])
    Managed_By = col3.selectbox("Managed By" , ["PMO - US","South Africa Field Office"])
    Fulfill_Via = col4.selectbox("Fulfill Via" , ["From RDC","Direct Drop"])

    # Create a Vendor INCO Term and Shipment Mode option
    col5 , col6 = st.columns([2,2])
    Vendor_INCO_Term = col5.selectbox("Vendor INCO Term" , ["N/A - From RDC","DDP","EXW","FCA","CIP","DDU","DAP"])
    Shipment_Mode = col6.selectbox("Shipment Mode" , ["Air","Truck","Air Charter","Ocean"])

    # Create a Product Group and Sub Classification Option
    col7 , col8 = st.columns([2,2])
    Product_Group = col7.selectbox("Product Group", ["ARV","ANTM","ACT"])
    Sub_classification = col8.selectbox("Sub Classification" , ["Adult","Pediatric","Malaria","ACT"])

    # Create a Vendor and Item Description option
    col9 , col10 = st.columns([2,2])
    Vendor = col9.selectbox("Vendor" , ["SCMS from RDC","S. BUYS WHOLESALER","Aurobindo Pharma Limited","ABBVIE LOGISTICS (FORMERLY ABBOTT LOGISTICS BV)"])
    Item_Description = col10.selectbox("Item Description" , ["Efavirenz 600mg, tablets, 30 Tabs","Nevirapine 200mg, tablets, 60 Tabs","Lamivudine/Nevirapine/Zidovudine 150/200/300mg, tablets, 60 Tabs","Lamivudine/Zidovudine 150/300mg, tablets, 60 Tabs"])

    # Create a Modecule/Test Type and Brand option
    col11 , col12 = st.columns([2,2])
    Molecule_Test_Type = col11.selectbox("Molecule and Test Type" , ["Efavirenz","Nevirapine","Lamivudine/Nevirapine/Zidovudine","Lamivudine/Zidovudine"])
    Brand = col12.selectbox("Brand" , ["Generic","Aluvia","Kaletra","Truvada","Norvir","Videx"])

    # Create a Dosage and Dosage Form option
    col13 , col14 = st.columns([2,2])
    Dosage = col13.selectbox("Dosage" , ["300mg","200mg","600mg","150/300/200mg","150/300mg","10mg/ml","150mg"])
    Dosage_Form = col14.selectbox("Dosage Form" , ["Tablet","Tablet - FDC","Oral solution","Capsule","Chewable/dispersible tablet - FDC"])

    # Create a Unit of Measure and Line Item Quantity option
    col15 , col16 = st.columns([2,2])
    Unit_of_Measure = col15.number_input("Unit of Measure (Per Pack)")
    Line_Item_Quantity = col16.number_input("Line Item Quantity")

    # Create a Line Item value and Pack Price option
    col17 , col18 = st.columns([2,2])
    Line_Item_Value = col17.number_input("Line Item Value")
    Pack_Price = col18.number_input("Pack Price")

    # Create a Manufacturing Site and First Line Designation option
    col19 , col20 = st.columns([2,2])
    Manufacturing_Site = col19.selectbox("Manufacturing Site", ["Aurobindo Unit III, India","Mylan (formerly Matrix) Nashik","Hetero Unit III Hyderabad IN","Cipla, Goa, India","Strides, Bangalore, India."])
    First_Line_Designation = col20.selectbox("First Line Designation" , ["Yes" , "No"])

    # Create a Weight and Freight Cost option
    col21 , col22 = st.columns([2,2])
    Weight = col21.number_input("Weight(Kilograms)")
    Freight_Cost = col22.number_input("Freight Cost (USD)")

    # Create the Line Item Insurance option
    Line_Item_Insurance = st.number_input("Line Item Insurance (USD)")


    if st.button("Submit"):
        input_lst = pd.Series([Project_Code,Country,Managed_By,Fulfill_Via,Vendor_INCO_Term,Shipment_Mode,Product_Group,Sub_classification,
                    Vendor,Item_Description,Molecule_Test_Type,Brand,Dosage,Dosage_Form,Unit_of_Measure,Line_Item_Quantity,Line_Item_Value,Pack_Price,Manufacturing_Site,
                    First_Line_Designation,Weight,Freight_Cost,Line_Item_Insurance], 
                    index=['Project Code', 'Country', 'Managed By', 'Fulfill Via', 'Vendor INCO Term', 'Shipment Mode',
                           'Product Group', 'Sub Classification', 'Vendor', 'Item Description', 'Molecule/Test Type', 
                           'Brand', 'Dosage', 'Dosage Form', 'Unit of Measure (Per Pack)', 'Line Item Quantity',
                           'Line Item Value', 'Pack Price', 'Manufacturing Site', 'First Line Designation', 
                           'Weight (Kilograms)', 'Freight Cost (USD)', 'Line Item Insurance (USD)'])

        categorical_types = ['Project Code', 'Country', 'Managed By', 'Fulfill Via', 'Vendor INCO Term', 
                            'Shipment Mode', 'Product Group', 'Sub Classification', 'Vendor', 
                            'Item Description', 'Molecule/Test Type', 'Brand', 'Dosage', 'Dosage Form', 
                            'Manufacturing Site', 'First Line Designation']
        #print(label_enc)
        #print(input_lst)
        X = []
        for column in input_lst.index:
            print(column)
            if column in categorical_types:
                X.append(int(label_enc[column].transform([input_lst[column]])[0]))
            else:
                X.append(int(input_lst[column]))
        X = pd.DataFrame([np.array(X).T], columns=input_lst.index)
        #X.to_csv("check.csv")
        print(X)
        print(X.shape)
        prediction = model.predict(X)
        #print(prediction)
        #output=round(prediction[0])
        #st.success("Unit Price is:- ".format(output))


#Managed By, Sub Classification, Unit of Measure (Per Pack), Line Item Quantity, Dosage Form, Product Group, Molecule/Test Type, Weight (Kilograms), Item Description, Fulfill Via, First Line Designation, Freight Cost (USD), Line Item Value, Vendor INCO Term, Manufacturing Site, Project Code, Line Item Insurance (USD), Pack Price, Shipment Mode

#Manufacturing_Site, Sub_Classification, Molecule_Test_Type, Pack_Price, Vendor_INCO_Term, Line_Item_Value, Item_Description, Project_Code, Managed_By, Freight_Cost, Dosage_Form, Line_Item_Insurance, Product_Group, First_Line_Designation, Shipment_Mode, Line_Item_Quantity, Weight, Unit_of_Measure, Fulfill_Via