from post.models import Category


def get_category_context(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return context