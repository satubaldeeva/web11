from django.contrib.auth.decorators import login_required
from django.template.defaulttags import url
from django.urls import path, re_path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('recipes', views.recipes, name='recipes'),
    path('contact', views.contact, name='contact'),
    path('logout', views.logoutUser, name='logout'),
    path('member', views.member, name='member'),
    path('favourite_post', views.favourite_post, name="favourite_post"),
    #path("post/<int:post_id>/favourite/",login_required(views.FavouriteView.as_view(model=FavouritePost)),name='post_favourite'),
    path("<slug:slug>", views.post_detail, name="post_detail"),
]
