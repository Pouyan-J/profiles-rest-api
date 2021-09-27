from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet) # no need for base_name due to assigned query_set



urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]