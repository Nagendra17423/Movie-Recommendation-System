from .  import views
from django.urls import path
urlpatterns=[
    path('',views.home,name='home'),
    path('movie',views.movie,name="movie"), # taking values 
    path('user',views.user,name='user'),
    path('entery',views.show,name='show'), # user data with id 
    path('choose',views.opt,name='opt'), # showing movie 
    path('genere',views.genere,name='genere'),
    path('genfinal',views.genfinal,name='genfinal'),
    path('sat',views.sat,name='sat'),
    path('graph',views.graph,name='graph'),
    path('graprat',views.graprat,name='graprat'),
    path('grapmov',views.grapmov,name='grapmov'),
    path('tot',views.tot,name='tot'),
    path('tag',views.tag,name='tag'),
    path('tag1',views.tag1,name='tag1')
]