import unittest
from app.models import Blog, User


class BlogTest(unittest.TestCase):
    def setUp(self):
        self.user_id = User(username='liz', password='12345', email='nyamburaliz91@gmail.com')
        self.new_blog = Blog(blog_title='Boo Blog',posted_at='10/11/2020', blog_content='Boo blog', user_id=self.user_id.id)


    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.blog_title, 'Boo Blog')
        self.assertEquals(self.new_blog.blog_content, 'Boo blog')
        self.assertEquals(self.new_blog.user_id, self.user_id.id)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(self)
