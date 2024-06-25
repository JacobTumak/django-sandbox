from django.db import models
from signoffs.models import ApprovalField, ApprovalSignoffSet
from approvals.approvals import ProjectApproval

class Project(models.Model):
    title = models.TextField(max_length=100)
    proposal = models.TextField(max_length=1000)
    approval, stamp = ApprovalField('ProjectApproval', blank=True)


class FieldTrip(models.Model):
    class_going = models.TextField(max_length=100)
    cost = models.IntegerField()
    destination = models.TextField(max_length=100)
    schedule = models.TextField(max_length=100)
    permission_signoffs = ApprovalSignoffSet()
