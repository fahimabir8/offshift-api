from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets,filters,status
from rest_framework.response import Response
from .serializers import CategorySerializer,WorkSerializer,ProposalSerializer
from .models import Category,Work,Proposal
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend]
    filterset_fields = ['id']
    search_fields = ['title', 'description', 'category__name']
    ordering_fields = ['budget']
    ordering = ['budget']
    

class ProposalApiView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProposalSerializer
    
    def post(self, request, *args, **kwargs):
        job_id = request.query_params.get('jobId')  
        work = Work.objects.get(id=job_id)  
   
        data = {
            'freelancer': request.user.id,  
            'work': work.id,
            'client': work.client.id,
            'price': request.data.get('price'),
            'content': request.data.get('content')
        }

        serializer = ProposalSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProposalViewAll(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['freelancer__id','client__id']
    