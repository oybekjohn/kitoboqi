from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework import filters

from books.models import BookReview
from api.serializers import BookReviewSerializer



# Custom BasePermission class written by me
class IsOwnerCustomPermission(BasePermission):
    ''' 
    foydalanuvchilar faqat o'zlarini malumotlarini tahrirlay olishadi bu permisson class bilan
    '''

    message = 'Only owners can edit of own reviews, So you are not the owner of this review'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user


class BookReviewsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerCustomPermission]
    serializer_class = BookReviewSerializer
    queryset = BookReview.objects.all().order_by("-created_at")
    lookup_field = "id"

    filter_backends = [filters.SearchFilter]
    search_fields = ["$book__title", "user__username"]
    # ordering = ['book_id']
    # ordering_fields = ['-book_id']

    # def filter_queryset(self, request, queryset, view):
    #     return queryset.filter(owner=request.user)
