import requests
import sys
import logging
from django.conf import settings
from accounts.models import User

PERSONA_VERIFY_URL = 'https://verifier.login.persona.org/verify'

logger = logging.getLogger(__name__)


class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        logger.warning('entering authenticate function')
        # send assertion to mozilla auth services
        data = {'assertion': assertion, 'audience': settings.DOMAIN}
        print('sending to mozilla', data, file=sys.stderr)
        resp = requests.post(PERSONA_VERIFY_URL, data=data)
        print('got', resp.content, file=sys.stderr)
        logger.warning('got response from persona')
        logger.warning(resp.content.decode())

        if resp.ok and resp.json()['status'] == 'okay':
            verification_data = resp.json()

            if verification_data['status'] == 'okay':
                email = verification_data['email']
                try:
                    return self.get_user(email)
                except User.DoesNotExist:
                    return User.object.create(email=email)
        else:
            logger.warning(f'Persona says no. Json was {resp.json()}')

    def get_user(self, email):
        return User.objects.get(email=email)
