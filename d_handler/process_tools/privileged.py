import os
import psutil

from .unprivileged import get_pids_by_args, get_pids_by_regular


def stop_all(args:str, signal:int = 15) -> int:
    pids = get_pids_by_args(args)
    for pid in pids:
        stop(pid, signal)
    return len(pids)


def stop_by_regular(pattern:str, signal:int = 15) -> int:
    pids = get_pids_by_regular(pattern)
    for pid in pids:
        stop(pid, signal)
    return len(pids)


def stop(pid:int, signal:int = 15):
    # os.system(f'sudo kill -{signal} {pid}')
    try:
        os.kill(pid, signal)
    except Exception as e:
        print('error', e , psutil.Process(pid), 'cant killed')