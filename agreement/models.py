from django.db import models
from signoffs.signoffs import IrrevokableSignoff
from signoffs.models import SignoffField

licensee_signoff = IrrevokableSignoff.register(id='licensee_signoff')

creator_signoff = IrrevokableSignoff.register(id='creator_signoff')


class LicensingAgreement(models.Model):  # TODO: change field names to something cleaner that's unique from signoff id
    license = models.TextField(max_length=1000)
    item_licensed = models.TextField(max_length=100)
    licensee_signoff, licensee_signet = SignoffField('licensee_signoff', related_name='license', blank=True)
    creator_signoff, creator_signet = SignoffField('creator_signoff', related_name='licensed', blank=True)

    def __str__(self):
        return f'Licensing Agreement for {self.item_licensed}'
