#!/usr/bin/python3
"""This module consist of a program that
 contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """class definition HBNBCommand implements:

       Quit and EOF to exit the program.

       help (this action is provided by default
       by cmd but will be updated and
       documented as we work through tasks)
       a custom prompt: (hbnb)

       Empty line + ENTER shouldn’t execute anything

"""

    prompt = "(hbnb)"

    def do_quit(self, args):
        """Implements quit to exit"""
        return True

    def do_EOF(self, args):
        """Implements the end of file program"""
        return True

    def help_quit(self):
        """"""
        print("{}".format("Quit command to exit to exit the program"))

    def emptyline(self):
        """does nothing"""
        pass


if _name_ == "__main__":
    HBNBCommand().cmdloop()
