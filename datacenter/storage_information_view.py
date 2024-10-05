from django.shortcuts import render
from django.utils.timezone import localtime, now

from datacenter.models import Visit
from datacenter.utils import format_duration, is_visit_long


def get_duration(entered_at):
    entered_at_local = localtime(entered_at)
    duration = now() - entered_at_local
    return duration


def storage_information_view(request):
    ongoing_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for visit in ongoing_visits:
        duration = get_duration(visit.entered_at)

        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at).strftime('%d-%m-%Y %H:%M:%S'),
            'duration': format_duration(duration),
            'is_strange': is_visit_long(visit)
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
