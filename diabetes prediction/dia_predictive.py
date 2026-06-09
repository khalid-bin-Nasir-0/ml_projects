
import numpy as np
import pickle
import streamlit as st


dia_model = pickle.load(open('C:/Users/moham/Downloads/dai_model.sav','rb')) # rb -- read the binary file

def diabetes_pred (input_data):
    
    np_input_data = np.asarray(input_data)

    reshpae_data =  np_input_data.reshape(1,-1)

    prediction = dia_model.predict(reshpae_data)
    
    if(prediction[0]==0):
    
        return 'the person is non diabetic'
            
    else:
    
        return 'the person is diabetic'
    
    
    
    
def main():
    
    # giving title 
    st.title('diabetes prediction')
    
    # getting the input data from user
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input( 'Glucose Level')
    BloodPressure = st. text_input('Blood Pressure value')
    SkinThickness = st. text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')  
    
    # now make prediction when the button is clicked
    
    diag = ''
    
    if(st.button('click for check result ')):
        
        # maintaing the order according to our data train and same to prediction funtion
        
      diag = diabetes_pred([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
      
      st.success(diag)
      
      
      
      
      
if __name__ == '__main__':
    main()
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    

    