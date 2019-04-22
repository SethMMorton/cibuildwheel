import glob
import subprocess
import sys

build_identifiers = subprocess.check_output([sys.executable, '-m', 'cibuildwheel', '--print-build-identifiers'], universal_newlines=True).strip().split('\n')
expected_identifiers = build_identifiers
built_wheels = glob.glob('wheelhouse/*.whl')

assert len(built_wheels) == len(expected_identifiers)