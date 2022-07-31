import os
import re
import subprocess
import psutil
from typing import Iterable


def check_root():
    if os.geteuid() != 0:
        exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")


def count(args:str = '') -> int:
    return len(get_pids_by_args(args))


def get_args(pid:int) -> list[str]:
    for proc in psutil.process_iter():
        if proc.pid == pid:
            return proc.cmdline()


def get_pids_by_args(args:str) -> list[int]:
    pids = list[int]()
    for proc in psutil.process_iter():
        print(proc.cmdline(), proc.pid)
        if args == ' '.join(proc.cmdline()):
            pids.append(proc.pid)
    return pids


def get_pids_by_name(process_name:str) -> list[int]:
    pids = list[int]()
    for proc in psutil.process_iter():
        if process_name == proc.name():
            pids.append(proc.pid)
    return pids


def get_pids_by_regular(pattern:str) -> list[str]:
    pids = list[int]()
    # list of pids from current procees
    self_pids = [p.pid for p in psutil.Process(os.getpid()).parents()]
    self_pids.append(os.getpid())
    for proc in psutil.process_iter():
        match = re.search(pattern, ' '.join(proc.cmdline()))
        if match is not None and not self_pids.__contains__(proc.pid):
            pids.append(proc.pid)
    return pids

def start(args:Iterable[str]):
    arguments = ' '.join(args).split()
    subprocess.Popen(arguments, close_fds=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)