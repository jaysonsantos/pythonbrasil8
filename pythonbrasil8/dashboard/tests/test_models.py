from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User

from pythonbrasil8.dashboard.models import AccountProfile
from pythonbrasil8.subscription.models import Subscription


class AccountProfileTestCase(TestCase):

    @classmethod
    def setUpClass(self):
        self.field_names = AccountProfile._meta.get_all_field_names()

    def test_should_has_user_field(self):
        self.assertIn('user', self.field_names)

    def test_user_field_should_be_one_to_one_field(self):
        field = AccountProfile._meta.get_field_by_name('user')[0]
        self.assertEqual(models.OneToOneField, field.__class__)

    def test_should_has_description_field(self):
        self.assertIn('description', self.field_names)

    def test_description_field_should_be_char_field(self):
        field = AccountProfile._meta.get_field_by_name('description')[0]
        self.assertEqual(models.CharField, field.__class__)

    def test_description_field_should_has_20_of_max_length(self):
        field = AccountProfile._meta.get_field_by_name('description')[0]
        self.assertEqual(20, field.max_length)

    def test_should_has_type_field(self):
        self.assertIn('type', self.field_names)

    def test_type_field_should_be_char_field(self):
        field = AccountProfile._meta.get_field_by_name('type')[0]
        self.assertEqual(models.CharField, field.__class__)

    def test_type_field_should_has_expected_choices(self):
        field = AccountProfile._meta.get_field_by_name('type')[0]
        self.assertIn(('Student', 'Student'), field.choices)
        self.assertIn(('APyB', 'APyB Associated'), field.choices)
        self.assertIn(('Normal', 'Normal'), field.choices)

    def test_should_has_tshirt_field(self):
        self.assertIn('tshirt', self.field_names)

    def test_tshirt_field_should_be_char_field(self):
        field = AccountProfile._meta.get_field_by_name('tshirt')[0]
        self.assertEqual(models.CharField, field.__class__)

    def test_tshirt_field_should_has_expected_choices(self):
        field = AccountProfile._meta.get_field_by_name('tshirt')[0]
        female_choices = (
            'Female', (
                ('P','P'),
                ('M', 'M'),
                ('G', 'G'),
            )
        )
        male_choices = (
            'Male', (
                ('P','P'),
                ('M', 'M'),
                ('G', 'G'),
                ('GG', 'GG'),
                ('GGX', 'GGX'),
            )
        )

        self.assertIn(female_choices, field.choices)
        self.assertIn(male_choices, field.choices)

    def test_should_has_locale_field(self):
        self.assertIn('locale', self.field_names)

    def test_locale_field_should_be_char_field(self):
        field = AccountProfile._meta.get_field_by_name('locale')[0]
        self.assertEqual(models.CharField, field.__class__)

    def test_locale_field_should_be_optional(self):
        field = AccountProfile._meta.get_field_by_name('locale')[0]
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_should_has_gender_field(self):
        self.assertIn('gender', self.field_names)

    def test_gender_field_should_be_char_field(self):
        field = AccountProfile._meta.get_field_by_name('gender')[0]
        self.assertEqual(models.CharField, field.__class__)

    def test_gender_field_should_has_expected_choices(self):
        field = AccountProfile._meta.get_field_by_name('gender')[0]
        self.assertIn(('female', 'female'), field.choices)
        self.assertIn(('male', 'male'), field.choices)
        self.assertIn(('transsexual', 'transsexual'), field.choices)
        self.assertIn(('other', 'other'), field.choices)

    def test_gender_field_should_be_optional(self):
        field = AccountProfile._meta.get_field_by_name('gender')[0]
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_should_has_age_field(self):
        self.assertIn('age', self.field_names)

    def test_age_field_should_be_char_field(self):
        field = AccountProfile._meta.get_field_by_name('age')[0]
        self.assertEqual(models.CharField, field.__class__)

    def test_age_field_should_has_expected_choices(self):
        field = AccountProfile._meta.get_field_by_name('age')[0]
        self.assertIn(('--9', '--9'), field.choices)
        self.assertIn(('10-19', '10-19'), field.choices)
        self.assertIn(('20-29', '20-29'), field.choices)
        self.assertIn(('30-39', '30-39'), field.choices)
        self.assertIn(('40-49', '40-49'), field.choices)
        self.assertIn(('50-59', '50-59'), field.choices)
        self.assertIn(('60-69', '60-69'), field.choices)
        self.assertIn(('70-79', '70-79'), field.choices)
        self.assertIn(('80-+', '80-+'), field.choices)

    def test_age_field_should_be_optional(self):
        field = AccountProfile._meta.get_field_by_name('age')[0]
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_should_has_profession_field(self):
        self.assertIn('profession', self.field_names)

    def test_profession_field_should_be_char_field(self):
        field = AccountProfile._meta.get_field_by_name('profession')[0]
        self.assertEqual(models.CharField, field.__class__)

    def test_profession_field_should_has_expected_choices(self):
        field = AccountProfile._meta.get_field_by_name('profession')[0]
        self.assertIn(('student', 'student'), field.choices)
        self.assertIn(('trainee', 'trainee'), field.choices)
        self.assertIn(('developer', 'developer'), field.choices)
        self.assertIn(('software engineer', 'software engineer'), field.choices)
        self.assertIn(('manager', 'manager'), field.choices)
        self.assertIn(('sys-admin', 'sys-admin'), field.choices)
        self.assertIn(('teacher', 'teacher'), field.choices)
        self.assertIn(('other', 'other'), field.choices)

    def test_profession_field_should_be_optional(self):
        field = AccountProfile._meta.get_field_by_name('profession')[0]
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_should_has_institution_field(self):
        self.assertIn('institution', self.field_names)

    def test_institution_field_should_be_char_field(self):
        field = AccountProfile._meta.get_field_by_name('institution')[0]
        self.assertEqual(models.CharField, field.__class__)

    def test_institution_field_should_be_optional(self):
        field = AccountProfile._meta.get_field_by_name('institution')[0]
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_institution_field_should_has_verbose_name_company_university_institution(self):
        field = AccountProfile._meta.get_field_by_name('institution')[0]
        self.assertEquals('Company / University / Institution', field.verbose_name)

    def test_should_has_payement_field(self):
        self.assertIn('payement', self.field_names)

    def test_payement_field_should_be_char_field(self):
        field = AccountProfile._meta.get_field_by_name('payement')[0]
        self.assertEqual(models.BooleanField, field.__class__)

    def test_payement_field_should_has_default_False(self):
        field = AccountProfile._meta.get_field_by_name('payement')[0]
        self.assertFalse(field.default)

    def test_have_talk_subscription_should_be_false_when_use_hasnt_a_subscription(self):
        user = User.objects.create(username="tony")
        profile = AccountProfile.objects.create(user=user)
        self.assertFalse(profile.has_talk_subscription())

    def test_have_talk_subscription_shoud_be_true_when_user_has_a_subscription(self):
        user = User.objects.create(username="tony")
        profile = AccountProfile.objects.create(user=user)
        Subscription.objects.create(user=user, type="talk")
        self.assertTrue(profile.has_talk_subscription())

    def test_talk_subscription_shoud_be_returns_the_talk_subscription(self):
        user = User.objects.create(username="tony")
        profile = AccountProfile.objects.create(user=user)
        subscription = Subscription.objects.create(user=user, type="talk")
        self.assertEqual(subscription, profile.talk_subscription())
