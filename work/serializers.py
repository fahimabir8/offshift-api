from rest_framework import serializers
from .models import Category,Work,Proposal
from account.models import CustomUser
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','email','user_type','last_login','date_joined','country']

class WorkSerializer(serializers.ModelSerializer):
    client = UserSerializer(many=False)
    freelancer = UserSerializer(many=False)
    category = CategorySerializer(many = True)
    
    class Meta: 
        model = Work
        fields = '__all__'
                
class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['freelancer', 'client','work', 'price', 'content', 'created_at']

    def save(self):
        freelancer = self.validated_data['freelancer']
        client = self.validated_data['client']
        work = self.validated_data['work']
        price = self.validated_data['price']
        content = self.validated_data['content']

        proposal = Proposal(freelancer=freelancer, client=client, work=work, price=price, content=content)
        proposal.save()
        return proposal
        
  