import requests
import json

from django.contrib.auth.backends import RemoteUserBackend


class HubAuthentiationBackend(RemoteUserBackend):
    def authenticate(self, username=None, password=None):
        try:
            headers = {'content-type': 'application/json'}
            payload = {'username': username, 'password': password}
            r = requests.post(
                'http://192.168.59.103:8000/users/login/',
                data=json.dumps(payload),
                headers=headers
            )
            if r.status_code == 200:
                user = super(HubAuthentiationBackend, self).authenticate(username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
                if user is not None:
                    return user
                else:
                    raise Exception('Invalid login')
        except Exception as e:
            raise Exception(e)
