# they're all bash exit codes
Normal = 0
Crash = 1
MissSourceCode = 2 # empty_function() {}
CanNotExecute = 126 # /dev/null
CommandNotFound = 127 # not_found_abcd_command
InvalidArgument = 128 # exit 3.12
CTRL_C = 130 # CTRL + C
OutOfRange = 255 # exit -1