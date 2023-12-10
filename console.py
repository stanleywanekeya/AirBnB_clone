#!/usr/bin/python3
"""Module defination of console log"""
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models import storage


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Class implementation of console

    Attributes:
        prompt (str): The prompt display
    """
    prompt = "(hbnb) "
    __classes = {
            "BaseModel"
            }

    def do_create(self, arg):
        """Creates an instance of BaseModel"""
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints string representation of class Based on id"""
        args = parse(arg)
        obj = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj:
            print("** no instance found **")
        else:
            print(obj["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes object from storage"""
        args = parse(arg)
        obj = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj.keys():
            print("** no instance found **")
        else:
            del obj["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """print a list of all representation of instances"""
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class name missing **")
        else:
            obj = []
            for objdict in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj.append(objdict.__str__)
                elif len(args) == 0:
                    obj.append(objdict.__str__)
            print(obj)

    def do_update(self, arg):
        args = parse(arg)
        obj = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        if len(args) == 1:
            print("** instance id missing **")
        if "{}.{}".format(args[0], args[1]) not in obj.keys():
            print("** no instance found **")
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) == 4:
            objdict = obj["{}.{}".format(args[0], args[1])]
            if args[2] in objdict.__class__.__name__.keys():
                valtype = type(objdict.__class__.__dict__[args[2]])
                objdict.__dict__[args[2]] = valtype(args[3])
            else:
                objdict.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            objdict = obj["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in objdict.__class__.__dict__.keys() and
                        type(objdict.__class__.__dict__[k])
                        in {str, int, float}):
                    valtype = type(objdict.__class__.__dict__[k])
                    objdict.__dict__[k] = valtype(v)
                else:
                    objdict.__dict__[k] = v
        storage.save()

    def do_EOF(self, arg):
        """EOF - signals exit"""
        return True

    def do_quit(self, arg):
        """quits the program"""
        return True

    def emptyline(self):
        """Enter dooes nothing in program"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
