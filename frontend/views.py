from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# # Create your views here.
@login_required
def homepage(request):
    return render(request, "pages/about.html")


@login_required
def image_classifier(request):
    return render(request, "pages/classifier.html")


@login_required
def team_page(request):
    return render(request, "pages/team.html")


@login_required
def settings_page(request):
    return render(request, "pages/settings.html")


def change_theme(request, **kwargs):
    if 'is_dark_theme' in request.session:
        request.session['is_dark_theme'] = not request.session['is_dark_theme']
    else:
        request.session['is_dark_theme'] = True

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
