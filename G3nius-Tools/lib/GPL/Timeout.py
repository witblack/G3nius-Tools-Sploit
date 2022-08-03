"""     libs     """
from signal import SIGALRM, SIG_IGN ,signal, alarm
from contextlib import contextmanager


"""     gpl     """
# Timeout
#
# external modules:
# signal
# contextlib
#
# version:
# 1
@contextmanager
def gpl_timeout(Sec=1):
    signal(SIGALRM, raise_timeout)
    alarm(Sec)
    try:
        yield
    except TimeoutError:
        pass
    finally:
        signal(SIGALRM, SIG_IGN)


# Raise_Timeout
#
# version:
# 1
def raise_timeout(Signum, Frame):
    raise TimeoutError