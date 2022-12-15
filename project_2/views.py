from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    # num_books = Book.objects.all().count()
    # num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    # num_authors = Author.objects.count()

    context = {
        'num_books': 2,
        'num_instances': 33,
        'num_instances_available': 21,
        'num_authors': 231,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)