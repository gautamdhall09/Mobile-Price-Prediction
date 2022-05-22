from flask import Flask, render_template, request 
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('Mob_Pred.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Battery_Power = int(request.form['battery_power'])
        Internal_Memory = int(request.form['int_memory'])
        Mobile_Depth = float(request.form['m_dep'])
        Mobile_Weight = float(request.form['mobile_wt'])
        Num_Cores = int(request.form['n_cores'])
        Primary_Camera = float(request.form['pc'])
        Pixel_Height = float(request.form['px_height'])
        Pixel_Width = float(request.form['px_width'])
        Screen_Height = float(request.form['sc_h'])
        Screen_Width = float(request.form['sc_w'])
        Talk_Time = int(request.form['talk_time'])
        Ram = int(request.form['ram'])
        Clock_Speed = float(request.form['clock_speed'])
        Front_Cam = float(request.form['fc'])
        
        Bluetooth_Yes=request.form['blue']
        if(Bluetooth_Yes=='Yes'):
            Bluetooth_Yes = 1
            Bluetooth_No = 0
        else:
            Bluetooth_Yes = 0
            Bluetooth_No = 1
            
        Dual_Yes = request.form['dual_sim']
        if(Dual_Yes == 'Yes'):
            Dual_Yes = 1
            Dual_No = 0
        else:
            Dual_No = 1
            Dual_Yes = 0
            
        Wifi_Yes = request.form['wifi']
        if(Wifi_Yes == 'Yes'):
            Wifi_Yes = 1
            Wifi_No = 0
        else:
            Wifi_No = 1
            Wifi_Yes = 0
       
        Three_Yes = request.form['three_g']
        if(Three_Yes == 'Yes'):
            Three_Yes = 1
            Three_No = 0
        else:
            Three_No = 1
            Three_Yes = 0
                                 
        Four_Yes = request.form['four_g']
        if(Four_Yes == 'Yes'):
            Four_Yes = 1
            Four_No = 0
        else:
            Four_No = 1
            Four_Yes = 0  
            
            
        Touch_Yes = request.form['touch_screen']
        if(Touch_Yes == 'Yes'):
            Touch_Yes = 1
            Touch_No = 0
        else:
            Touch_No = 1
            Touch_Yes = 0
                                 
        prediction = model.predict([[Battery_Power,Internal_Memory ,Mobile_Depth,Mobile_Weight,Num_Cores,Primary_Camera,
                               Pixel_Height,Pixel_Width,Screen_Height,Screen_Width,Talk_Time,Ram,Dual_Yes,Bluetooth_Yes,Wifi_Yes,Three_Yes,Four_Yes,Touch_Yes, Clock_Speed ,Front_Cam]])
        
        output = round(prediction[0],2)
        
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you can not buy")
        else:
            return render_template('index.html',prediction_text="Cost Price is {}".format(output))
    else:
        return render_template('index.html')
if __name__=="__main__":
    app.run(debug = True)
                                                    
                                 
                              
            
            
      
            
            
        
        
    
        
    