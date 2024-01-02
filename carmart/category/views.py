from django.shortcuts import render, redirect
# from .forms import AuthorForm
from . import forms


def addCategory(request):
    if request.method == 'POST':
        categoryFrom = forms.CategoryFrom(request.POST)
        if categoryFrom.is_valid():
            categoryFrom.save()
            return redirect('add_Category')

    else:
        categoryFrom = forms.CategoryFrom()
    return render(request, 'addCategory.html', {'form': categoryFrom})
