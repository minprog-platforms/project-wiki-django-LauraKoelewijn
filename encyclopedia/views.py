from django.shortcuts import render

from . import util


def index(request):
    """Returns a render of the index page."""
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def error(request):
    """Returns a render of the error page."""
    return render(request, "encyclopedia/error.html", {
        "page": util.get_entry()
    })

def entry(request, entry):
    """Returns a render of the entry page."""
    return render(request, "encyclopedia/entry.html", {
        "entry": entry.capitalize()
    })

def new_page(request):
    """Returns a render of a page where the user
    can create their own new page."""
    return render(request, "encyclopedia/newpage.html", {
        "page": util.get_entry()
