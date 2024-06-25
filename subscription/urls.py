from django.urls import path
from subscription import views


urlpatterns = [
    path('confirm/<int:subscription_pk>', views.confirm_subscription, name='confirm-subscription'),
    path('cancel/<int:signet_pk>', views.cancel_subscription, name='cancel-subscription')
]
