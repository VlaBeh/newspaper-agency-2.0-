from django.test import TestCase

from catalog.forms import RedactorCreationForm


class FormsTestCase(TestCase):
    def test_redactor_creation_form(self):
        form_data = {
            "username": "new_user",
            "first_name": "new_first",
            "last_name": "new_last",
            "years_of_experience": 2,
            "email": "email@mail.net",
            "password1": "pass23word",
            "password2": "pass23word",
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
