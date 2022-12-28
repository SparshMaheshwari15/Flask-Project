import pickle
import numpy as np
from flask import Flask, render_template,request
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    try:
        area=request.form.get('area')
        bedroom=request.form.get('bedroom')
        bathroom=request.form.get('bathroom')
        stories=request.form.get('stories')
        mainroad=request.form.get('mainroad')
        guestroom=request.form.get('guestroom')
        basement=request.form.get('basement')
        hotwaterheating=request.form.get('hotwaterheating')
        airconditioning=request.form.get('airconditioning')
        parking=request.form.get('parking')
        prefarea=request.form.get('prefarea')
        furnishingstatus=request.form.get('furnishingstatus')
        input=np.array([area,bedroom,bathroom,stories,mainroad,guestroom,basement,
        hotwaterheating,airconditioning,parking,prefarea,furnishingstatus])
        for i in range(input.__len__()):
            if(input[i]=='yes'):
                input[i]=100
            elif(input[i]=='no'):
                input[i]=101
            elif(input[i]=='furnished'):
                input[i]=10
            elif(input[i]=='semi-furnished'):
                input[i]=11
            elif(input[i]=='unfurnished'):
                input[i]=12
        input1=input.astype(int)
        #ip=input.reshape(1,-1)
        # for i in range(input.__len__()):
        #     if type(input[i])!=int:
        #         input[i]=int(input[i])
        #         input[i]=int(input[i])
        #input=input.reshape(1,-1)
        ip=input1.reshape(1,-1)
        try:
            #prediction=model.predict([[]])
            output=int(model.predict(ip))
            #output=round(prediction[0],2)
            #return render_template('index.html')
            return render_template('index.html',prediction_text=f'Total price of the flat is {output}')
        except:
            return render_template('index.html',prediction_text=f'Something went wrong(Wrong Input)!')
    except:
        return render_template('index.html',prediction_text=f'Something went wrong(No Input detected)!')
if __name__ == "__main__":
    app.run(debug=True)
##