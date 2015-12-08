import re
from unittest import TestCase

from app import create_app


class TestApp(TestCase):

    def setUp(self):
        app = create_app()
        app.config['TESTING'] = True
        self.app = app.test_client()

    def testBlueprintFilter(self):
        """
        Test that the date filter defined in the core
        blueprint gets applied in the blog template
        """
        res = self.app.get('/blog/latest')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}$", res.data))
