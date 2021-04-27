from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import Http404
from .forms import RegistrationForm, PostForm, CommentForm
from .models import Post, Comment



# Create your views here.
def index(req):
	queryset = Post.objects.filter(status=1).order_by('-date_created')
	contxt = {'title': 'Blog', 'posts': queryset}
	return render(req, 'blog/index.html', contxt)


def blog_admin_index(req, filter):
	if filter == 'All':
		queryset = Post.objects.filter(author=req.user).order_by('-date_created')
	elif filter == 'Draft':
		queryset = Post.objects.filter(status=0, author=req.user).order_by('-date_created')
	elif filter =='Published':
		queryset = Post.objects.filter(status=1, author=req.user).order_by('-date_created')
	else:
		raise Http404('Path does not exist')

	contxt = {'title': 'Blog', 'posts': queryset, 'status': ['Draft', 'Published'] }
	return render(req, 'blog/blog_admin.html', contxt)


def signin(req):
	if req.user.is_authenticated:
		return redirect('blog_admin_index', filter='All')
	if req.method == 'POST':
		username = req.POST['username']
		password = req.POST['password']
		user = authenticate(req, username=username, password=password)
		if user is not None:
			login(req, user)
			return redirect('blog_admin_index', filter='All')
		else:
			form = AuthenticationForm(req.POST)
			return render(req, 'blog/signin.html', {'form': form})
	else:
		form = AuthenticationForm()
		return render(req, 'blog/signin.html', {'title':'Sign In', 'form': form})

def signup(req):
	if req.user.is_authenticated:
		return redirect('blog_index')
	if req.method == 'POST':
		form = RegistrationForm(req.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.first_name = form.cleaned_data.get('first_name')
			user.profile.last_name = form.cleaned_data.get('last_name')
			user.profile.middle_name = form.cleaned_data.get('middle_name')
			user.profile.email = form.cleaned_data.get('email')
			user.profile.birth_date = form.cleaned_data.get('birth_date')
			user.save()
			return redirect('blog_signin')
	else:
		form = RegistrationForm()
	contxt = {
				'title': 'Sign up',
				'form': form,
			}
	return render(req, 'blog/form.html', contxt)


def signout(req):
	logout(req)
	return redirect('/')


def create_post(req):
	if not req.user.is_authenticated:
		return redirect('blog_index')


	if req.method == 'POST':
		form = PostForm(req.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = req.user
			post.date_modified = timezone.now()
			post.status = int(form.cleaned_data.get('publish'))
			post.save()

	else:
		form = PostForm()
	contxt = {'title': 'Create Post', 'form': form}
	return render(req, 'blog/create_post.html', contxt)	

def blog_detail(req, slug):
	queryset = get_object_or_404(Post, slug=slug)
	comments = Comment.objects.filter(post=queryset)

	if req.method == 'POST' and req.user.is_authenticated:
		form = CommentForm(req.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.author = req.user
			comment.post = queryset
			comment.save()
	
	form = CommentForm()

	contxt = {'title':queryset.title, 'post': queryset, 'form': form, 'comments':comments, }
	return render(req, 'blog/blog_detail.html', contxt)


def update_blog(req, slug):
	queryset = get_object_or_404(Post, slug=slug)
	form = PostForm(instance=queryset)

	if req.method=='POST':
		form = PostForm(req.POST, instance=queryset)
		if form.is_valid():
			post = form.save(commit=False)
			post.date_modified = timezone.now()
			post.status = int(form.cleaned_data.get('publish'))
			post.save()

	contxt = {'title':queryset.title, 'form': form, 'post': queryset}
	return render(req, 'blog/blog_modify.html', contxt)	


def delete_blog(req, slug):
	queryset = get_object_or_404(Post, slug=slug)
	queryset.delete()
	return redirect('blog_admin_index', filter='All')

def password_change(req):
	if not req.user.is_authenticated:
		return redirect('blog_index')

	msg = ''

	if req.user.is_authenticated and req.method=='POST':
		password = req.POST['new_password']
		user = get_object_or_404(User, username=req.user.username)
		user.set_password(password)
		user.save()
		msg = "Password Changed Successfully"

	return render(req, 'blog/reset_password.html', {'message': msg})

