from . import views
from django.urls import include,path
from django.views.generic.base import RedirectView


urlpatterns = [
    
    path('', views.products, name='products'),
    path('<str:category>', views.products, name='products'),
    # path('DearCovid', RedirectView.as_view(url = "http://19-ncov.cf/DearCovid/1"), name='messages'),
    path('<str:category>/<str:productname>', views.product, name='product'),
    # path('<str:pagename>', views.multiview),
]
