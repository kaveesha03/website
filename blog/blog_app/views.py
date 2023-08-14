

# Create your views here.

from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import Blog




def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            request.session['signup_name'] = name  # Store the signup name in the session
            return redirect('home')  # Replace 'home' with the name of your home view
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})





def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})




from .forms import CreatePostForm


def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.session.get('signup_name')  # Retrieve the signup name from the session
            blog.save()
            return redirect('home')  # Replace 'home' with the name of your home view
    else:
        form = CreatePostForm(initial={'author': request.session.get('signup_name')})  # Set the initial value for the author field

    return render(request, 'create_post.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog

def delete_post(request, post_id):
    blog = get_object_or_404(Blog, pk=post_id)

    # Check if the current user is the author of the post
    if request.session.get('signup_name') == blog.author:
        # User is the author, allow post deletion
        blog.delete()

    return redirect('home')  # Replace 'home' with the name of your home view
