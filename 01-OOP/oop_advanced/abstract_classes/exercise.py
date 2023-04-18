"""
You are about to create a multifunction device (MFD) that can scan and print
documents;

The system consists of a scanner and a printer;

Your task is to create blueprints for it and deliver the implementations;

Create an abstract class representing a scanner that enforces the following
methods:
    - scan_document: returns a string indicating that the document has been
      scanned;
    - get_scanner_status: returns information about the scanner (max. resolution,
      serial number)

Create an abstract class representing a printer that enforces the following
methods:
    - print_document: returns a string indicating that the document has been
      printed;
    - get_printer_status: returns information about the printer (max.
      resolution, serial number)

Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes
responsible for scanning and printing:
    - MFD1: should be a cheap device, made of a cheap printer and a cheap
      scanner, so device capabilities (resolution) should be low;
    - MFD2: should be a medium-priced device allowing additional operations
      like printing operation history, and the resolution is better than the
      lower-priced device;
    - MFD3: should be a premium device allowing additional operations like
      printing operation history and fax machine.

Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices
should be capable of serving generic feature sets.
"""
import abc


class Scanner(abc.ABC):

    @abc.abstractmethod
    def scan_document(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass


class Printer(abc.ABC):

    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass


class MFD1(Scanner, Printer):

    def scan_document(self):
        return "The document has been scanned."

    def get_scanner_status(self):
        return "SN: MFD1-SC-0001; Resolution: 800x600px"

    def print_document(self):
        return "The document has been printed."

    def get_printer_status(self):
        return "SN: MFD1-PT-0001; Resolution: 800x600px"


class MFD2(Scanner, Printer):

    def scan_document(self):
        return "The document has been scanned."

    def get_scanner_status(self):
        return "SN: MFD2-SC-0001; Resolution: 1280x900px"

    def print_document(self):
        return "The document has been printed."

    def get_printer_status(self):
        return "SN: MFD2-PT-0001; Resolution: 1280x900px"


class MFD3(Scanner, Printer):

    def scan_document(self):
        return "The document has been scanned."

    def get_scanner_status(self):
        return "SN: MFD3-SC-0001; Resolution: 2000x1600px"

    def print_document(self):
        return "The document has been printed."

    def get_printer_status(self):
        return "SN: MFD3-PT-0001; Resolution: 2000x1600px"


if __name__ == "__main__":
    for obj in (MFD1(), MFD2(), MFD3()):
        print(obj.scan_document())
        print(obj.print_document())
        print(obj.get_scanner_status())
        print(obj.get_printer_status())
        print()
