import unittest
from app.models import Comment

class CommentTest(unittest.TestCase):

    def setUp(self):
       
        self.new_comment = Comment(comment="all comments")

    def test_init(self):
        self.assertEqual(self.new_comment.comment, "all comments")

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)
        
