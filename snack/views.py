from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import Snack
from .serializer import SnackSerializer
from .permissions import IsAutherorRead
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class SnackListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class SnackDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAutherorRead,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
