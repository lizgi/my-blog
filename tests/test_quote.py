import unittest
from app.models import Quote


class TestQuote(unittest.TestCase):
    def setUp(self):
        self.quote = Quote("liz", "To love and to hold")

    def test_instance(self):
        self.assertTrue(isinstance(self.quote, Quote))

    def test_init(self):
        self.assertEqual(self.quote.author, "liz")
        self.assertEqual(self.quote.quote, "To love and to hold")
        
