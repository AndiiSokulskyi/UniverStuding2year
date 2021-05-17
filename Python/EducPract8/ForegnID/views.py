from rest_framework import generics
from .serializers import ForeignIDDetailSerializer
from .models import ForeignID
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import filters, pagination

# Create your views here.

class ForeignIDCreateView(generics.CreateAPIView):
    serializer_class = ForeignIDDetailSerializer
    permission_classes = (IsAuthenticated, )

class ForeignIDCollectionView(generics.ListAPIView):
    serializer_class = ForeignIDDetailSerializer
    queryset = ForeignID.objects.all()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    pagination_class = pagination.LimitOffsetPagination
    search_fields = ['id', 'country_code', 'passport_no', 'first_name', 'last_name', 'date_of_birth', 'date_of_issue', 'date_of_expire']
    permission_classes = (IsAdminUser, )

class ForeignIDDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ForeignIDDetailSerializer
    queryset = ForeignID.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )

