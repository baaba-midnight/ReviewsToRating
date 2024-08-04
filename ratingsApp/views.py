from django.shortcuts import render,redirect
from django.urls import reverse
from .models import product,reviews
import torch

import random
from .bert_model import model,tokenizer
from django.http import HttpResponseRedirect, JsonResponse
# import re



# Load the Keras model (only once when the view is first loaded)
# model = tf.keras.models.load_model('path/to/your_model.h5')


def products(request):
    products = product.objects.all()
    context = {"products":products}
    if request.method == "POST":
        review = request.POST['review']
        pid = request.POST['productId']
        ratings = predict(review)
        print(ratings)
        # review = pre_process(review)
        # prediction = model.predict(review)
        review_instance = reviews()
        review_instance.product = product.objects.get(id = pid)
        review_instance.review = review
        review_instance.ratings = ratings
        review_instance.save()
        return HttpResponseRedirect(reverse('product'))
    return render(request,"products.html",context)

def display_reviews(request,id):
    review = reviews.objects.filter(product__id = id)
    context = {"reviews":review}
    return render(request,"reviews.html",context)    

"""
def process_form(request):
    print("form")
    if request.method == "POST":
        review = request.POST['review']
        pid = request.POST['productId']
        # review = pre_process(review)
        # prediction = model.predict(review)
        ratings = random.randint(1,5)
        print(review)
        print(pid)
        context = {
            # "products":products,
            "stars":ratings,
            "productId":pid,  
        }    
        print("Lame")
        return JsonResponse(context)
    return redirect('product')
"""

def home(request):
    return render(request,"base.html",{})


"""
model.load_state_dict(torch.load('/content/drive/MyDrive/Colab Notebooks/Final Project AI/model.pth', map_location=torch.device('cpu')))
model.eval()

"""

def predict(comment):
    # tokenize my input
    inputs = tokenizer(comment, return_tensors="pt", truncation=True, padding=True, max_length=512)
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    # make prediction
    with torch.no_grad():
        outputs = model(input_ids, attention_mask)
        preds = torch.argmax(outputs, dim=1)
        # probs = torch.softmax(outputs, dim=1)

    return preds



#Baaba has to code this
# def pre_process(text):
#     # remove special characters
#     text = re.sub(r'[^\w\s]', '', text)
#     text = ' '.join(text.split())
#     # Get BERT embeddings
#     embeddings = bert_model.get_embeddings(text)
#     print(embeddings.shape)

    
#     # pass text through tokenizer
#     tokenizer(text, return_tensors='tf', trancation=True, padding=True, max_length=512)

# Create your views here.
