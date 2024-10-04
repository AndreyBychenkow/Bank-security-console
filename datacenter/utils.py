HOURS_IN_SECONDS = 3600
MINUTES_IN_SECONDS = 60
LONG_VISIT_THRESHOLD = 60


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, HOURS_IN_SECONDS)
    minutes, seconds = divmod(remainder, MINUTES_IN_SECONDS)
    return f'{hours:02}:{minutes:02}:{seconds:02}'


def is_visit_long(visit):
    duration = visit.leaved_at - visit.entered_at
    return duration.total_seconds() // MINUTES_IN_SECONDS > LONG_VISIT_THRESHOLD
