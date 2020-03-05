from django.test import TestCase
from .forms import TicketForm, DonationForm, CommentForm


class TestTicketForm(TestCase):
    def test_user_can_create_ticket(self):
        '''test that user can create a ticket with a title and description'''
        form = TicketForm({
            "title": "Test Ticket Title",
            "description": "Test ticket description"
        })
        self.assertTrue(form.is_valid())

    def test_blank_field_error_message(self):
        '''Test that the appropriate fields are required for it to be valid'''
        form = TicketForm({"title": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["title"],
                         [u"This field is required."])


class TestDonationForm(TestCase):
    def test_user_can_donate(self):
        '''Tests that the user can donate by selecting a donation ammount'''
        form = DonationForm({"donation_amount": 5})
        self.assertTrue(form.is_valid())


class TestCommentForm(TestCase):
    def test_user_can_create_comment_over_five_characters(self):
        '''Tests user can fill in comment form and must be over 5 characters'''
        form = CommentForm({"description": "Test comment"})
        self.assertTrue(form.is_valid())

    def test_user_cannot_create_comment_under_five_characters(self):
        '''Tests that user cannot create form if less than 5 characters'''
        form = CommentForm({"description": "Test"})
        self.assertFalse(form.is_valid())

    def test_blank_field_error_message(self):
        '''Tests that the appropriate fields are required '''
        form = CommentForm({"description": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["description"],
                         [u"This field is required."])