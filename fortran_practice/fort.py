import subprocess
import sys
import os
file_name = sys.argv[1]
cmd = "gfortran "+file_name+" -o ___.exe"
subprocess.call(cmd)
out = subprocess.check_output("___.exe").decode("utf-8")
os.remove("___.exe")
print(out)