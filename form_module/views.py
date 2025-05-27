from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import ContactSubmission  # Import your model

def contact_view(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            ContactSubmission.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

class homeView(TemplateView):
    template_name = 'home.html'
