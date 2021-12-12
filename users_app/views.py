from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms.registrations import RegistrationForm
from .forms.profile import ProfileForm, EditProfileForm


def registration_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            next_page = request.GET.get('next', '/accounts/login/')
            return redirect(next_page)
    else:
        form = RegistrationForm()
    context = {
        'reg_form': form
    }
    return render(request, "reg_form.html", context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)  # request.FILES is show the selected image or file

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            next_page = request.GET.get('next', '/user/profile/')
            return redirect(next_page)
    else:
        form = ProfileForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)
        args = {}
        args['form'] = form
        args['profile_form'] = profile_form
        return render(request, 'edit_profile.html', args)

@login_required
def view_profile(request):
    form = ProfileForm(instance=request.user)
    profile_form = EditProfileForm(instance=request.user.profile)
    args = {}
    # args.update(csrf(request))
    args['form'] = form
    args['profile_form'] = profile_form
    return render(request, 'view_profile.html', args)
