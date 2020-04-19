from my_blog import views
from django.urls import path

urlpatterns = [
    #  a list of posts for our homepage 
    path('',views.PostList.as_view(),name='home'),
    # Django uses angle brackets < > to capture the values from the URL and return the equivalent post detail page.
    path('<slug:slug>/', views.PostDetail.as_view(),name='post_detail'),
]

# Names are an optional parameter, but it is a good practice to give unique and rememberable names 
# to views which makes our work easy while designing templates 
# and it helps keep things organized as your number of URLs grows.