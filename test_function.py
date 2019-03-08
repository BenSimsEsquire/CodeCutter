import unittest
import paths
import extract_function
import os
from unittest.mock import patch

class TestStringMethods(unittest.TestCase):

	def test_path_append(self):
		self.assertEqual(extract_function.set_env(), {**os.environ, 'PATH': 'CTAGS'})

	@patch('subprocess.Popen')
	def test_ctags(self, mock_subproc_popen):
		process_mock = unittest.mock.Mock()
		attrs = {'communicate.return_value': ('output', 'error')}
		process_mock.configure_mock(**attrs)
		mock_subproc_popen.return_value = process_mock 
		extract_function.extract_function("blah", "blah")
		mock_subproc_popen.assert_called_with("ctags")
		
	@patch('subprocess.Popen')
	def test_run_script(self, mock_subproc_popen):
		process_mock = unittest.mock.Mock()
		attrs = {'communicate.return_value': ('output', 'error')}
		process_mock.configure_mock(**attrs)
		mock_subproc_popen.return_value = process_mock 
		extract_function.extract_function("blah", "blah")
		self.assertTrue(mock_subproc_popen.called)


if __name__ == '__main__':
    unittest.main()
