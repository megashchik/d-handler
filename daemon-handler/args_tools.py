import sys
from typing import Tuple

from process_tools import privileged, unprivileged


COUNT       = '--count'
HELP        = '--help'
NAME        = '--name' 
START       = '--start'
STOP_ALL    = '--stop-all'
ARGS        = '--args'
SIGNAL      = '--signal'
REGULAR     = '--regular'


def _print_help():
    print(f'{HELP}         print help')
    print(f'{START}        start one worker')
    print(f'{ARGS}         arg in \'\'')
    print(f'{COUNT}        count of running workers')
    print(f'{STOP_ALL}     stop all workers, needed root')
    print(f'{SIGNAL}       signal to process')
    # print(f'{REGULAR}      regular expression (not implemented)')


def _get_name_and_arguments() -> Tuple[str, str]:
    name = ''
    arguments = ''
    for arg in sys.argv:
        if arg.startswith(f'{NAME}='):
            name = arg.split('=')[-1]
            continue
        if arg.startswith(f'{ARGS}='):
            arguments = arg.split('=')[-1]
    
    if arguments == '':
        arguments = _get_base_arg()

    if name == '':
        name = arguments.split(' ')[0].split('/')[-1]

    return name, arguments


def _parse_process_arg(arg_name:str) -> str:
    for arg in sys.argv:
        if arg.startswith(f'{arg_name}='):
            return arg.split('=')[-1]
    return ''


def _get_base_arg() -> str:
    for arg in sys.argv[1:]:
        if not arg.startswith('-'):
            return arg


def parse_args():
    if sys.argv.__contains__(HELP):
            _print_help()
    elif sys.argv.__contains__(COUNT):
        name , arguments = _get_name_and_arguments()
        cnt = unprivileged.count(name, arguments)
        print(f'count:  {cnt}')
    elif sys.argv.__contains__(STOP_ALL):
        unprivileged.check_root()
        name, arguments = _get_name_and_arguments()
        signal = _parse_process_arg(SIGNAL)
        # TODO fix it
        if signal != '':
            signal = int(signal)
        else:
            signal = 15
        cnt = privileged.stop_all(name, arguments, signal)
        print(f'closed: {cnt}')
    else:
        # START
        name, arguments = _get_name_and_arguments()
        print(arguments)
        unprivileged.start(arguments)