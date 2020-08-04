from sys import stdin
import re


def parsing(language, variable):
    transformed_variable = ''
    if language == 'C++':
        for idx, word in enumerate(variable.split('_')):
            if idx != 0:
                transformed_variable += word[0].upper() + word[1:]
            else:
                transformed_variable += word
    elif language == 'JAVA':
        word_list = []
        for char in variable:
            if 'A' <= char <= 'Z':
                word_list.append(transformed_variable)
                transformed_variable = char.lower()
            else:
                transformed_variable += char
        word_list.append(transformed_variable)
        transformed_variable = '_'.join(word_list)
    return transformed_variable


def main():
    variable = stdin.readline().rstrip()
    c_pattern = re.compile('([a-z]+_)*([a-z]+)')
    java_pattern = re.compile('([a-z]+)([A-Z]{1}[a-z]*)*')

    if c_pattern.fullmatch(variable) is not None:
        print(parsing('C++', variable))
    elif java_pattern.fullmatch(variable) is not None:
        print(parsing('JAVA', variable))
    else:
        print('Error!')


if __name__ == "__main__":
    main()
