from unittest import mock
import unittest
from HW04_Weijie_Pan import read_github_repo, read_github_commit


class GithubParserTest(unittest.TestCase):

    @mock.patch('requests.get')
    def test_repo(self, mock_req):
        content = [{'id': '001', 'name':'hello world'}, {'id': '002', 'name':'python'}]
        mock_req.return_value = mock.Mock()
        mock_req.return_value.json.return_value = content
        response = read_github_repo("hi")
        self.assertEqual(response, content)

    @mock.patch('requests.get')
    def test_commit(self, mock_res):
        content = [{'id': '001', 'name': 'hello world'}, {'id': '002', 'name': 'python'}]
        mock_res.return_value = mock.Mock()
        mock_res.return_value.json.return_value = content
        response = read_github_commit("hi")
        self.assertEqual(response, {'hello world': 2, 'python': 2})


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
