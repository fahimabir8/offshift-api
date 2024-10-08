from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('user',views.UserViewset)
router.register('reviews', views.ReviewViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationApiView.as_view(), name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('edit-profile/', views.EditProfileApiView.as_view(), name='edit-profile'), 
    path('active/<uid64>/<token>/', views.activate, name='activate'),
    path('post_review/',views.ReviewApiView.as_view(), name = 'review')
]