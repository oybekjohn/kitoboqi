# from django.urls import path
from rest_framework.routers import DefaultRouter

# from api.views import BookReviewDetailAPIView, BookReviewAPIView
from api.views import BookReviewsViewSet


app_name = "api"

router = DefaultRouter()
router.register("reviews", BookReviewsViewSet, basename='review') # routerni ro'yxatdan o'tkazish "reviews" bu url pathga

urlpatterns = router.urls
