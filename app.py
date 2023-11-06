import streamlit as st
import pickle
import pandas as pd
import numpy as np
import webbrowser

st.title("Arokiyyam - Diabetes Prediction")

model = pickle.load(open('model.pkl','rb'))

name = st.text_input("Name :")
pregnancy = st.number_input("No. of Pregnancies :")
glucose = st.number_input("Plasma Glucose Concentration :")
bp =  st.number_input("Diastolic Blood Pressure (mm Hg) :")
skin = st.number_input("Triceps Skin Fold Thickness (mm) :")
insulin = st.number_input("2-Hour serum insulin (mu U/ml) :")
bmi = st.number_input("Body Mass Index (weight in kg/(height in m)^2) :")
dpf = st.number_input("Diabetes Pedigree Function :")
age = st.number_input("Age :")
submit = st.button('Predict')

if submit:
        prediction = model.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
        if prediction == 0:
            st.write('Congratulations', name, '. You are Not Diabetic.')
            st.subheader("Diet Recommendation to Prevent Diabetes in the Future")
            st.write("Choose whole grains and whole grain products over refined grains and other highly processed carbohydrates. ",
                     "Skip the sugary drinks, and choose water, coffee, or tea instead. ",
                     "Limit red meat and avoid processed meat; choose nuts, beans, whole grains, poultry, or fish instead.",
                     "Fiber-rich foods promote weight loss and lower the risk of diabetes. ",
                     "Eat a variety of healthy, fiber-rich foods, which include :",
                     "Fruits, such as tomatoes, peppers and fruit from trees, ",
                     "Nonstarchy vegetables, such as leafy greens, broccoli and cauliflower, ",
                     "Legumes, such as beans, chickpeas and lentils, ",
                     "Whole grains, such as whole-wheat pasta and bread, whole-grain rice, whole oats, and quinoa.")

        else:
            st.write('Sorry ',name, '. It seems like you might be Diabetic.')
            st.subheader("Diet Recommendation to Control Diabetes")
            st.write("Keeping track of how many carbs you eat and setting a limit for each meal can help keep your blood sugar levels in your target range.",
                     "The plate method is a simple, visual way to make sure you get enough nonstarchy vegetables and lean protein while limiting the amount of higher-carb foods you eat that have the highest impact on your blood sugar.",
                     "Start with a 9-inch dinner plate",
                     "Fill half with nonstarchy vegetables, such as salad, green beans, broccoli, cauliflower, cabbage, and carrots.",
                     "Fill one quarter with a lean protein, such as chicken, turkey, beans, tofu, or eggs.",
                     "Fill one quarter with carb foods. Foods that are higher in carbs include grains, starchy vegetables (such as potatoes and peas), rice, pasta, beans, fruit, and yogurt. A cup of milk also counts as a carb food.",
                     "Then choose water or a low-calorie drink such as unsweetened iced tea to go with your meal.")
            
            if(age>=18 and age<=50):
                st.subheader("Recommended Exercise for Adults Aged to 18 and 50")
                st.write("Swimming, Planks, Weight Lifting, Resistance Band Exercises, Pushups, Pullups, Squats, Lunges, Abdominal Crunches")
            else:
                st.subheader("Recommended Exercise for Adults Aged over 50")
                st.write("Walking, Cycling, Zumba, Mermaid Movement, Side Circles, Step Ups, Yoga, Aqua Jogging, Flutter Kicking")

st.subheader("Doctor Recommendation")
st.write('Find Suitable Doctors according to your Location')
location = st.text_input("Location : ")
get_doc = st.button('Get Doctors')
if get_doc:   
    query = 'https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22diabetes%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22symptom%22%7D%5D&city='+location
    st.write("Here's the Best Doctors for Diabetes available in ",location, " : [Doctors](%s)" %query)
   
                