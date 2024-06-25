from django.shortcuts import render, get_object_or_404, HttpResponse
from subscription.models import Subscription, subscription_signoff
from signoffs.shortcuts import get_signoff_or_404, get_signet_or_404


def confirm_subscription(request, subscription_pk):
    subscription = get_object_or_404(Subscription, pk=subscription_pk, user=request.user)
    if request.method == 'POST' and not subscription.signoff.has_signed(request.user):
        form = subscription.signoff.forms.get_signoff_form(request.POST)
        if form.is_signed_off() and form.is_valid():
            signet = form.sign(user=request.user, commit=False)
            signet.subscription = subscription
            signet.save()
    return render(request, 'render_simple_signoff.html', context={'subscription': subscription})


def cancel_subscription(request, signet_pk):
    signet = get_signet_or_404('subscription_signoff', signet_pk)
    if signet.user == request.user == signet.subscription.user and signet.is_signed(): #TODO: use perms to replace triple equality condition
        signet.signoff.get().revoke_if_permitted(user=request.user)
        return HttpResponse(f'{signet.subscription} was successfully cancelled.')
    return HttpResponse(f'You do not have permission to cancel this subscription.)')


# def cancel_subscription(request, subscription_pk): #TODO only option is to use signet_pk?
#     subscription = get_object_or_404(Subscription, pk=subscription_pk, user=request.user)
#     if subscription.signoff.has_signed(request.user):
#         subscription.signoff.get().revoke_if_permitted(user=request.user)
#         subscription.save()
#         return HttpResponse(f'{subscription} was successfully cancelled.')
#     return HttpResponse(f'{subscription} has not yet been signed (is_signed: {subscription.signoff.get().is_signed()})')

