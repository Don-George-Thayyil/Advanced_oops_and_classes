import abc

class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        pass
    @abc.abstractmethod
    def get_printer_status(self):
        pass

class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan_document(self):
        pass
    @abc.abstractmethod
    def get_scanner_status(self):
        pass

class Mfd1(Printer,Scanner):
    def print_document(self):
        print("Prints low quality document")
    def get_printer_status(self):
        print("Not capable of printing status")
    def scan_document(self):
        print("Low quality document scanning")
    def get_scanner_status(self):
        print("Not capable")

class Mfd2(Printer, Scanner):
    def print_document(self):
        print("Prints good quality document")
    def get_printer_status(self):
        print("Printing printer status")
    def scan_document(self):
        print("Good quality document scanning")
    def get_scanner_status(self):
        print("Printing scanner status")
        

class Mfd3(Printer, Scanner):
    def print_document(self):
        print("Prints best quality document")
    def get_printer_status(self):
        print("Printing printer status and history")
    def scan_document(self):
        print("Best quality document scanning")
    def get_scanner_status(self):
        print("Printing scanner status and history")

