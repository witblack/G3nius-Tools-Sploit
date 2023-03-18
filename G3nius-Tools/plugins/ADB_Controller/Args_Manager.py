"""     lib     """
from lib.classes.gpl import Error_Levels, Handler


"""     process     """
def Manage_args(arg: str, can_be:list[str:str]):
    if arg in can_be:
        return arg
    else:
        Handler(Error_Levels.Minus, f"Invalid input, Just can be once {can_be}")
        return False



def Join_args(args):
    Value = ' '.join(args)
    if Value.replace(' ', '') == '':
        raise IndexError('Invalid arguments.')
    else:
        return Value
