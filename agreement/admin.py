from django.contrib import admin
from .models import *
from signoffs.models import Signet

admin.site.register([LicensingAgreement, Signet])
