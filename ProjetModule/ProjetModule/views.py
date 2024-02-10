from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Session, Response

@login_required
def session_form(request, session_id):
    session = Session.objects.get(id=session_id)
    if session.is_open:
        if request.method == 'POST':
            # Traiter les données du formulaire de réponse
            return render(request, 'success.html')
        else:
            return render(request, 'form.html', {'session': session})
    else:
        return render(request, 'closed.html')