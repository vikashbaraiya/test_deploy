from django.urls import path
from login_app import views
from django.views.generic import RedirectView

urlpatterns = [
   
    
    path('auth/<page>/',views.auth),
    path('<page>/<operation>/<int:id>', views.actionId),
    path('<page>/', views.actionId),
    path('',views.index),
    path('index/', views.index),
    path('', RedirectView.as_view(url='/index/', permanent=True))
    
]