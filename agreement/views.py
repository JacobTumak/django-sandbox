from django.shortcuts import render, get_object_or_404
from django.core.exceptions import FieldError
from signoffs.shortcuts import get_signoff_or_404
from agreement.models import LicensingAgreement, licensee_signoff, creator_signoff

def get_signoff_fields(model: object, signoff_id: str) -> tuple:
    signoff, signet = None, None
    print(model.__dict__)
    for k, v in model.__dict__.items():
        print(k, v)
        if getattr(getattr(v,'signet', None), 'signoff_id', None) == signoff_id:
            signoff = v
        if getattr(v, 'id', None) == signoff_id:
            signet = v
        if signoff and signet:
            return signoff, signet
    raise FieldError(f'field names for {signoff_id} not found in {model}')

def agreement_signoffs_view(request, agreement_pk):
    agreement = get_object_or_404(LicensingAgreement, pk=agreement_pk)

    if request.method == 'POST':
        if request.POST['signoff_id'] == agreement.licensee_signoff.id:
            form = agreement.licensee_signoff.forms.get_signoff_form(request.POST)
            signet = agreement.licensee_signet
        elif request.POST['signoff_id'] == agreement.creator_signoff.id:
            form = agreement.creator_signoff.forms.get_signoff_form(request.POST)
            signet = agreement.creator_signet
        else:
            raise Exception('How did we get here?')

        if all((form.is_valid(), form.is_signed_off(), not signet)):
            signet = form.sign(request.user)
            agreement.save()
            # agreement.refresh_from_db()
    return render(request, "render_agreement_signoffs.html", context={'agreement':agreement})