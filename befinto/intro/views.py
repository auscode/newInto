from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'intro/base.html',{"message":"hey im in"})

def index(request):
    return render(request,'intro/index.html')

from django.shortcuts import render
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # Validate the form data
            # Process the form data and save it to the database (not shown in this example)
            # You can access the form data using form.cleaned_data

            # Redirect to a success page or perform other actions
            return render(request, 'intro/success.html')
    else:
        form = BookForm()

    return render(request, 'intro/add_book.html', {'form': form})
