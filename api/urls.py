from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register('studentapi',views.StudentApiView,basename='stuapi')


urlpatterns = [
    path('',views.StudentApiView.as_view(),name='studentview'),
    # path('<int:pk>/',views.StudentApiUpdate.as_view(),name='studentupdates'),
    path('auth/',include('rest_framework.urls')),
    # path('',include(router.urls))
]

