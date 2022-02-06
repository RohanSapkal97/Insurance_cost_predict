from flask import Flask , render_template , request

import pickle




app = Flask(__name__)
model = pickle.load(open('Random_forest_regressor.pkl', 'rb'))

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    gender_female = 0
    region_northwest = 0
    region_southeast = 0
    region_southwest = 0
    smoker_no = 0
    
    if request.method == 'POST':
        gender_male=request.form['gender_male']
        if(gender_male=='male'):
            gender_male=1
            gender_female=0
        else:
            gender_male=0
            gender_female=1
        age = int(request.form['age'])
        children_0=request.form['children_0']
        if(children_0 == '0'):
            children_0 = 0
        elif(children_0 == '1'):
            children_0 = 1
        elif(children_0 == '2'):
            children_0 = 2
        elif(children_0 == '3'):
            children_0 = 3
        elif(children_0 == '4'):
            children_0 = 4
        else:
            children_0 = 5
            
        
        bmi = float(request.form['bmi'])

        region_northeast = request.form['region_northeast']
        if(region_northeast=='northeast'):
            region_northeast = 1
            region_northwest = 0
            region_southeast = 0
            region_southwest = 0
        elif(region_northeast=='northwest'):
            region_northeast = 0
            region_northwest = 1
            region_southeast = 0
            region_southwest = 0
        elif(region_northeast=='southeast'):
            region_northeast = 0
            region_northwest = 0
            region_southeast = 1
            region_southwest = 0
        else:
            region_northeast = 0
            region_northwest = 0
            region_southeast = 0
            region_southwest = 1
        
        smoker_yes=request.form['smoker_yes']
        if(smoker_yes=='smoker_yes'):
            smoker_yes=1
            smoker_no=0
        else:
            smoker_yes=0
            smoker_no=1
            
        input_data = ([[age,bmi,children_0,gender_female,gender_male,smoker_no,smoker_yes,region_northeast,region_northwest,region_southeast,region_southwest]])

        prediction = model.predict(input_data)

        output = round(prediction[0],2)
        
        return render_template('result.html',prediction_texts="Medical cost billed by health insurance is {}.".format(output))
        

    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)