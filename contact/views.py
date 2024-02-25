from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})

