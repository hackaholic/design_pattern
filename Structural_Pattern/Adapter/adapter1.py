
from abc import ABC, abstractmethod

# Step 1: Define a common interface
class PrinterInterface:
    @abstractmethod
    def print():
        pass

# Step 2: Existing class (Old Printer with a different interface)
class OldPrinter:
    def print_text(self, text: str) -> str:
        return f"Old Printer: {text}"

# Step 3: New Printer (Already follows the expected interface)
class NewPrinter(PrinterInterface):
    def print(self, text) -> str:
        return f"New Printer: {text}"

# Step 4: Adapter to make OldPrinter compatible with PrinterInterface
class PrinterAdapter(PrinterInterface):
    def __init__(self, printer: OldPrinter|NewPrinter):
        self.printer = printer
    
    def print(self, text) -> str:
        if hasattr(self.printer, "print_text"):
            return self.printer.print_text(text)
        return self.printer.print(text)

# Step 5: Using the Adapter for both printers
oldprinter = OldPrinter()
newprinter = NewPrinter()

oldprinter_adapter = PrinterAdapter(oldprinter)
newprinter_adapter = PrinterAdapter(newprinter)

print(oldprinter_adapter.print("Hello Coco"))
print(newprinter_adapter.print("Hello Coco"))

