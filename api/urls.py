# from django.urls import path
from rest_framework.routers import DefaultRouter

# from api.views import BookReviewDetailAPIView, BookReviewAPIView
from api.views import BookReviewsViewSet


app_name = "api"

router = DefaultRouter()
router.register("reviews", BookReviewsViewSet, basename='nimadir') # routerni ro'yxatdan o'tkazish "reviews" bu url pathga

urlpatterns = [
    # path("reviews/", BookReviewAPIView.as_view(), name="review-list"),
    # path("reviews/<int:id>/", BookReviewDetailAPIView.as_view(), name="review-detail"), # POST, GET, UPDATE, DELETE bor shu urlda
]
urlpatterns +=router.urls
