from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from Grid.models import Review
import os 
path = os.getcwd()+'/FlipBackend/Weights'

import pickle 

svm0 = pickle.load(open(path+'/finalized_model0.sav', 'rb'))
svm1= pickle.load(open(path+'/finalized_model1.sav', 'rb'))
tf0 = pickle.load(open(path+'/TFidf_vector0.sav', 'rb'))
tf1 = pickle.load(open(path+'/Tfidf_vector1.sav', 'rb'))

s= ['product was damaged when delivered','delivery was prompt','error while doing payment','packaging was ugly','customer service was amazing and replied instataneously']

prediction_final(s)

@csrf_exempt 
def storeReview(request):
    data = json.loads(request.body)
    print("data is ",data)
    
    feedback = data['Feedback']
    userId = data['UserId']
    customerName = data['CustomerName']
    order_No = data["OrderNo"]
    review = Review(customer_name = customerName, order_no = order_No, review_text = feedback,categories_detected = "1 2")
    print("review is ",review)
    review.save()
    return JsonResponse({'valid':1})


@csrf_exempt 
def storeIssue(request):
    data = json.loads(request.body)
    print("data is ",data)

    
    return JsonResponse({'valid':1})
