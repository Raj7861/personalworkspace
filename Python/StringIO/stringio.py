import io
from pathlib import Path
import logging

FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

path =  Path('.')

logging.basicConfig(filename=f"{Path(__file__).parent.absolute()}/logs.log", level=logging.DEBUG, format=FORMAT)

with open("yes.txt") as file:
    content = file.read()
    with io.StringIO(content) as fileob:
        fileob.seek(0)
        print(fileob.read())

# logging.debug(f"! File name is {Path(__file__).absolute()}")
# logging.debug(f"File name is {Path(__file__).parent.absolute()}")
print(f"! File name is {Path(__file__).resolve().parent}")
# print(f"File name is {Path(__file__).parent.absolute()}")

for i in path.iterdir():
    if i.suffix == '.py':
        print(i)


