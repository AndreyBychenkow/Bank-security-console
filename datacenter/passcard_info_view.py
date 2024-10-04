from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.utils import format_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    visits = Visit.objects.filter(passcard=passcard).order_by('-entered_at')

    this_passcard_visits = []

    for visit in visits:
        duration = visit.leaved_at - visit.entered_at if visit.leaved_at else None

        this_passcard_visits.append({
            'entered_at': localtime(visit.entered_at).strftime('%d-%m-%Y %H:%M'),
            'duration': format_duration(duration) if duration else "Still inside",
            'is_strange': is_visit_long(visit) if visit.leaved_at else False
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
