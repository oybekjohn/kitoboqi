from rest_framework import viewsets, generics
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser, IsAuthenticated
from rest_framework import filters

from books.models import Book, Author, BookAuthor, BookReview
from users.models import CustomUser
from api.serializers import UserCreateSerializer, UserSerializer, UserUpdateSerializer, BookSerializer, AuthorSerializer, BookAuthorSerializer,BookReviewSerializer




# ------------------Custom Permissions------------------
class IsOwnerCustomPermission(BasePermission):
    ''' 
    foydalanuvchilar faqat o'zlarini malumotlarini tahrirlay olishadi bu permisson class bilan
    '''

    message = 'Only owners can edit this API of own, So you are not the owner of this data'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user




# ------------------User Seralizers---------------------------
# class UserCreateAPIView(generics.CreateAPIView):
#     '''
#     Custom user list and create API view
#     '''
#     queryset = CustomUser.objects.all()
#     serializer_class = UserCreateSerializer
#     permission_classes = [IsAdminUser]
   



# class UserListAPIView(generics.ListAPIView):
#     '''
#     Custom user list API view
#     '''
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['username', 'email']




# class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     '''
#     Custom user retrieve, update, destroy API view
#     '''
#     queryset = CustomUser.objects.all()
#     serializer_class = UserUpdateSerializer
#     permission_classes = [IsOwnerCustomPermission]




# ------------------Books Seralizers---------------------------
class BookViewSet(viewsets.ModelViewSet):
    '''
    Book viewset class
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']



class AuthorViewSet(viewsets.ModelViewSet):
    '''
    Author viewset class
    '''
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']



class BookAuthorViewSet(viewsets.ModelViewSet):
    '''
    BookAuthor viewset class
    '''
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['book', 'author']



class BookReviewsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerCustomPermission | IsAdminUser]
    serializer_class = BookReviewSerializer
    queryset = BookReview.objects.all().order_by("-created_at")
    lookup_field = "id"

    filter_backends = [filters.SearchFilter]
    search_fields = ["$book__title", "user__username"]
    # ordering = ['book_id']
    # ordering_fields = ['-book_id']

    # def filter_queryset(self, request, queryset, view):
    #     return queryset.filter(owner=request.user)
