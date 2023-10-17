#!/usr/bin/python3
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

def parse(arg):
    """Parse a string of arguments and return a list of tokens"""
    tokens = []
    while arg:
        match = re.search(r'(\{.*?\}|\[.*?\])', arg)
        if match:
            start, end = match.span()
            tokens.extend(arg[:start].split())
            tokens.append(arg[start:end])
            arg = arg[end:]
        else:
            tokens.extend(arg.split())
            break
    return tokens

class HBNBCommand(cmd.Cmd):
    """HBNBCommand command interpreter"""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def default(self, arg):
        """Handle unknown commands"""
        arg_parts = parse(arg)
        if len(arg_parts) >= 2 and arg_parts[0] in self.classes:
            class_name = arg_parts[0]
            command = arg_parts[1]
            if command == "all":
                return self.do_all(class_name)
            elif command == "count":
                return self.do_count(class_name)
            elif command == "show" and len(arg_parts) >= 3:
                instance_id = arg_parts[2]
                return self.do_show(f"{class_name} {instance_id}")
            elif command == "destroy" and len(arg_parts) >= 3:
                instance_id = arg_parts[2]
                return self.do_destroy(f"{class_name} {instance_id}")
            elif command == "update" and len(arg_parts) >= 6:
                instance_id = arg_parts[2]
                attribute = arg_parts[3]
                value = arg_parts[4]
                return self.do_update(f"{class_name} {instance_id} {attribute} {value}")
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_all(self, arg):
        """Display string representations of instances"""
        arg_parts = parse(arg)
        if len(arg_parts) == 1 and arg_parts[0] in self.classes:
            class_name = arg_parts[0]
            all_objs = self.storage.all()
            obj_list = [str(obj) for obj in all_objs.values() if obj.__class__.__name__ == class_name]
            print(obj_list)
        else:
            print("*** Unknown syntax: all")

    def do_count(self, arg):
        """Count instances of a class"""
        arg_parts = parse(arg)
        if len(arg_parts) == 1 and arg_parts[0] in self.classes:
            class_name = arg_parts[0]
            all_objs = self.storage.all()
            count = sum(1 for obj in all_objs.values() if obj.__class__.__name__ == class_name)
            print(count)
        else:
            print("*** Unknown syntax: count")

    def do_show(self, arg):
        """Show the string representation of an instance"""
        arg_parts = parse(arg)
        if len(arg_parts) == 2 and arg_parts[0] in self.classes:
            class_name, obj_id = arg_parts
            key = f"{class_name}.{obj_id}"
            all_objs = self.storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
        else:
            print("*** Unknown syntax: show")


    def do_destroy(self, arg):
        """Delete an instance by class name and ID"""
        arg_parts = parse(arg)
        if len(arg_parts) == 0:
            print("** class name missing **")
        elif arg_parts[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg_parts) < 2:
            print("** instance id missing **")
        else:
            obj_id = arg_parts[1]
            key = f"{arg_parts[0]}.{obj_id}"
            all_objs = self.storage.all()
            if key in all_objs:
                del all_objs[key]
                self.storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """Update an instance's attributes"""
        arg_parts = parse(arg)
        if len(arg_parts) == 0:
            print("** class name missing **")
        elif arg_parts[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg_parts) < 2:
            print("** instance id missing **")
        else:
            obj_id = arg_parts[1]
            key = f"{arg_parts[0]}.{obj_id}"
            all_objs = self.storage.all()
            if key in all_objs:
                obj = all_objs[key]
                if len(arg_parts) < 3:
                    print("** attribute name missing **")
                elif len(arg_parts) < 4:
                    print("** value missing **")
                else:
                    attr_name = arg_parts[2]
                    attr_value = arg_parts[3]
                    setattr(obj, attr_name, attr_value)
                    obj.save()
            else:
                print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
