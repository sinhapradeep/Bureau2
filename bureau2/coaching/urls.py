from django.urls import path
from coaching import views

urlpatterns = [
      path('', views.index, name='index'),
      path('about/', views.about, name='about'),
      path('song1/', views.song1, name='song1'),
      #path('career/', views.career, name='career'),
      #path('computer/', views.computer),
      #path('computer/computer/', views.computer, name='computer'),
      #path('coaching/', views.coaching),
      #path('coaching/coaching/', views.coacing, name='coaching'),
      #path('coachi/', views.coachi),
      #path('coachi/coachi/', views.coachi, name='coachi'),
      #path('teach/', views.teach),
      #path('teach/teach/', views.teach, name='teach'),
      #path('cont/', views.cont),
      #path('cont/cont/', views.cont, name='cont'),
      #path('mat/', views.mat),
      #path('mat/mat/', views.mat, name='mat'),

      path('sign_up/', views.sign_up, name='sign_up'),
      path('sign_up/sign_up/', views.sign_up, name='sign_up'),
      #path('register/', views.register, name='register'),
      #path('register/register/', views.register, name='register'),
      path('payment/', views.payment, name='payment'),
      path('ul/', views.ul, name='ul'),
      path('ul/ul/', views.ul, name='ul'),

      path('user_profile/', views.user_profile, name='profile'),
      path('profile2/', views.profile2, name='profile2'),
      path('payment/', views.payment, name='payment'),
      path('user_logout/', views.user_logout, name='user_logout'),
      path('timeT/', views.timeT, name='timeT'),

]