

from django.urls import path, include
from apis import views

# Default Router
from rest_framework.routers import DefaultRouter

# Assign router to a Variable
router = DefaultRouter()
# 2nd argument - views.HelloViewSet
# 3rd argument - basename used for retrieving URLS in Router
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
#router.register('Incident', views.UserProfileViewSets)
#router.register('Organization', views.UserProfileFeedViewSet)
#router.register('Individual', views.UserProfileFeedViewSet)

urlpatterns = [
    # path('hello-view/', views.HelloApiView.as_view()),
    # path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]