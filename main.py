import logging
import datetime
import time
import textwrap
output_file = "output.txt"

def custom_decor_logger(logfile):
    def decor_logger(func):
        def wrapper(*args, **kwargs):
            with open(logfile, 'w') as f_obj:
                file = open(logfile, 'w')
                start = datetime.datetime.now()
                f_obj.write(f'Функция {func.__name__} стартовала в: {start}\n')
                f_obj.write('Данные для вывода на печать: \n' + '\n'.join(args) + '\n')
                f_obj.write('Параметры вызова функции: \n')
                for key, value in kwargs.items():
                    f_obj.write("{} is {}".format(key, value) + '\n')
                result = func(*args, **kwargs)
                file.close()
            return result
        return wrapper
    return decor_logger

@custom_decor_logger("print.log")
def adv_print(*args, **kwargs):
    start_line = kwargs.get('start', '')
    max_line = kwargs.get('max_line', 100)
    in_file = kwargs.get('in_file', False)
    if in_file:
        with open(output_file, 'w') as f_obj:
            if start_line:
                print(start_line, file=f_obj)
            for item in args:
                print('\n'.join(textwrap.wrap(item, max_line)), file=f_obj)
    else:
        if start_line:
            print(start_line)
        for item in args:
            print('\n'.join(textwrap.wrap(item, max_line)))


adv_print("zzzzzzzzzzzzzzzzzzzzz","zzzzxxxxxxxxxxxxxxxxxxxxxxxxx",start="Start Line!", max_line=10)

