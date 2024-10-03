from django.shortcuts import render
from django.utils.timezone import localtime, now

from datacenter.models import Visit


def get_duration(entered_at):
    entered_at_local = localtime(entered_at)
    duration = now() - entered_at_local
    return duration


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours:02}:{minutes:02}:{seconds:02}'


def storage_information_view(request):
    ongoing_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for visit in ongoing_visits:
        duration = get_duration(visit.entered_at)

        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at).strftime('%d-%m-%Y %H:%M:%S'),
            'duration': format_duration(duration),
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
