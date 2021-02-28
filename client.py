from websocket import create_connection



ws = create_connection("ws://{}:{}".format("127.0.0.1", 9001)) 
import subprocess
import sys


def run_shell(shell):
    cmd = subprocess.Popen(shell, stdin=subprocess.PIPE, stderr=sys.stderr, close_fds=True,
                           stdout=sys.stdout, universal_newlines=True, shell=True, bufsize=1)

    cmd.communicate()
    return cmd.returncode

p = subprocess.Popen("ping baidu.com",
                     shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
returncode = p.poll()
while returncode is None:
    line = p.stdout.readline()
    returncode = p.poll()
    line = line.strip()
    ws.send(line)
