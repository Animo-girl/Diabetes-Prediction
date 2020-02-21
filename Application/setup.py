'''
import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit'
    }
}

executables = [
    Executable('main.py', base=base)
]

setup(name="D's",
      version='0.1',
      description='Application for Daibetic patients',
      options=options,
      executables=executables
      )
'''
from cx_Freeze import setup,Executable
import sys

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'


build_exe_options = {
"packages":['numpy','pandas','sklearn','xlrd'],
"include_files":["Model File.sav","Model File Treatment.sav"]
}
setup(
	name = "D's",
	version = "1.0",
	description = "For diabetic patients",
	options = {"build_exe":build_exe_options},
	executables = [
					Executable('main.py',base = base,shortcutName="D's",
            shortcutDir="DesktopFolder" )
				]
	)
	
	
