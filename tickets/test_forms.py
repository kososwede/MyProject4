from django.test import TestCase
from .forms import FormForTickets, DonationFormForTickets, CommentFormForTickets


class TestTheTicketForm(TestCase):
    def testing_user_can_create_ticket(self):
        '''test that user can create a ticket with a title and description'''
        form = FormForTickets({
            "title": "Test Title",
            "description": "Test description"
        })
        self.assertTrue(form.is_valid())

    def testing_empty_field_message(self):
        '''Test that the appropriate fields are required for it to be valid'''
        form = FormForTickets({"title": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["title"],
                         [u"This field is required."])


class TestTheDonationForm(TestCase):
    def testing_user_can_donate(self):
        '''Tests that the user can donate by selecting a shown donation amount'''
        form = DonationFormForTickets({"donation_amount": 10})
        self.assertTrue(form.is_valid())


class TestCommentForm(TestCase):
    def testing_user_can_create_a_comment_over_five_characters(self):
        '''Tests that the user can fill in comment form and must be over 5 characters'''
        form = CommentFormForTickets({"description": "Tests"})
        self.assertTrue(form.is_valid())

    def testing_user_cannot_create_comment_under_five_characters(self):
        '''Tests that user cannot create form if less than 5 characters'''
        form = CommentFormForTickets({"description": "Test"})
        self.assertFalse(form.is_valid())

    def testing_empty_field_error_message(self):
        '''Tests that the appropriate fields are required '''
        form = CommentFormForTickets({"description": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["description"],
                         [u"This field is required."])
