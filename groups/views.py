from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Group

def Groups(request):
    groups = Group.objects.filter(author=request.user)
    context = {
        'groups': groups,
    }
    return render(request, 'groups/groups.html', context)


class GroupDetailView(DetailView):
    model = Group
    
class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['name']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class GroupUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Group
    fields = ['name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        group = self.get_object()
        if self.request.user == group.author:
            return True
        return False

class GroupDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Group
    success_url = '/'
    
    def test_func(self):
        group = self.get_object()
        if self.request.user == group.author:
            return True
        return False
