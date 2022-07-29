import os
import subprocess
import psutil


def start(args:str):
    arguments = args.split(' ')
    subprocess.Popen(arguments, close_fds=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)


def count(process_name:str, args:str = '') -> int:
    return len(get_pids(process_name, args))


def get_pids(process_name:str, args:str = '') -> list[int]:
    pids = []
    for proc in psutil.process_iter():
        if process_name == proc.name():
            if args == '' or args == ' '.join(proc.cmdline()):
                pids.append(proc.pid)
    return pids


def get_args(pid:int) -> list[str]:
    for proc in psutil.process_iter():
        if proc.pid == pid:
            return proc.cmdline()


def check_root():
    if os.geteuid() != 0:
        exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")