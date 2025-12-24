from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project, Proposal, Contract
from .serializers import (
    ProjectSerializer,
    ProposalSerializer,
    ContractSerializer
)

@api_view(['GET'])
def active_projects(request):
    projects = Project.objects.filter(status='active')
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def proposals(request):
    proposals = Proposal.objects.all()
    serializer = ProposalSerializer(proposals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def contracts(request):
    contracts = Contract.objects.all()
    serializer = ContractSerializer(contracts, many=True)
    return Response(serializer.data)
