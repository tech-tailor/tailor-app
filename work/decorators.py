from django.http import HttpResponseForbidden
from django.shortcuts import redirect

from work.models import Worker_Profile

def verify_worker_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        try:  
            user = request.user
            worker = Worker_Profile.objects.get(user=request.user)
            if user.is_authenticated and worker.verified_worker:  #user.verified_worker:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("Access Denied, you cannot view this page until the Admin verifies you. Contact the Admin ")
        
        except Exception as e:
            print('error: {e}')
            return redirect('work_worker_form')
        
    return wrapped_view
