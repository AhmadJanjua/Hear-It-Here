from django.shortcuts import render
from forum.models import Category


# The home is a page with all categories and some stats displayed
def home_response(request):
    # get all categories
    categories = Category.objects.all()
    # loop through and get total number of posts
    total = 0
    for category in categories:
        total += category.post_set.count()
    # render the home page with category info
    return render(request, 'index.html', {'categories': categories, 'total': total})
