# import G3nius-Tools
# coding: utf-8

"""     libs        """
# internal
from lib.GPL.Page_Managers import gpl_clear_and_banner, gpl_set_banner_verion
from lib.core.Error_Handler import Handler
from lib.GPL.File_Workers import gpl_ask_save_to_file
from lib.GPL.IO import gpl_input, gpl_confirm, gpl_sleep
# configs
import lib.config.Error_Levels as Error_Levels
# external
from itertools import combinations


"""     process     """
# set verion
gpl_set_banner_verion('2.0.0')

# ask for default
Answers = []
Default_Questions = gpl_confirm('Do you want use default questions', True)
if Default_Questions:
        # questions
        Default_Questions = [
            "Target name(s) / Nikname(s)",
            "Job(s) name",
            "Pet's name'(s) name",
            "Day of month (Target birthday)",
            "Month of year (Target birthday)",
            "Year of birthday",
            "Name(s) of favorite things",
            "Name of city",
            "Name of country",
            "Country cellphone code",
            "Phone number (without Phone number)",
            "Add more words if you want (Or enter empty)"
        ]
        # ask
        for Question in Default_Questions:
            gpl_clear_and_banner()
            Handler(Error_Levels.Info, 'Use ", " (contain space) to enter multi values.', 'Lot of values = Big size and big process.')
            Answer = gpl_input(Question + ' ? ', clear_and_banner_before=False)
            # convert list
            Answer = Answer.split(', ')
            for Word in Answer:
                Answers.append(Word)
else:
    while True:
        # manual ask
        gpl_clear_and_banner()
        Handler(Error_Levels.Info, 'Use CTRL+C to end and get results.')
        Handler(Error_Levels.Info, 'Use ", " (contain space) to enter multi values.', 'Lot of values = Big size and big process.')
        try:
            Answer = input('Enter a value (Name, Job, Food, ...) : ')
            Answer = Answer.split(', ')
            for Word in Answer:
                Answers.append(Word)
            Handler(Error_Levels.Alert, "Words added to list.")
            gpl_sleep()
        except (EOFError, KeyboardInterrupt):
            break

# essential characters
gpl_clear_and_banner()
Characters = [',', '.', '/', '-', '=', '_', '+', '*', '(', ')', '^', '%', '$', '#', '@', '!', '?', '\\', '~', '`']
Handler(Error_Levels.Info, "Essential Characters: " + str(Characters))
Answer = gpl_confirm("Do you want add essential characters to list of words", True, clear_and_banner_before=False)
if Answer:
    Answers += Characters

# ask file address
gpl_clear_and_banner()
File_Address = gpl_ask_save_to_file(just_ask=True)

# generate & write
gpl_clear_and_banner()
Handler(Error_Levels.Info, "Processing on wordlist...", 'Use CTRL+C or CTRL+D to cancell.')
Number = 0
File = open(File_Address, 'w')
while True:
    Number += 1
    # calculate
    States = list(combinations(Answers, Number))
    if len(States) == 0:
        break
    for State in States:
        # join tuple
        Word = ''
        for Item in State:
            Word += Item
        # write result
        File.write("\n" + Word)
File.close()
Handler(Error_Levels.Alert, 'File created, Done.')
gpl_sleep(2)