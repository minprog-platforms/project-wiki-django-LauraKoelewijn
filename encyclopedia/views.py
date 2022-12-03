from django.shortcuts import render

from . import util
import markdown

def convert_markdown(title):
    """Converts text from markdown to html and returns it
    if the page is not empty"""
    text = util.get_entry(title)
    while text is not None:
        return markdown.markdown(text)

def index(request):
    """Returns a render of the index page."""
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def notfound(request):
    """Returns a render of the 404error page."""
    return render(request, "encyclopedia/404error.html", {
    })

def notallowed(request):
    """Returns a render of the 409error page."""
    return render(request, "encyclopedia/409error.html", {
    })

def entry(request, title):
    """Returns a render of the entry page if the page is not empty. """
    existing_page = convert_markdown(title)
    if existing_page is not None:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": existing_page
            })
    else:
        return render(request, "encyclopedia/404error.html")

def random_page(request):
    """Returns a render of a random page."""
    return render(request, "encyclopedia/randompage.html", {
        "page": util.list_entries()
    })

def search(request):
    """Returns a render of a search results."""
    searched_entry = request.POST['q']

    if request.method == "POST":
        results = convert_markdown(searched_entry)
        if results is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": searched_entry,
                "content": results
            })
        else:
            len_query = len(searched_entry)
            all_entries = util.list_entries()
            len_list = len(all_entries)
            list_entries = []

            for i in range(len_list):
                if all_entries[i][ 0 : len_query ].lower() == searched_entry.lower():
                    list_entries.append(all_entries[i])

            return render(request, "encyclopedia/search.html", {
                "len_query": len_query,
                "len_list": len_list,
                "list_entries": list_entries
            })

def new_page(request):
    """Returns a render of a page where the user
    can create their own new page."""
    """Saves entered data in form at newpage.html"""
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html", {
            "page": util.list_entries()
        })
    else:
        title = request.POST['new_title']
        content = request.POST['new_content']
        title = convert_markdown(title)
        if title is not None:
            return render(request, "encyclopedia/409error.html")
        else:
            util.save_entry(title, content)
            newpage_content = convert_markdown(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": newpage_content
            })
