import os

from .unprivileged import get_pids_by_args


def stop_all(args:str, signal:int = 15) -> int:
    pids = get_pids_by_args(args)
    for pid in pids:
        stop(pid, signal)
    return len(pids)


def stop(pid:int, signal:int = 15):
    os.kill(pid, signal)