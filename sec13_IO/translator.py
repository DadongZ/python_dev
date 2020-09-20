from translate import Translator
from os.path import dirname, join

input_file = join(dirname(__file__), 'test.txt')

try:
    with open(input_file, 'r') as f:
        l0 =f.readline()
        print(f.read())
except FileNotFoundError as  err:
    print('file not found!')
    raise err

translator = Translator(to_lang = 'zh')
translation = translator.translate(l0)

with open(input_file, 'a') as f:
    f.write(translation)