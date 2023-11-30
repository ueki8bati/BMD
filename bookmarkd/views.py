from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Dictionary
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import DictionaryForm

# Create your views here.

@login_required
def index(request):
    bookmarks = Dictionary.objects.all()
    return render(request, 'bookmarkd/index.html',{'bookmarks':bookmarks})

@login_required
def detail(request, id):
    bookmark = get_object_or_404(Dictionary, id=id)
    return render(request, 'bookmarkd/detail.html', {'bookmark': bookmark})

@login_required
def add(request):
    if request.method == "POST":
        form = DictionaryForm(request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.author = request.user
            bookmark.date = timezone.now()
            bookmark.save()
            return render(request, 'bookmarkd/detail.html', {'bookmark': bookmark})
    else:
        form = DictionaryForm()
    return render(request, 'bookmarkd/edit.html', {'form': form})