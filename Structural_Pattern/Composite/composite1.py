# File System (Files & Folders)

from abc import ABC, abstractmethod

# Step 1: Component Interface (Common Interface for Files & Folders)
class FileSystemComponent(ABC):
    """Abstract class for both files and folders."""
    @abstractmethod
    def show_details(self, indent=0):
        """Displays the details of the component."""
        pass

# Step 2: Leaf Component (File)
class File(FileSystemComponent):
    """Concrete class representing a file."""
    def __init__(self, name, size):
        self.name = name
        self.size = size   # Size in KB
    
    def show_details(self, indent=0):
        print(" " * indent + f"📄 File: {self.name} ({self.size}KB)")

class Folder(FileSystemComponent):
    """Concrete class representing a folder, which can contain files or subfolders."""
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add(self, component):
        """Adds a file or folder to this folder."""
        self.children.append(component)
    
    def remove(self, component):
        """Rmove a file or folder to this folder."""
        self.children.remove(component)
    
    def show_details(self, indent=0):
        print(" " * indent + f"📁 Folder: {self.name}")
        for child in self.children:
            child.show_details(indent+2)

# creating root folder
root = Folder("Root")

# create files
file1 = File("resume.pdf", 200)
file2 = File("photo.png", 500)

sub_folder = Folder("Documents")
file3 = File("notes.txt", 50)

# Building structure
sub_folder.add(file3)
root.add(file1)
root.add(file2)
root.add(sub_folder)

# Display structure
root.show_details()

    
