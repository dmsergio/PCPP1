"""
Your task is to build a multifunction device (MFD) class consisting of methods
responsible for document scanning, printing, and sending via fax.

The methods are delivered by the following classes:
    - scan(), delivered by the Scanner class;
    - print(), delivered by the Printer class;
    - send() and print(), delivered by the Fax class.

Each method should print a message indicating its purpose and origin, like:
    - 'print() method from Printer class'
    - 'send() method from Fax class'

Create an MFD_SPF class ('SPF' means 'Scanner', 'Printer', 'Fax'), then
instantiate it;

Create an MFD_SFP class ('SFP' means 'Scanner', 'Fax', 'Printer'), then
instantiate it;

On each object call the methods: scan(), print(), send();

Observe the output differences. Was the Printer class utilized each time?
"""


class Scanner:
    def scan(self):
        print("scan() method from Scanner class")


class Printer:
    def print(self):
        print("print() method from Printer class")


class Fax:
    def send(self):
        print("send() method from Fax class")

    def print(self):
        print("print() method from Fax class")


class MFD_SPF(Scanner, Printer, Fax):
    pass


class MFD_SFP(Scanner, Fax, Printer):
    pass


def main() -> None:
    spf = MFD_SPF()
    sfp = MFD_SFP()

    for obj in (spf, sfp):
        print(f"Calling methods for {obj.__class__.__name__} ...")
        obj.scan()
        obj.print()
        obj.send()
        print()


if __name__ == "__main__":
    main()
