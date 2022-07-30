from concurrent.futures import process
import os
import re
import subprocess
from typing import Iterable
import psutil


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
        if args == ' '.join(proc.cmdline()):
            pids.append(proc.pid)
    return pids


def get_pids_by_name(process_name:str) -> list[int]:
    pids = list[int]()
    for proc in psutil.process_iter():
        if process_name == proc.name():
            pids.append(proc.pid)
    return pids


def get_processes_by_regular(pattern:str) -> list[str]:
    processes = list[str]()
    for proc in psutil.process_iter():
        match = re.search(pattern, ' '.join(proc.cmdline()))
        if match is not None:
            processes.append(match.string)
    return processes

def start(args:Iterable[str]):
    arguments = ' '.join(args).split()
    subprocess.Popen(arguments, close_fds=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)