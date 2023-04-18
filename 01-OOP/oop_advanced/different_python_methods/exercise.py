"""
Create a class representing a luxury watch;

The class should allow you to hold a number of watches created in the
watches_created class variable. The number could be fetched using a class
method named get_number_of_watches_created;

The class may allow you to create a watch with a dedicated engraving (text).
As this is an extra option, the watch with the engraving should be created
using an alternative constructor (a class method), as a regular __init__ method
should not allow ordering engravings;

The regular __init__ method should only increase the value of the appropriate
class variable;

The text intended to be engraved should follow some restrictions:
    - it should not be longer than 40 characters;
    - it should consist of alphanumerical characters, so no space characters
      are allowed;
    - if the text does not comply with restrictions, an exception should be
      raised;
"""


class EngravingTextValidationError(Exception): ...


class LuxuryWatch:
    watches_created = 0

    def __init__(self) -> None:
        LuxuryWatch.watches_created += 1
        self.engraving_text = ""

    @classmethod
    def get_number_of_watches_created(cls) -> int:
        return cls.watches_created

    @classmethod
    def init_luxury_watch(cls, engraving_text: str):
        cls.check_engraving_text(engraving_text)
        watch = cls()
        watch.engraving_text = engraving_text
        return watch

    @staticmethod
    def check_engraving_text(engraving_text: str) -> bool:

        def check_len() -> bool:
            return len(engraving_text) <= 40

        def check_alphanumerical() -> bool:
            return engraving_text.isalnum()

        if not check_len() or not check_alphanumerical():
            raise EngravingTextValidationError(
                "The engraving text given is not valid. Please, the text "
                "mustn't exceeds 40 characters and must to be alphanumeric.")
        return True
