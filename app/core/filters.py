from pytz import timezone

from . import core


@core.app_template_filter('int_date')
def format_datetime(date):
    utc_time = timezone("UTC")
    london_time = timezone("Europe/London")
    if date:
        return utc_time.localize(date).astimezone(london_time).strftime('%Y-%m-%d %H:%M')
    return date
