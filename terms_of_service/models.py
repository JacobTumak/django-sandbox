from django.db import models
from signoffs.models import Signet, SignoffSet
from signoffs.signoffs import IrrevokableSignoff


class TermsOfServiceSignet(Signet):
    terms = models.ForeignKey('TermsOfService', on_delete=models.DO_NOTHING, related_name='signatories') # , related_name='terms_signatories'


tos_signoff = IrrevokableSignoff.register('tos_signoff', signetModel=TermsOfServiceSignet)


class TermsOfService(models.Model):
    terms = models.TextField(max_length=1000)
    signoff_set = SignoffSet(signoff_type='tos_signoff')
