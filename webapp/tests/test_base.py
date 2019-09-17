import sys
import os
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../')
)

import unittest

from webapp.run import app


class BaseTest(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False

        self.app = app.test_client()
        self.assertFalse(app.debug)

        response = self.check_echo()
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, 'Hello, World!')

    # executed after each test
    def tearDown(self):
        pass

    ########################
    #### helper methods ####
    ########################

    def check_echo(self):
        return self.app.get('/api/v1/app/echo')

    def test_echo(self):
        response = self.check_echo()
        self.assertEqual(response.status_code, 200)

    def test_multiply(self):
        self.assertEqual((2 * 3), 6)


if __name__ == "__main__":
    unittest.main()