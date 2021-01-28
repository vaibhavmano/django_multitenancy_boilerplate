import os
import re

BOILERPLATE_NAME = 'django_boilerplate'


def validate_filename(project_name):
    new_name = re.findall('^[\w\_]+$', project_name)
    if new_name:
        return True
    else:
        return False


def main():
    try:
        print('\nInitializing MULTITENANCY configurator...')
        root = os.getcwd()
        all_files = [os.path.join(path, name) for path, subdirs, files in os.walk(root) for name in files]
        all_files = [file for file in all_files if '/__pycache__' not in file]
        while True:
            project_rename = input('Enter name of django project. Make sure there is no existing directory of the same name\n')
            flag = validate_filename(project_rename)
            if flag:
                break
            else:
                print("Make sure to use only underscores('_')\n")
                project_rename = input('Re-enter valid name of django project\n')
                pass
        for file in all_files:
            print(f'\nRenaming all occurences of project name in {file}...')
            with open(file, 'r') as infile:
                data = infile.read()
            with open(file, 'w') as infile:
                data = data.replace(BOILERPLATE_NAME, project_rename)
                infile.write(data)
        print('\nRenaming directory...')
        os.rename(BOILERPLATE_NAME, project_rename)
        print('\nRenaming root directory...')
        orginal_name = os.getcwd()
        new_name = orginal_name.replace(BOILERPLATE_NAME, project_rename)
        os.rename(orginal_name, new_name)
        print('\nConfiguration completed!\n')
    except Exception as e:
        print('Error occured in configurator ** {} **'.format(str(e)))


if __name__ == '__main__':
    main()
