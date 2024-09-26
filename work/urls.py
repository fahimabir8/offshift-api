from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('categories',views.CategoryViewSet)
router.register('list',views.WorkViewSet)
router.register('allProposal',views.ProposalViewAll)

urlpatterns = [
    path('',include(router.urls)),
    path('proposal/',views.ProposalApiView.as_view(),name='proposal'),
]
