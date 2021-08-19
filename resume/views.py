from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'home.html', {'form' : form})