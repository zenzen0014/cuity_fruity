from corsheaders.signals import check_request_enabled

from .models import Profile

def cors_allow_mysites(sender, request, **kwargs):
    # return Profile.objects.filter(host=request.host).exists()
    return request.path.startswith('/customer/')

check_request_enabled.connect(cors_allow_mysites)