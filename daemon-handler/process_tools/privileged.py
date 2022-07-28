import os

from .unprivileged import get_pids


def stop_all(process_name:str, args:str = '', signal:int = 15) -> int:
    pids = get_pids(process_name, args)
    for pid in pids:
        stop(pid, signal)
    return len(pids)


def stop(pid:int, signal:int = 15):
    os.kill(pid, signal)