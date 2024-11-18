from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('' , home.as_view(), name = 'home'),
    path('historia' , historia.as_view(), name = 'historia'),
    path('directorio', directorio.as_view(), name='directorio'),
    path('comite', comite.as_view(), name="comite"),
    path('estatutos', estatutos.as_view(), name='estatutos'),
    path('400', NotFound400.as_view(), name='error_400'),
    path('403', NotFound403.as_view(), name='error_403'),
    path('404', NotFound404.as_view(), name='error_404'),
    path('500', NotFound500.as_view(), name='error_500'),
    path('site.webmanifest', manifest, name= 'manifest'),
    path('simulate-500', simulate_500_error),
    path('simulate-403', simulate_403_error),
    path('simulate-400', simulate_400_error),


]

