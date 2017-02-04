import os,sys
#sys.path.append(os.path.abspath('..\\..'))
from test_package.settings.settings import *

def prnt_result():
	print("[+] result : xxx")
	print(__name__)
	print(age)

if __name__ == "__main__":
	prnt_result()
	
