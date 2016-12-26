from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import DetailView, ListView, UpdateView
from comments.models import Comment
from .forms import SearchForm
from .models import Album
from django.shortcuts import get_object_or_404
from django.db.models import Q


class AlbumList(ListView):
    model = Album
    template_name = 'album_list.html'
    context_object_name = 'album'
    paginate_by = 4

    def dispatch(self, request, *args, **kwargs):
        self.search_form = SearchForm(request.GET)
        return super(AlbumList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Album.objects.all().shown_for(self.request.user)
        queryset = queryset.select_related('author').annotate(buyers = models.Count('bought_by'))
        #queryset = Album.objects.all()
        if self.search_form.is_valid():
            queryset = queryset.filter(name__icontains=self.search_form.cleaned_data['search'])
            queryset = queryset.order_by(self.search_form.cleaned_data['sort'])
            return queryset
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AlbumList, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form
        return context

class AlbumView(CreateView):
    model = Comment
    template_name = "album.html"
    context_object_name = 'album'
    fields = ('text',)

    def dispatch(self, request, pk = None, *args, **kwargs):
        self.album = get_object_or_404(Album, id=pk)
        return super(AlbumView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AlbumView, self).get_context_data(**kwargs)
        context['album'] = self.album
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.album = self.album
        return super(AlbumView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('albums:detail', kwargs={'pk':self.album.id})

class EditAlbum(UpdateView):
    model = Album
    template_name = 'album_edit.html'
    fields = ('name','genre','photo','information', 'file')

    def get_queryset(self):
        return Album.objects.filter(author=self.request.user)

    def form_valid(self, form):
        response = super(EditAlbum, self).form_valid(form)
        return HttpResponse('OK')

class CreateAlbum(CreateView):
    model = Album
    template_name = 'create_album.html'
    fields = ('name', 'genre','photo','information',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateAlbum, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('albums:detail', kwargs={'pk':self.object.id})

# class CreateCommentView(CreateView):
#     model = Comment
#     fields = ('text')
#     def get_success_url(self):
#         return reverse('albums:album')
#     def form_valid(self, form):
#         #form.instance.album = self.
#         form.instance.author = self.request.user
#         return super(CreateCommentView, self).form_valid(form)