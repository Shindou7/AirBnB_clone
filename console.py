#!/usr/bin/python3
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
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
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def default(self, arg):
        """Handle unknown commands"""
        arg_parts = parse(arg)
        if len(arg_parts) >= 4 and arg_parts[0] in self.classes:
            class_name = arg_parts[0]
            command = arg_parts[1]
            if command == "all":
                return self.do_all(class_name)
            instance_id = arg_parts[2]
            if command == "show":
                return self.do_show(f"{class_name} {instance_id}")
            if command == "destroy":
                return self.do_destroy(f"{class_name} {instance_id}")
            if command == "update":
                if len(arg_parts) == 4:
                    attribute = arg_parts[2]
                    value = arg_parts[3]
                    return self.do_update(f"{class_name} {instance_id} {attribute} {value}")
                elif len(arg_parts) == 5 and arg_parts[3] == "{":
                    # Handle update with dictionary
                    attr_dict = eval(" ".join(arg_parts[3:]))
                    return self.do_update(f"{class_name} {instance_id} {attr_dict}")
        print("*** Unknown syntax: {}".format(arg))
        return False

    # Other methods remain the same

    def do_all(self, class_name):
        """Display string representations of instances or all instances of a class"""
        all_objs = storage.all()
        if class_name in self.classes:
            obj_list = [str(obj) for obj in all_objs.values() if obj.__class__.__name__ == class_name]
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_count(self, class_name):
        """Count instances of a class"""
        if class_name in self.classes:
            all_objs = storage.all()
            count = sum(1 for obj in all_objs.values() if obj.__class__.__name__ == class_name)
            print(count)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance"""
        arg_parts = parse(arg)
        if len(arg_parts) < 2:
            print("** instance id missing **")
        elif arg_parts[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            obj_id = arg_parts[1]
            key = f"{arg_parts[0]}.{obj_id}"
            all_objs = storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance by class name and ID"""
        arg_parts = parse(arg)
        if len(arg_parts) < 2:
            print("** instance id missing **")
        elif arg_parts[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            obj_id = arg_parts[1]
            key = f"{arg_parts[0]}.{obj_id}"
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """Update an instance's attributes or attributes using a dictionary"""
        arg_parts = parse(arg)
        if len(arg_parts) < 2:
            print("** instance id missing **")
        elif arg_parts[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            obj_id = arg_parts[1]
            key = f"{arg_parts[0]}.{obj_id}"
            all_objs = storage.all()
            if key in all_objs:
                obj = all_objs[key]
                if len(arg_parts) < 3:
                    print("** attribute name missing **")
                elif len(arg_parts) < 4:
                    print("** value missing **")
                elif len(arg_parts) == 4:
                    attr_name = arg_parts[2]
                    attr_value = arg_parts[3]
                    setattr(obj, attr_name, attr_value)
                    obj.save()
                elif len(arg_parts) == 5 and isinstance(arg_parts[4], dict):
                    attr_dict = eval(arg_parts[4])
                    if isinstance(attr_dict, dict):
                        for key, value in attr_dict.items():
                            setattr(obj, key, value)
                        obj.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
