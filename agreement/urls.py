from django.urls import path
from agreement import views


urlpatterns = [
    path('agreement_signoffs/<int:agreement_pk>', views.agreement_signoffs_view, name='agreement-signoff'),
]
