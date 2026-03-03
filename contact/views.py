from django.shortcuts import render, redirect

from .models import ContactUS
from .form import ContactForm


# def contact_in(request):
#     contact_info = ContactInfo.objects.all()
#     context = {
#         'contacts_info': contact_info,
#     }
#     return render(request, 'contact.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
