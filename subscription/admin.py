from django.contrib import admin
from subscription.models import SubscriptionSignet, Subscription

admin.site.register([SubscriptionSignet, Subscription])

