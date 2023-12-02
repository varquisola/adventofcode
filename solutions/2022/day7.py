# Creating a tree

class Node:
    def __init__(self, parent=None, children=[], name="", size=0, type="dir"):
        self.parent = parent
        self.children = children
        self.size = size
        self.name = name
        self.type = type

    def print_tree(self, level=0):
        print('\t' * level + repr(self.name) + ' ' + repr(self.size))
        for child in self.children:
            child.print_tree(level + 1)


def create_file_tree(cmds):
    root = Node(name="root", parent=None, children=[], size=0, type="dir")
    home = root
    curr_parent = root

    for cmd in cmds:
        cmd_split = cmd.split()
        if len(cmd_split) == 3:
            # We must have a cd command
            # Move to node
            if cmd_split[2] == '..':
                # Move a level up (go to parent)
                curr_node = curr_node.parent
                curr_parent = curr_node.parent
            else:
                # Move to node at [2]
                for child in curr_parent.children:
                    if child.name == cmd_split[2]:
                        curr_node = child
                        curr_parent = curr_node
        else:
            if cmd_split[0] == 'dir':
                curr_node = Node(name=cmd_split[1], size=0, parent=curr_parent, children=[], type="dir")
                curr_parent.children.append(curr_node)
            elif cmd_split[0].isnumeric():
                curr_node = Node(name=cmd_split[1], size=int(cmd_split[0]), parent=curr_parent, children=[], type="file")
                curr_parent.children.append(curr_node)

                # Bubble the size up the directories
                something = curr_parent
                while something is not None:
                    something.size += curr_node.size
                    something = something.parent

                # print(curr_node.name, curr_node.size, curr_parent.name, curr_parent.size)
            elif cmd_split[0] == 'cd' and cmd_split[1] == 'ls':
                continue
    return home


def find_dirs_with_greater_than_100000(root, tree_sum):
    if root:
        print(root.name, root.size)
        if root.size < 100000 and root.type == "dir":
            # print(root.name, root.size)
            tree_sum += root.size

        for child in root.children:
            tree_sum = find_dirs_with_greater_than_100000(child, tree_sum)

    return tree_sum


def calculate_smallest_dir_remove(root, unused_space, curr_dir_size, curr_dir_name):
    if root:
        if unused_space < root.size < curr_dir_size and root.type == "dir":
            curr_dir_size = root.size
            curr_dir_name = root.name

        for child in root.children:
            curr_dir_size, curr_dir_name = calculate_smallest_dir_remove(child, unused_space, curr_dir_size, curr_dir_name)

    return curr_dir_size, curr_dir_name


def sum_of_all_files(cmds):
    sum = 0
    for cmd in cmds:
        cmd_split = cmd.split()
        if cmd_split[0].isnumeric():
            sum = sum + int(cmd_split[0])
    return sum
