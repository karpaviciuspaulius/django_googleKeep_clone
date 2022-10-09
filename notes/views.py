from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Note
from groups.models import Group
from .filter import NoteFilter

def notes(request):
    notes = Note.objects.filter(author=request.user).order_by('-date_created')
    myFilter = NoteFilter(request.GET, queryset=notes)
    notes = myFilter.qs
    context = {
        'notes': notes,
        'myFilter': myFilter,
    }
    return render(request, 'notes/notes.html', context)


class NoteDetailView(DetailView):
    model = Note
    
class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content', 'image', 'categories']

    def get_form(self, *args, **kwargs):
        form = super(NoteCreateView, self).get_form(*args, **kwargs)
        form.fields['categories'].queryset = Group.objects.filter(author=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'content', 'image', 'categories']

    def get_form(self, *args, **kwargs):
        form = super(NoteUpdateView, self).get_form(*args, **kwargs)
        form.fields['categories'].queryset = Group.objects.filter(author=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False

    

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = '/'
    
    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False

def about(request):
    return render(request, 'notes/about.html', {'title': 'About'})