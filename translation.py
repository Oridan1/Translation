from translate import Translator
linea = ""
translator = Translator(to_lang="es")
try:
    with open("text.txt", mode='r') as my_file:
        linea = my_file.read()
        with open("translated.txt", mode='w') as my_file2:
            my_file2.write(translator.translate(linea))
            print("translation complete")
except FileNotFoundError:
    print("no text.txt file")
