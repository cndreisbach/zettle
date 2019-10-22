from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect(to='notes_list')
    return render(request, "home.html")


def notes_list(request):
    notes = request.user.notes.order_by('-modified')
    return render(request, "notes/notes_list.html", {"notes": notes})
