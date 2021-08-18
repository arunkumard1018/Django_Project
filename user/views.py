from django.shortcuts import redirect, render
from .models import post
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first_name')
            messages.success(request,f'Account Created Succesfully for {user}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request,'user/register.html',{'form':form})

@login_required # To redirect Login page if user not Logdin
def profile(request):
    context = {'post' : request.user.post_set.all()}
    return render(request,'user/profile.html',context)


class PostListView(ListView):
    model = post
    template_name = 'user/home.html' ## <app>/<model>_<viewtype>.html By default
    context_object_name = 'post'
    ordering = ['-created_at']
    paginate_by = 5

class PostDetailView(DetailView):
    model = post
    #look for <app_name>/<model_view_type.html>
    #i.e user/post_Detail.html

class PostCreateView(CreateView, LoginRequiredMixin):
    model = post
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = post
    fields = ['title', 'text',]

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):

    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
    
    