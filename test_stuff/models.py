# my_app/models.py
from django.db import models
from signoffs.signoffs import SimpleSignoff
from signoffs.models import Signet

Signet

my_signoff = SimpleSignoff.register(id='my_app.my_signoff')  # id can be any str