from django.urls import path
from .views import ImageTransactionView


urlpatterns = [
    # path('upload-image/', views.upload_image, name='upload_image'),
    path('imgtransactions/', ImageTransactionView.as_view(), name='image_transactions'),
]