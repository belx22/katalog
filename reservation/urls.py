from django.urls import path
from . import views


app_name = 'reservation'
from reservation.views import home
urlpatterns = [
    path('',home),
    path('update/<int:pk>/',views.update, name='update'),
    path('cites',views.cites, name="cites"),
   # path('cites/detail',views.detail, name="detail"),
    path('cites/<int:cite_id>/',views.detail,name="detail"),
    path('recherche/',views.recherche, name="recherche"),
    path('apropos_de_nous/',views.apropos_de_nous, name="apropos_de_nous"),
    path('apropos_de_la_plateforme/',views.apropos_de_la_plateforme, name="apropos_de_la_plateforme"),
    path('nous_contacter/',views.nous_contacter, name="nous_contacter"),
    path('testes/',views.testes,name="testes"),
    
   
]

