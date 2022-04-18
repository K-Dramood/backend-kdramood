from django.urls import path, include
from . import views

urlpatterns = [
    # GET localhost:8000/kdramas
    # POST localhost:8000/kdramas
    path('kdramas/', views.DramaList.as_view(), name='drama_list'),
    # PUT localhost:8000/kdramas/:id
    # DELETE localhost:8000/kdramas/:id
    path('kdramas/<int:pk>', views.DramaDetail.as_view(), name='drama_detail'),

    path('kdramas/mood/:mood', views.DramaList.as_view(), name='drama_list'),
    # GET localhost:8000/reviews
    # POST localhost:8000/reviews
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    # PUT localhost:8000/reviews/:id
    # DELETE localhost:8000/reviews/:id
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
]