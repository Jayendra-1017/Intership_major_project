from flask import Flask, request, jsonify, render_template
from flask_ngrok import run_with_ngrok
import pickle


app = Flask(__name__)

    
model_RF=pickle.load(open('/content/drive/My Drive/RF_model_predictor.pkl', 'rb')) 
model_KNN=pickle.load(open('/content/drive/My Drive/KNN_model_predictor.pkl', 'rb')) 
model_K_SVM=pickle.load(open('/content/drive/My Drive/SVM_model_predictor.pkl', 'rb')) 
model_DT=pickle.load(open('/content/drive/My Drive/DT_model_predictor.pkl', 'rb')) 
model_NB=pickle.load(open('/content/drive/My Drive/NB_model_predictor.pkl', 'rb')) 

run_with_ngrok(app)

@app.route('/')
def home():
  
    return render_template("index.html")
#------------------------------About us-------------------------------------------
@app.route('/aboutusnew')
def aboutusnew():
    return render_template('aboutusnew.html')

@app.route('/contact')
def contact():
  
  return render_template('contact.html')

@app.route('/Major')
def Major():
  
  return render_template('Major.html')  
  
@app.route('/predict',methods=['GET'])

def predict():
    
     
    r1 = float(request.args.get('rm'))
    r2 = float(request.args.get('text'))
    r3 = float(request.args.get('perimeter'))
    r4 = float(request.args.get('area'))
    r5 = float(request.args.get('smooth'))
    r6 = float(request.args.get('compact'))
    r7 = float(request.args.get('connect'))
    r8 = float(request.args.get('concave'))
    r9 = float(request.args.get('sym'))
    r10 = float(request.args.get('fract'))
    r11 = float(request.args.get('radius'))

    
    


# CreditScore	Geography	Gender	Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary	
    Model = (request.args.get('Model'))

    if Model=="Random Forest Classifier":
      prediction = model_RF.predict([[cs, con, gen, age, ten, bal, pro, cr, active, sal]])

    elif Model=="Decision Tree Classifier":
      prediction = model_DT.predict([[cs, con, gen, age, ten, bal, pro, cr, active, sal]])

    elif Model=="KNN Classifier":
      prediction = model_KNN.predict([[cs, con, gen, age, ten, bal, pro, cr, active, sal]])

    elif Model=="SVM Classifier":
      prediction = model_K_SVM.predict([[cs, con, gen, age, ten, bal, pro, cr, active, sal]])

    else:
      prediction = model_NB.predict([[cs, con, gen, age, ten, bal, pro, cr, active, sal]])

    
    if prediction == [1]:
      return render_template('index.html', prediction_text='The person not exited', extra_text ="-> Prediction by " + Model)
    
    else:
      return render_template('index.html', prediction_text='The person is exited', extra_text ="-> Prediction by " + Model)


app.run()
