from django.db import models
from django.contrib.auth.models import User

from signoffs.signoffs import SimpleSignoff, SignoffUrlsManager, SignoffRenderer
from signoffs.models import Signet, SignoffSingle


class SubscriptionSignet(Signet):
    subscription = models.ForeignKey(to='Subscription',
                                     on_delete=models.CASCADE,
                                     related_name='signatories',
                                     editable=False)


subscription_signoff = SimpleSignoff.register(id='subscription_signoff',
                                              signetModel='subscription.SubscriptionSignet',
                                              sigil_label='Confirmed by',
                                              # label='Not priority',
                                              render=SignoffRenderer(
                                                  form_context=dict(
                                                      help_text='Check box and confirm to subscribe',
                                                      label='Confirm Subscription',
                                                  ),
                                                  signet_context=dict(
                                                      timestamp_label='Started',
                                                      show_revoke=True,
                                                      # with_signature_line=True,
                                                      # signature_line_label='Signature'
                                                  )
                                              ),
                                              urls=SignoffUrlsManager(revoke_url_name='cancel-subscription'))


class Subscription(models.Model):
    class TierOpts(models.TextChoices):
        BRONZE = 'bronze', 'Bronze'
        SILVER = 'silver', 'Silver'
        GOLD = 'gold', 'Gold'

    tier = models.TextField(choices=TierOpts.choices, default=TierOpts.BRONZE, max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE) #related_name
    signoff = SignoffSingle('subscription_signoff')#, signet_set_accessor='model')

    def __str__(self):
        return f'''{self.user}'s subscription'''

