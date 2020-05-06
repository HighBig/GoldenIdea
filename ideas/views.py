from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from ideas.models import Idea
from common.views_utils import json_response


@login_required(login_url='/accounts/login')
def list_view(request):
    keywords = request.GET.get('keywords', '')
    if keywords:
        idea_list = Idea.objects\
                        .filter(Q(title__icontains=keywords) |
                                Q(description__icontains=keywords))
    else:
        idea_list = Idea.objects.all()

    paginator = Paginator(idea_list, 10)

    page = request.GET.get('page', 1)
    ideas = paginator.get_page(page)
    return render(request, 'ideas/list.html', {'ideas': ideas})


@login_required(login_url='/accounts/login')
def detail_view(request, idea_id):
    return render(request, 'ideas/detail.html')


@login_required(login_url='/accounts/login')
def create_view(request):
    idea = Idea()
    title = request.POST.get('title', '')
    description = request.POST.get('description', '')
    idea.title = title
    idea.description = description
    idea.user = request.user
    idea.save()
    return json_response({'is_success': True})
