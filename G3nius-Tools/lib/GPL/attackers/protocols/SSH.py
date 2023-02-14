"""     libs    """
# internal
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, SSHException

# external
from socket import socket

# configs
from lib.config.GPL import SSH_Timeout, Encoding


"""     GPL     """
# connect to SSH server
#
# internal:
# from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, SSHException
#
# note:
# 1. if get error, be quota over
# 2. return SSH controller if connected
# 3. your login won't be logged at server
#
# version
# 1
def gpl_connect_to_ssh(IP, username, password, port=22, timeout=SSH_Timeout):
    # initialize SSH client
    Client = SSHClient()
    Socket = socket()
    # add to know hosts
    Client.set_missing_host_key_policy(AutoAddPolicy())
    # try to connect
    if Socket.connect_ex((IP, port)) != 0:
        raise SSHException('Quota over or closed port, Retry later...')
    try:
        Client.connect(hostname=IP, port=port, username=username, password=password, timeout=SSH_Timeout)
    except AuthenticationException:
        return False
    except SSHException:
        raise SSHException('Quota exceeded, Retry later...')
    except:
        return None
    else:
        return Client

# run ssh commands on SSH_controller
#
# version
# 1
def gpl_run_command_on_SSH(SSH_controller, command, encoding=Encoding):
    try:
        Stdin, Stdout, Stderr = SSH_controller.exec_command(command)
        result = {
            'ExitCode': Stdout.channel.recv_exit_status(),
            'Stdout': Stdout.read().decode(encoding),
            'Stderr': Stderr.read()
        }
        return result
    except:
        return False

# Close SSH connection
#
# version
# 1
def gpl_disconnect_SSH(SSH_controller):
    try:
        SSH_controller.close()
    except:
        return False
    else:
        return True
