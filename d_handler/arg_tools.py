import argparse

from .process_tools import privileged, unprivileged


PROCESS     = 'process'
COUNT       = 'count'
STOP_ALL    = 'stop_all'
ARGS        = 'args'
SIGNAL      = 'signal'
REGULAR     = 'regular'


def _get_args(process:str, args:str):
    return ' '.join([process, args]).strip()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(PROCESS, type=str)
    parser.add_argument('-a', '--' + ARGS, type=str, help='arg in \'\'', default='')
    parser.add_argument('-c', '--' + COUNT, action='store_true', help='print count of replicas')
    parser.add_argument('-k', '--' + STOP_ALL, action='store_true', help='stop all replicas')
    parser.add_argument('-s', '--' + SIGNAL, type=int, help='signal to processes', default=15)
    parser.add_argument('-r', '--' + REGULAR, action='store_true', help='process is regular pattern')
    args = parser.parse_args().__dict__
    if args[COUNT]:
        cnt = 0
        if args[REGULAR]:
            cnt = len(unprivileged.get_pids_by_regular(args[PROCESS]))
        else:
            cnt = unprivileged.count(_get_args(args[PROCESS], args[ARGS]))
        print(cnt)
    elif args[STOP_ALL]:
        unprivileged.check_root()
        closed_count = 0
        if args[REGULAR]:
            closed_count = privileged.stop_by_regular(args[PROCESS], args[SIGNAL])
        else:
            closed_count = privileged.stop_all(_get_args(args[PROCESS], args[ARGS]), args[SIGNAL])
        print(closed_count)
    else:
        unprivileged.start([args[PROCESS], args[ARGS]])