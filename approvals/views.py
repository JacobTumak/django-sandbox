from django.shortcuts import render, get_object_or_404
from approvals.approvals import ProjectApproval
from approvals.models import Project

# def sign_assignment_view(request, assignment_id):
#     assignment = get_object_or_404(Assignment, pk=assignment_id)
#     signoff = assignment.approval.get_next_signoff(for_user=request.user)
#     if request.method == "POST" and signoff:
#         signoff_form = signoff.forms.get_signoff_form(request.POST)
#         if signoff_form.is_valid():
#             signoff.sign(request.user, commit=True)
#             assignment.bump_status()
#             assignment.save()
#         else:
#             messages.error(request, "You do not have permission to sign this signoff")
#     return HttpResponseRedirect(reverse("assignment:detail", args=(assignment.id,)))

def sign_approval_view(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    signoff = project.approval.get_next_signoff()

    if request.method == 'POST':
        form = signoff.forms.get_signoff_form(request.POST)

        if form.is_valid() and form.is_signed_off():
            form.sign(request.user)

    context = dict(project=project)
    return render(request, 'render_project_approval.html', context)
