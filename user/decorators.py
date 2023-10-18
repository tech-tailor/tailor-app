from django.shortcuts import redirect

def phone_number_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        user = request.user

        if user.is_authenticated and user.verified:
            return view_func(request, *args, **kwargs)
        else:
            # Redirect to the phone number verification page
            return redirect('verifyphone')  # Replace with the correct URL pattern name

    return _wrapped_view