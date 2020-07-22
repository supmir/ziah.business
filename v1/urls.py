from django.urls import path

from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    
    path('', views.products, name='products'),
    # path('DearCovid', RedirectView.as_view(url = "http://19-ncov.cf/DearCovid/1"), name='messages'),
    path('Maxxima/<str:productname>', views.maxxima, name='maximma'),
    path('Garden/<str:productname>', views.garden, name='garden'),
    # path('<str:pagename>', views.multiview),
]
