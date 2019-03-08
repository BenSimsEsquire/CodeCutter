import paths
import os
import subprocess

def extract_function(file, func):
	subprocess.Popen("ctags", set_env())

def set_env():
	return {**os.environ, 'PATH': 'CTAGS'}

	

	
