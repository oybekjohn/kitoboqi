from rest_framework.routers import DefaultRouter

from api.views import BookViewSet, AuthorViewSet, BookAuthorViewSet, BookReviewsViewSet


app_name = "api"

router = DefaultRouter()
# router.register('user-create', UserCreateAPIView, basename='user-create')
# router.register('user-list', UserListAPIView, basename='user-list')
# router.register('user-update', UserRetrieveUpdateDestroyAPIView, basename='user-update')
router.register("books", BookViewSet, basename='book')
router.register("authors", AuthorViewSet, basename='author')
router.register("bookauthors", BookAuthorViewSet, basename='bookauthor')
router.register("reviews", BookReviewsViewSet, basename='review')


urlpatterns = router.urls
