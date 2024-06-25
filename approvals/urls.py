from django.urls import path
from approvals import views


urlpatterns = [
    path('sign/<int:project_pk>', views.sign_approval_view, name='sign-approval'),
]
