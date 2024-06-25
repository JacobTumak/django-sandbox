from django.db import models
from signoffs.approvals import ApprovalSignoff, SimpleApproval, IrrevokableApproval
from signoffs.models import Signet
from signoffs.registry import register
from signoffs.signoffs import SignoffLogic
from signoffs.signing_order import SigningOrder


@register("ProjectApproval")
class ProjectApproval(SimpleApproval):
    signoff_type = ApprovalSignoff

    submitter_signoff = signoff_type.register(id='submitter_signoff')

    pm_signoff = signoff_type.register(id='pm_signoff', perms='Project.can_create')

    fo_signoff = signoff_type.register(id='fo_signoff')

    cpo_signoff = signoff_type.register(id='cpo_signoff')

    signing_order = SigningOrder(submitter_signoff,
                                 pm_signoff,
                                 fo_signoff,
                                 cpo_signoff,
                                 )

class PermissionSignet(Signet):
    field_trip = models.ForeignKey('FieldTrip', on_delete=models.DO_NOTHING)


@register("PermissionApproval")
class PermissionApproval(IrrevokableApproval):
    S = ApprovalSignoff
    S_logic = SignoffLogic
    signet = PermissionSignet


    child_signoff = S.register('child_signoff', signetModel=signet)

    parent_signoff = S.register('parent_signoff', signetModel=signet, logic=S_logic(perm='auth.is_parent'))

    teacher_signoff = S.register('teacher_signoff', signetModel=signet, logic=S_logic(perm='auth.is_teacher'))


