from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NoteForm
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect(to='notes_list')
    return render(request, "home.html")


@login_required
def notes_list(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect(to='notes_list')
    else:
        form = NoteForm()

    notes = request.user.notes.order_by('-modified')
    return render(request, "notes/notes_list.html", {
        "notes": notes,
        "form": form,
    })
