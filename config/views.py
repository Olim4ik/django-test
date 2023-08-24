from django.http import JsonResponse
from django.utils import timezone
from pytz import timezone as pytz_timezone
from zoneinfo import ZoneInfo

from config.settings.settings import TIME_ZONE


def index(request):
    user_timezone = request.COOKIES.get('user_timezone')  # Get user's selected time zone from cookies
    if user_timezone:
        local_time_zone = pytz_timezone(user_timezone)
    else:
        local_time_zone = timezone.get_default_timezone()

    current_time = timezone.now()
    local_current_time = current_time.astimezone(local_time_zone)
    
    django_time_zone = ZoneInfo(TIME_ZONE)
    test_time = current_time.astimezone(django_time_zone)
    
    context = {
        "time_zone": user_timezone,
        "current_time": local_current_time,
        "django_time_zone": test_time
    }

    return JsonResponse(context)
