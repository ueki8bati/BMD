from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Dictionary
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import DictionaryForm
from django.views.decorators.http import require_POST
from django.db.models import Q

from .getURL import get_url
from .mecab import get_url_tag

now_queryset = None

# Create your views here.
class Index(LoginRequiredMixin, generic.ListView):
    template_name = 'bookmarkd/index.html'
    def get_queryset(self):
        global now_queryset
        query = self.request.GET.get('query')
        queryset = Dictionary.objects.filter(author=self.request.user)

        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(tag__icontains=query) | Q(url_tag__icontains=query))
        now_queryset = queryset
        return queryset

@login_required
def detail(request, id):
    global now_queryset
    if now_queryset == None:
        queryset = Dictionary.objects.filter(author=request.user)
    else:
        queryset = now_queryset
    bookmark = get_object_or_404(Dictionary, id=id, author=request.user)
    return render(request, 'bookmarkd/detail.html', {'bookmark': bookmark,'object_list': queryset})

@login_required
def add(request):
    global now_queryset
    if request.method == "POST":
        form = DictionaryForm(request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.author = request.user
            bookmark.url_tag = get_url_tag(get_url(bookmark.url))
            bookmark.date = timezone.now()
            bookmark.save()
            queryset = Dictionary.objects.filter(author=request.user)
            return render(request, 'bookmarkd/detail.html', {'bookmark': bookmark,'object_list': queryset})
    else:
        form = DictionaryForm()
    if now_queryset == None:
        queryset = Dictionary.objects.filter(author=request.user)
    else:
        queryset = now_queryset
    return render(request, 'bookmarkd/edit.html', {'form': form,'object_list': queryset})

@login_required
def edit(request,id):
    global now_queryset
    bookmark = get_object_or_404(Dictionary, id=id)
    if request.method == "POST":
        form = DictionaryForm(request.POST, instance=bookmark)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.author = request.user
            bookmark.url_tag = get_url_tag(get_url(bookmark.url))
            bookmark.date = timezone.now()
            bookmark.save()
            if now_queryset == None:
                queryset = Dictionary.objects.filter(author=request.user)
            else:
                queryset = now_queryset
            return render(request, 'bookmarkd/detail.html', {'bookmark': bookmark,'object_list': queryset})
    else:
        form = DictionaryForm(instance=bookmark)
    if now_queryset == None:
        queryset = Dictionary.objects.filter(author=request.user)
    else:
        queryset = now_queryset
    return render(request, 'bookmarkd/edit.html', {'form': form,'object_list': queryset})

@require_POST
def delete(request, id):
    bookmark = get_object_or_404(Dictionary, id=id)
    bookmark.delete()
    bookmarks = Dictionary.objects.filter(author=request.user)
    return render(request, 'bookmarkd/index.html', {'bookmarks': bookmarks})

