from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from activities.models import Activity, Option, Vote
from common.views_utils import json_response
from common.debug_utils import debug


@login_required(login_url='/accounts/login')
def list_view(request):
    activity_list = Activity.objects.filter(
        end_datetime__gte=timezone.now())

    status = request.GET.get('status', '0')
    if status == '1':
        activity_list = Activity.objects.filter(
            end_datetime__lt=timezone.now())

    paginator = Paginator(activity_list, 9)

    page = request.GET.get('page', 1)
    activities = paginator.get_page(page)

    return render(
        request,
        'activities/list.html',
        {'activities': activities})


@login_required(login_url='/accounts/login')
def detail_view(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    remaining_vote_num = activity.get_remaining_vote_num(request.user)
    options = activity.option_set.all()
    if activity.is_finished:
        options = activity.get_ordered_options()

    return render(
        request, 'activities/detail.html',
        {'activity': activity,
         'options': options,
         'remaining_vote_num': remaining_vote_num})


@login_required(login_url='/accounts/login')
def vote_view(request):
    activity_id = request.POST.get('activity_id', None)
    activity = get_object_or_404(Activity, pk=activity_id)
    user = request.user
    option_id_list = request.POST.getlist('option_id', [])
    if (not activity.is_finished and not activity.get_remaining_vote_num(user) < len(option_id_list)):
        for option_id in option_id_list:
            option = get_object_or_404(Option, pk=option_id)
            vote = Vote()
            vote.option = option
            vote.voter = user
            vote.save()

    return redirect('/activities/detail/%s/' % activity_id)


@login_required(login_url='/accounts/login')
def create_view(request):
    if not request.user.can_create_vote:
        return redirect('/activities/list/')

    if request.POST:
        activity = Activity()
        activity.title = request.POST.get('title', '')
        activity.vote_num_per_user = request.POST.get('vote_num_per_user', 8)
        activity.sponsor = request.user
        activity.end_datetime = request.POST.get('end_datetime', None)
        activity.save()

        images = request.FILES.getlist('option_image', [])
        contents = request.POST.getlist('option_content', [])
        for image, content in zip(images, contents):
            option = Option()
            option.image = image
            option.content = content
            option.activity = activity
            option.save()

        return redirect('/activities/detail/%s/' % activity.id)
    else:
        return render(request, 'activities/create.html')


@login_required(login_url='/accounts/login')
def edit_view(request):
    return json_response({'is_success': True})
