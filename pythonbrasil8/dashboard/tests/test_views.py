from django.test import TestCase
from django.test.client import RequestFactory, Client
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from pythonbrasil8.dashboard.views import IndexView, ProfileView
from pythonbrasil8.dashboard.forms import ProfileForm
from pythonbrasil8.dashboard.models import AccountProfile
from pythonbrasil8.schedule.models import Session


class DashboardIndexTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory().get("/")
        self.request.user = User.objects.create_user(username="user", password='test')
        session = Session.objects.create(
            title="Python for dummies",
            description="about python, universe and everything",
            type="talk",
            tags="python, 42",
        )
        session.speakers.add(self.request.user)

    def test_should_be_a_template_view(self):
        self.assertTrue(issubclass(IndexView, TemplateView))

    def test_shoud_use_a_dashboard_template(self):
        self.assertEqual('dashboard/index.html', IndexView.template_name)

    def test_should_redirects_if_user_is_not_logged_in(self):
        self.request.user.is_authenticated = lambda : False
        result = IndexView.as_view()(self.request)
        self.assertEqual(302, result.status_code)

    def test_should_have_200_status_code_when_user_is_logged_in(self):
        result = IndexView.as_view()(self.request)
        self.assertEqual(200, result.status_code)

    def test_should_have_sessions_on_context(self):
        result = IndexView.as_view()(self.request)
        self.assertIn('sessions', result.context_data)
        self.assertQuerysetEqual(result.context_data['sessions'], [u"Python for dummies",], lambda s: s.title)

    def test_get_url_should_return_200(self):
        client = Client()
        client.login(username=self.request.user.username, password='test')
        response = client.get('/dashboard/')
        self.assertEqual(200, response.status_code)


class ProfileViewTestCase(TestCase):

    @classmethod
    def setUpClass(self):
        self.user = User.objects.create_user(username="user", password="test")
        self.account_profile = AccountProfile.objects.create(user=self.user)

    def setUp(self):
        self.request = RequestFactory().get("/")
        self.request.user = User.objects.get(id=self.user.id)
        self.response = ProfileView.as_view()(self.request, pk=self.account_profile.id)

    @classmethod
    def tearDownClass(self):
        self.account_profile.delete()

    def test_should_use_expected_template(self):
        self.assertTemplateUsed(self.response, 'dashboard/profile.html')

    def test_model_should_be_AccountProfile(self):
        self.assertEqual(AccountProfile, ProfileView.model)

    def test_form_should_be_ProfileForm(self):
        self.assertEqual(ProfileForm, ProfileView.form_class)

    def test_success_url_should_be_deashboard(self):
        self.assertEqual('/dashboard/', ProfileView.success_url)

    def test_should_redirects_if_user_is_not_logged_in(self):
        self.request.user.is_authenticated = lambda : False
        result = ProfileView.as_view()(self.request, pk=self.account_profile.id)
        self.assertEqual(302, result.status_code)

    def test_should_have_200_status_code_when_user_is_logged_in(self):
        self.assertEqual(200, self.response.status_code)

    def test_update_account_user_with_success(self):
        data = {
            'id': self.account_profile.id,
            'user': self.user.id,
            'name': 'siminino',
            'description': 'simi test',
            'type': 'Student',
            'tshirt': 'M'
        }

        request = RequestFactory().post('/', data)
        request.user = self.request.user
        response = ProfileView.as_view()(request, pk=self.account_profile.id)
        self.assertEqual(302, response.status_code)

        profile = AccountProfile.objects.get(id=self.account_profile.id)
        self.assertEqual('siminino', profile.name)
        self.assertEqual('simi test', profile.description)
        self.assertEqual('Student', profile.type)
        self.assertEqual('M', profile.tshirt)

    def test_get_url_should_return_200(self):
        client = Client()
        client.login(username=self.request.user.username, password='test')
        response = client.get('/dashboard/profile/')
        self.assertEqual(200, response.status_code)
