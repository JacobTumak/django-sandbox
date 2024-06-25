from django.urls import path
from terms_of_service import views


urlpatterns = [
    path('sign/<int:terms_pk>', views.tos_signoff_view, name='sign-terms'),
]
