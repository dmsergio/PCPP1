class BankAccount:
    def __init__(self, iban: str) -> None:
        self.iban = iban

    @staticmethod
    def iban_is_valid(iban: str) -> bool:
        return len(iban) == 20


if __name__ == "__main__":
    ibans = [
        "8" * 20,
        "7" * 4,
        "2222"]

    for iban in ibans:
        if BankAccount.iban_is_valid(iban):
            print(f"We can use {iban} to create a bank account")
        else:
            print(f"The IBAN {iban} is invalid")
