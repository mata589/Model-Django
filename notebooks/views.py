
import json
from django.http.response import HttpResponse ,JsonResponse
from django.shortcuts import render
from joblib import load
import re
from django.views.decorators.csrf import csrf_exempt
model = load('./savedModels/model.joblib')

def predictor(request):
    return render(request,'main.html')

@csrf_exempt
def formInfo(request):
    if request.method == 'POST':
        try:
            input_data = json.loads(request.body)
            data = input_data['data']  # Extract the input data from the request
            print(data)
            # Process the input data and perform prediction using your model
            # ... (your code here)
        
            y_predict = model.predict(data),
            print(y_predict)
            
            prediction = y_predict[0]  
            print(prediction)
            prediction_str = str(prediction)
            prediction_str = re.sub(r'\[|\]', '', prediction_str)
            prediction_str = prediction_str.strip("'")
            print(prediction_str)
            prediction_json = {'prediction': prediction_str}
            return JsonResponse(prediction_json)

           
        except KeyError:
            return JsonResponse({'error': 'Invalid input data'})
    else:
        return JsonResponse({'error': 'Invalid request method'})




    
  