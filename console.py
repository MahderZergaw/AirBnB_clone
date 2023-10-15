#!/usr/bin/python3
"""This module consist of a program that
 contains the entry point of the command interpreter"""

import cmd
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class definition HBNBCommand implements:

       Quit and EOF to exit the program.

       help (this action is provided by default
       by cmd but will be updated and
       documented as we work through tasks)
       a custom prompt: (hbnb)

       Empty line + ENTER shouldn’t execute anything

"""
    prompt = "(hbnb) "

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

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id
        """
        if args == "" or args is None:
            print("* class name missing *")
        elif args not in storage.classes():
            print("** class doesn't exist")
        else:
            model = storage.classes()[args]()
            model.save()
            print(model.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if args == "" or args is None:
            print("* class name missing *")
        else:
            args_list = args.split(' ')
            if args_list[0] not in storage.classes():
                print("* class doesn't exist *")
            elif len(args_list) < 2:
                print("* instance id missing *")
            else:
                key = "{}.{}".format(args_list[0], args_list[1])
                if key not in storage.all():
                    print("* no instance found *")
                else:
                    print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if args == "" or args is None:
            print("* class name missing *")
        else:
            args_list = args.split(' ')
            if args_list[0] not in storage.classes():
                print("* class doesn't exist *")
            elif len(args_list) < 2:
                print("* instance id missing *")
            else:
                obj_id = "{}.{}".format(args_list[0], args_list[1])
                if obj_id not in storage.all():
                    print("* no instance found *")
                else:
                    del storage.all()[obj_id]
                    storage.save()

    def do_all(self, args):
        """Prints all string representation of
           all instances based or not on the class name
        """
        if args != "":
            args_list = args.split(' ')
            if args_list[0] not in storage.classes():
                print("* class doesn't exist *")
            else:
                str_rep = [str(value) for key,
                           value in storage.all().items()
                           if obj.__class__.__name__ == args[0]]
                print(str_rep)
        else:
            crtd_list = [str(value) for key, value
                         in storage.all().items()]
            print(crtd_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        if not args:
            print("* class name missing *")
            return
        args_list = args.split()
        if args_list[0] != "BaseModel":
            print("* class doesn't exist *")
            return
        if len(args_list) < 2 or self.id is None:
            print("* instance id missing *")
            return
        if len(args_list) < 3:
            print("* attribute name missing *")
            return
        if len(args_list) < 4:
            print("* value mising *")
            return

        class_name = args_list[0]
        instance_id = args_list[1]
        attribute_name = args_list[2]
        attribute_value = args_list[3].strip('"')
        all_objs = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key not in all_objs:
            print("* no instance found *")
        else:
            obj = all_objs[key]
            setattr(obj, attribute_name, attribute_value)
            obj.save()


if _name_ == "__main__":
    HBNBCommand().cmdloop()
