# from transformers import BertTokenizer,TFBertForSequenceClassification

from django.db import models
class product(models.Model):
    name=models.CharField(max_length=60)
    description = models.TextField()
    picture = models.ImageField(blank = True, null = True, upload_to="product_images")
    
    def __str__(self):
        return self.name
    
class reviews(models.Model):
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    review = models.TextField()
    ratings = models.IntegerField()

    def __str__(self):
        return self.product.name + ": " + self.review
    

# Create your models here.
