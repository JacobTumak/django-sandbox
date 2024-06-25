from django.shortcuts import render, get_object_or_404
from terms_of_service.models import TermsOfService, TermsOfServiceSignet, tos_signoff
from signoffs.shortcuts import get_signoff_or_404

def tos_signoff_view(request, terms_pk):
    model = get_object_or_404(TermsOfService, pk=terms_pk)
    signoff = tos_signoff.get(terms=model, user=request.user)

    if request.method == 'POST' and not signoff.is_signed():
        form = signoff.forms.get_signoff_form(request.POST)

        if form.is_valid() and form.is_signed_off():
            form.sign(user=request.user)

    return render(request, 'render_terms_signoff.html', context=dict(terms=model, signoff=signoff))


# def tos_signoff_view(request, terms_pk):
#     model = get_object_or_404(TermsOfService, pk=terms_pk)
#
#     if request.method == 'POST' and not model.signoff_set.has_signed(user=request.user):
#         form = model.signoff_set.forms.get_signoff_form(request.POST)
#
#         if form.is_valid() and form.is_signed_off():
#             signet = form.sign(user=request.user)
#
#     return render(request, 'render_terms_signoff.html', context=dict(terms=model))
