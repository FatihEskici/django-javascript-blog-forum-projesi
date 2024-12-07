from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category
from .forms import CommentForm, PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils import timezone
from .forms import NewsletterForm


def home(request):
    category_id = request.GET.get('category')  # URL'den kategori parametresini al
    if category_id:
        posts = Post.objects.filter(category_id=category_id)  # Kategoriye göre gönderileri filtrele
    else:
        posts = Post.objects.all()  # Tüm gönderileri al

    featured_posts = Post.objects.filter(is_featured=True)  # Öne çıkan gönderiler
    popular_posts = Post.objects.order_by('-views')[:5]  # En popüler gönderiler
    categories = Category.objects.all()  # Tüm kategoriler
    recent_comments = Comment.objects.order_by('-created_at')[:5]
    current_time = timezone.now()  

    return render(request, 'blog/home.html', {
        'posts': posts,
        'featured_posts': featured_posts,
        'popular_posts': popular_posts,
        'categories': categories,
        'recent_comments': recent_comments,
        'current_time': current_time
    })


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.views += 1  
    post.save()  
    comments = post.comments.all()  
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'blog/profile.html')


def create_post(request):
    if not request.user.is_authenticated:
        
        return render(request, 'blog/please_login.html')  

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog-home')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

# Kategorilere göre yazıları listeleme
def posts_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = category.posts.all()
    return render(request, 'blog/posts_by_category.html', {'category': category, 'posts': posts})

# Custom Login View
class CustomLoginView(LoginView):
    def get_success_url(self):
        
        if self.request.user.is_superuser or self.request.user.is_staff:
            return reverse_lazy('admin:index')
        return reverse_lazy('blog-home')


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})


def settings(request):
    return render(request, 'blog/settings.html')

def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bültene başarıyla abone oldunuz!')
            return redirect('blog-home')
    else:
        form = NewsletterForm()
    return render(request, 'blog/newsletter_subscribe.html', {'form': form})

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        

        messages.success(request, 'Geri bildiriminiz başarıyla gönderildi!')
        return redirect('blog-home')  

    return render(request, 'blog/home.html')  