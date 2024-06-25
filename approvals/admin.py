from django.contrib import admin
from approvals.models import Project
from signoffs.models import Stamp

admin.site.register([Project, Stamp])
