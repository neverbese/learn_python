import os
import string

from termcolor import colored, cprint
import colorama

colorama.init()

class NoTemplateError(Exception):
    pass


def get_template_dir_path():
    template_dir_path = None
    try:
        import settings
        if settings.TEMPLATE_PATH:
            template_dir_path = settings.TEMPLATE_PATH
    except ImportError:
        # print('not set')
        pass

    if not template_dir_path:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(base_dir, 'templates')

    return template_dir_path


def find_template(tem_file):
    template_dir_path = get_template_dir_path()
    tem_file_path = os.path.join(template_dir_path, tem_file)

    if not os.path.exists(tem_file_path):
        raise NoTemplateError('Could not find {}'.format(tem_file))
    return tem_file_path


def get_template(tem_file, color="green"):
    template = find_template(tem_file)
    # print(template)
    with open(template, 'r', encoding="utf-8_sig") as template_file:
        contents = template_file.read()
        contents = contents.rstrip('\n')
        contents = '{spliter}\n{contents}\n{spliter}\n'.format(
            contents=contents,
            spliter='=' * 40)
        colorama.init()
        # contents = cprint(contents, color)
        # colorama.init()
        # return string.Template(repr(cprint(contents)))
        return string.Template(contents)


#get_template('good_bye.txt')
