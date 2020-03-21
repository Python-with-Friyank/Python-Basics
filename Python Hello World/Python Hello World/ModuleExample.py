# One way to import module is using import file name
import Converter
print(Converter.convert("Hello :)"))


# another to import module  with specific functions only
from Converter import convert
print(convert("haha :P"))

