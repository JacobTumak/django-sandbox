from django.contrib import admin
from terms_of_service.models import TermsOfService, TermsOfServiceSignet

admin.site.register([TermsOfService, TermsOfServiceSignet])
