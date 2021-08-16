from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)

model = pickle.load(open('saved_models/randomforest2.pkl', 'rb'))

@app.route('/')
def Home():
    return render_template('home.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        monthlycharges = float(request.form['MonthlyCharges'])
        totalcharges = float(request.form['TotalCharges'])
        tenure = int(request.form['tenure'])

        gender = request.form['gender']
        if(gender == "Male"):
            gender_Male = 1
        else:
            gender_Male = 0

        seniorcitizen = request.form['seniorcitizen']
        if(seniorcitizen == 'Yes'):
            SeniorCitizen_1 = 1
        else:
            SeniorCitizen_1=0

        partner = request.form['partner']
        if(partner == "Yes"):
            Partner_Yes = 1
        else:
            Partner_Yes = 0

        dependents = request.form['Dependents']
        if(dependents == 'Yes'):
            Dependents_Yes = 1
        else:
            Dependents_Yes = 0

        phoneservice = request.form['phoneservice']
        if(phoneservice == "Yes"):
            PhoneService_Yes = 1
        else:
            PhoneService_Yes = 0

        multiplelines = request.form['multiplelines']
        if(multiplelines == "No phone service"):
            MultipleLines_No_phone_service = 1
            MultipleLines_Yes = 0
        elif(multiplelines == "Yes"):
            MultipleLines_No_phone_service = 0
            MultipleLines_Yes = 1
        else:
            MultipleLines_No_phone_service = 0
            MultipleLines_Yes = 0

        internetservice = request.form['InternetService']
        if(internetservice=='Fiber optic'):
            InternetService_Fiber_optic = 1
            InternetService_No = 0
        elif(internetservice == "No"):
            InternetService_Fiber_optic = 0
            InternetService_No = 1
        else:
            InternetService_Fiber_optic = 0
            InternetService_No = 0

        onlinesecurity = request.form['OnlineSecurity']
        if(onlinesecurity == 'Yes'):
            OnlineSecurity_Yes = 1
            OnlineSecurity_No_internet_service = 0
        elif(onlinesecurity == "No internet service"):
            OnlineSecurity_Yes = 0
            OnlineSecurity_No_internet_service = 1
        else:
            OnlineSecurity_Yes = 0
            OnlineSecurity_No_internet_service = 0

        onlinebackup = request.form['OnlineBackup']
        if(onlinebackup == 'No internet service'):
            OnlineBackup_No_internet_service = 1
            OnlineBackup_Yes = 0
        elif(onlinebackup == "Yes"):
            OnlineBackup_No_internet_service = 0
            OnlineBackup_Yes = 1
        else:
            OnlineBackup_No_internet_service = 0
            OnlineBackup_Yes = 0

        deviceprotection = request.form['DeviceProtection']
        if(deviceprotection == "No internet service"):
            DeviceProtection_No_internet_service = 1
            DeviceProtection_Yes = 0
        elif(deviceprotection == "Yes"):
            DeviceProtection_No_internet_service = 0
            DeviceProtection_Yes = 1
        else:
            DeviceProtection_No_internet_service = 0
            DeviceProtection_Yes = 0

        techsupport = request.form['TechSupport']
        if(techsupport == "No internet service"):
            TechSupport_No_internet_service = 1
            TechSupport_Yes = 0
        elif(techsupport == "Yes"):
            TechSupport_No_internet_service = 0
            TechSupport_Yes = 1
        else:
            TechSupport_No_internet_service = 0
            TechSupport_Yes = 0

        streamingtv = request.form['StreamingTV']
        if(streamingtv == 'No internet service'):
            StreamingTV_No_internet_service = 1
            StreamingTV_Yes = 0
        elif(streamingtv == "Yes"):
            StreamingTV_No_internet_service = 0
            StreamingTV_Yes = 1
        else:
            StreamingTV_No_internet_service = 0
            StreamingTV_Yes = 0


        streamingmovies = request.form['StreamingMovies']
        if(streamingmovies == "No internet service"):
            StreamingMovies_No_internet_service = 1
            StreamingMovies_Yes = 0
        elif(streamingtv == "Yes"):
            StreamingMovies_No_internet_service = 0
            StreamingMovies_Yes = 1
        else:
            StreamingTV_No_internet_service = 0
            StreamingTV_Yes = 0

        contract = request.form['Contract']
        if(contract == "One yesr"):
            Contract_One_year = 1
            Contract_Two_year = 0
        elif(contract == "Two year"):
            Contract_One_year = 0
            Contract_Two_year = 1
        else:
            Contract_One_year = 0
            Contract_Two_year = 0

        paperlessbilling = request.form['PaperlessBilling']
        if(paperlessbilling == "Yes"):
            PaperlessBilling_Yes = 1
        else:
            PaperlessBilling_Yes = 0

        paymentmethod = request.form['PaymentMethod']
        if(paymentmethod == "Electronic check"):
            PaymentMethod_Electronic_check = 1
            PaymentMethod_Credit_card = 0
            PaymentMethod_Mailed_check = 0
        elif(paymentmethod == 'Credit card (automatic)'):
            PaymentMethod_Electronic_check = 0
            PaymentMethod_Credit_card = 1
            PaymentMethod_Mailed_check = 0
        elif(paymentmethod == "Mailed check"):
            PaymentMethod_Electronic_check = 0
            PaymentMethod_Credit_card = 0
            PaymentMethod_Mailed_check = 1
        else:
            PaymentMethod_Electronic_check = 0
            PaymentMethod_Credit_card = 0
            PaymentMethod_Mailed_check = 0


        features = [tenure, monthlycharges, totalcharges, gender_Male, SeniorCitizen_1, Partner_Yes,
                    Dependents_Yes, PhoneService_Yes, MultipleLines_No_phone_service, MultipleLines_Yes,
                    InternetService_Fiber_optic, InternetService_No, OnlineSecurity_No_internet_service, 
                    OnlineSecurity_Yes, OnlineBackup_No_internet_service, OnlineBackup_Yes,
                    DeviceProtection_No_internet_service, DeviceProtection_Yes, TechSupport_No_internet_service,
                    TechSupport_Yes, StreamingTV_No_internet_service, StreamingTV_Yes,StreamingMovies_No_internet_service,
                    StreamingMovies_Yes, Contract_One_year, Contract_Two_year, PaperlessBilling_Yes,
                   PaymentMethod_Credit_card, PaymentMethod_Electronic_check, PaymentMethod_Mailed_check]

        prediction=model.predict([features])
        if prediction == 1:
            return render_template('home.html',prediction_texts="The customer will churn")
        else:
            return render_template('home.html',prediction_text="The Customer will not churn")
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)
