from django.shortcuts import render

from . import util
import markdown

def convert_markdown(entry):
    """Converts text from markdown to html and returns it
    if the page is not empty"""
    text = util.get_entry(entry)
    while text is not None:
        return True
        return markdown.markdown(text)

    return False

def index(request):
    """Returns a render of the index page."""
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def error(request):
    """Returns a render of the error page."""
    return render(request, "encyclopedia/error.html", {
        "error": util.list_entries()
    })

def entry(request, entry):
    """Returns a render of the entry page if the page is not empty. """
    existing_page = convert_markdown(entry)
    if existing_page == True:
        return render(request, "encyclopedia/entry.html", {
            "title": entry.capitalize(),
            "content": existing_page
            })
    else:
        return render(request, "encyclopedia/error.html")

def new_page(request):
    """Returns a render of a page where the user
    can create their own new page."""
    return render(request, "encyclopedia/newpage.html", {
        "page": util.list_entries()
    })

def random_page(request):
    """Returns a render of a random page."""
    return render(request, "encyclopedia/randompage.html", {
        "page": util.list_entries()
    })
