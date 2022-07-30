import argparse

from .process_tools import privileged, unprivileged


PROCESS     = 'process'
COUNT       = 'count'
STOP_ALL    = 'stop_all'
ARGS        = 'args'
SIGNAL      = 'signal'
REGULAR     = 'regular' # TODO


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(PROCESS, type=str)
    parser.add_argument('--' + ARGS, type=str, help='arg in \'\'', default='')
    parser.add_argument('--' + COUNT, action='store_true', help='print count of replicas')
    parser.add_argument('--' + STOP_ALL, action='store_true', help='stop all replicas')
    parser.add_argument('--' + SIGNAL, type=int, help='signal to processes', default=15)
    args = parser.parse_args().__dict__
    print(args)
    if args[COUNT]:
        cnt = unprivileged.count(args[PROCESS], args[ARGS])
        print(cnt)
    elif args[STOP_ALL]:
        unprivileged.check_root()
        closed_count = privileged.stop_all(args[PROCESS], args[ARGS], args[SIGNAL])
        print(closed_count)
    else:
        unprivileged.start([args[PROCESS], args[ARGS]])