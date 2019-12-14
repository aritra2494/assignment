def join(request):
    if request.method == "POST":
        userForm = UserForm(request.POST, prefix='user')
        profileForm = ProfileForm(request.POST, prefix='profile')
        if userForm.is_valid() * profileForm.is_valid():
            user = userForm.save()
            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('index')
    else:
        userForm = UserForm()
        profileForm = ProfileForm()
    return render_to_response('registration/join.html',dict(userform=userForm,
                                                profileform=profileForm))
