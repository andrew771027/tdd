
from django.test import TestCase
from django.contrib.auth import get_user_model, SESSION_KEY
from django.http import HttpRequest
from unittest.mock import patch
from accounts.views import persona_login
User = get_user_model()


class LoginViewTest(TestCase):

    @patch('accounts.views.authenticate')
    def test_calls_authenticate_with_assertion_from_post(self, mock_authenticate):
        mock_authenticate.return_value = None
        self.client.post('/accounts/login', {'assertion': 'assert this'})
        mock_authenticate.assert_called_once_with(assertion='assert this')

    @patch('accounts.views.authenticate')
    def test_returns_OK_when_user_found(self, mock_authenticate):
        user = User.objects.create(email='a@b.com')
        user.backend = ''   # 需要驗證登入才可以動作
        mock_authenticate.return_value = user
        response = self.client.post('/accounts/login', {'assertion': 'a'})
        self.assertEqual(response.content.decode(), 'OK')

    @patch('accounts.views.authenticate')
    def test_gets_logged_in_session_if_authenticate_returns_a_user(self, mock_authenticate):
        user = User.objects.create(email='a@b.com')
        user.backend = ''   # required for auth_login to work
        mock_authenticate.return_value = user
        self.client.post('/accounts/login', {'assertion': 'a'})
        self.assertEqual(self.client.session[SESSION_KEY], str(user.pk))

    @patch('accounts.views.authenticate')
    def test_does_not_get_logged_in_if_authenticate_returns_None(self, mock_authenticate):
        mock_authenticate.return_value = None
        self.client.post('/accounts/login', {'assertion': 'a'})
        self.assertNotIn(SESSION_KEY, self.client.session)

    @patch('accounts.views.login')
    @patch('accounts.views.authenticate')
    def test_calls_auth_login_if_authenticate_returns_a_user(self, mock_authenticate, mock_login):
        request = HttpRequest()
        request.POST['assertion'] = 'asserted'
        mock_user = mock_authenticate.return_value
        persona_login(request)
        mock_login.assert_called_once_with(request, mock_user)
