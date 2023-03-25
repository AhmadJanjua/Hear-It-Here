from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Post, Category, Comment
from .forms import PostForm, CommentForm


# create a post under a specific category
@login_required
def create_post(request, category_id):
    # get a category object using the id
    category = Category.objects.get(id=category_id)
    # check if the post form is submitted
    if request.method == 'POST':
        form = PostForm(request.POST)
        # validate form, submit and redirect to post pages
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.category = category
            post.save()
            return redirect('forum:posts', category_id=category_id)
    # if there is no existing form, produce one
    else:
        form = PostForm()
    # render the form and pass category information
    return render(request, 'forum/create_post.html', {'form': form, 'category': category})


# Deletes a post if the user is a mod or the person logged in is the one deleting it
@login_required
def delete_post(request, category_id, post_id):
    # get the post
    post = get_object_or_404(Post, id=post_id)
    # check permission
    if post.user.id == request.user.id or request.user.is_mod:
        post.delete()
    previous_url = request.META.get('HTTP_REFERER')
    if previous_url:
        return redirect(previous_url, )
    else:
        # reload the posts page
        return redirect('forum:posts', category_id=category_id)


# deletes a comment if the user is a moderator or if they made the comment
@login_required
def delete_comment(request, comment_id):
    # get the comment object
    comment = get_object_or_404(Comment, id=comment_id)
    # check permission
    if comment.user.id == request.user.id or request.user.is_mod:
        comment.delete()
    # redirect to the post where the comment was initially present
    return redirect('forum:view_post', category_id=comment.post.category.id, post_id=comment.post.id)


# browse the existing posts in a category
def browse_posts(request, category_id):
    # try to get the object
    category = get_object_or_404(Category, id=category_id)
    # get all posts by date they are made
    posts = Post.objects.filter(category_id=category_id).order_by('-time')
    # render all the images
    return render(request, 'forum/posts.html', {'category': category, 'posts': posts})


# view a post with the ability to comment if logged in
def view_post(request, category_id, post_id):
    # find the object if it exists
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    if request.method == 'POST':
        # get the comment form
        form = CommentForm(request.POST)
        # validate and submit the comment
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            # Redirect to the same page to display the new comment
            return redirect('forum:view_post', category_id=category_id, post_id=post_id)
    # if there is no form make one
    else:
        form = CommentForm()
    # render the post page
    return render(request, 'forum/detail.html', {'post': post, 'form': form, 'comments': comments})


# Search for forums
def search_forum(request):
    # check if there was a form filled
    if request.method == "POST":
        # check what was searched
        searched = request.POST['search_forum']
        # retrieve all matching posts
        posts = Post.objects.filter(Q(title__contains=searched) | Q(user__username__contains=searched))
        # display results
        return render(request, 'forum/search_forum.html', {'searched': searched, 'posts': posts})
    # pass a page regardless
    return render(request, 'forum/search_forum.html')
