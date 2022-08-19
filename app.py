import numpy as np
from flask import Flask, request, jsonify, render_template


import pickle
import pandas as pd
import subprocess as sp


app = Flask(__name__)


  


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


@app.route('/Minor')
def Minor():
  
  return render_template('Minor.html') 

@app.route('/predict',methods=['GET'])
def predict():
    
    
    '''
    For rendering results on HTML GUI
    '''
    #result=np.array(['SqFt','bedrooms','Offers','bricks','Neighborhood','Bathrooms'])
    #result.reshape(1,-1)
    #print(result)
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
    model1=int(request.args.get('model1'))
   

    
    
    if model1==0:
      model=pickle.load(open('RF_cancer_predictor.pkl','rb'))

    elif model1==1:
       model=pickle.load(open('DT_cancer_predictor.pkl','rb'))
    
    elif model1==2:
      model=pickle.load(open('KNN_cancer_predictor.pkl','rb'))

    elif model1==3:
       model=pickle.load(open('LC_cancer_predictor.pkl','rb'))

    elif model1==4:
       model=pickle.load(open('SVM_cancer_predictor.pkl','rb'))

    elif model1==5:
       model=pickle.load(open('NB_cancer_predictor.pkl','rb'))

    elif model1==6:
       model=pickle.load(open('linear_cancer_pridictor.pkl','rb'))   

    dataset= pd.read_csv('breast-cancer.csv')
    X = dataset.iloc[:,2:13]
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(X)
    prediction = model.predict(sc.transform([[r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11]]))
    if prediction==1:
      message="That you are Suffrering from cancer"
    else:
      message=" that you are not suffering from cancer"  
  
    return render_template('Major.html',prediction_text="This model is saying {} ".format(message))


if __name__ == "__main__":
    app.run(debug=True)
