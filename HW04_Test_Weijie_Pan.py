import unittest
from HW04_Weijie_Pan import read_github_repo


class GithubParserTest(unittest.TestCase):
    """test if id: richkempinski exists"""
    def test_github_parser(self):
        result = {'hellogitworld': 30, 'helloworld': 6, 'Mocks': 10, 'Project1': 2, 'threads-of-life': 1}
        self.assertEqual(read_github_repo('richkempinski'), result)

    def test_github_parser2(self):
        """test if id: bondi exists"""
        self.assertEqual(read_github_repo('bondi'), {'bpi-print': 8, 'liquibase-demo': 9, 'server-configs-nginx': 30})


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

