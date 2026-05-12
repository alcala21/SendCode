import os
from ..applescript import osascript

_SEND = os.path.join(os.path.dirname(__file__), "cmux_send.applescript")
_SEND_BRACKETED = os.path.join(os.path.dirname(__file__), "cmux_send_bracketed.applescript")


def send_to_cmux(cmd, cmux=None, bracketed=False, commit=True):
    if bracketed:
        osascript(_SEND_BRACKETED, cmd, str(commit))
    else:
        osascript(_SEND, cmd, str(commit))
