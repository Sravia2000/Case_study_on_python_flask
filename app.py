from flask import Flask,request,render_template
import pickle
import numpy as np

app=Flask(__name__)

# Load the trained model
with open('social.pkl','rb') as social_file:
    social = pickle.load(social_file)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    gender =int(request.form['gender'])
    age =int(request.form['age'])
    salary =int(request.form['salary'])

# Make Prediction
    prediction = social.predict(np.array([[gender, age, salary]]))
    result = "will purchase the product" if prediction[0] == 0 else "will not purchase the product"

    return render_template('predict.html',result=result)


if __name__=='__main__':
    app.run(debug=True)    