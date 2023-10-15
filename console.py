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
            instance_id = arg_parts[2]
            attribute = arg_parts[3]
            if command == "show":
                return self.do_show(f"{class_name} {instance_id}")
            elif command == "destroy":
                return self.do_destroy(f"{class_name} {instance_id}")
            elif command == "update" and len(arg_parts) >= 5:
                value = arg_parts[4]
                return self.do_update(f"{class_name} {instance_id} {attribute} {value}")
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        print("")
        return True

    def do_create(self, arg):
        """Create a new instance of a class and print its ID"""
        arg_parts = parse(arg)
        if len(arg_parts) == 0:
            print("** class name missing **")
        elif arg_parts[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[arg_parts[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance"""
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
            all_objs = storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

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
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Display string representations of instances"""
        arg_parts = parse(arg)
        if len(arg_parts) == 0:
            all_objs = storage.all()
            print([str(obj) for obj in all_objs.values()])
        elif arg_parts[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            obj_list = [str(obj) for obj in all_objs.values() if obj.__class__.__name__ == arg_parts[0]]
            print(obj_list)

    def do_count(self, arg):
        """Count instances of a class"""
        arg_parts = parse(arg)
        if len(arg_parts) == 0:
            print("** class name missing **")
        elif arg_parts[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            count = sum(1 for obj in all_objs.values() if obj.__class__.__name__ == arg_parts[0])
            print(count)

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
            all_objs = storage.all()
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
