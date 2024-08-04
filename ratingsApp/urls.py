from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("products",views.products,name="product"),
    path("reviews/<int:id>",views.display_reviews,name="reviews"),
    # path('process_form/', views.process_form, name='process_form'),

]