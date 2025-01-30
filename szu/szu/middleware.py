from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth import logout

class AutoLogout:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)

        try:
            last_activity = datetime.strptime(request.session['last_activity'], '%Y-%m-%d %H:%M:%S.%f')
            now = datetime.now()
            if now - last_activity > timedelta(seconds=settings.SESSION_COOKIE_AGE):
                logout(request)
                del request.session['last_activity']
        except KeyError:
            pass

        request.session['last_activity'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        return self.get_response(request)
