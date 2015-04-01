'''
    This is the biicode hook file. It changes some relative #include's to make possible POCO reusing

    You can revert all the modifications suffered in the original code. By default,
    if you're using biicode, the changes are applied:

        BII_FLAT_REVERT_CHANGES = 'False'

    To revert all, run into your current command prompt:

        Windows:    $ set BII_FLAT_REVERT_CHANGES=True
        Unix:       $ export BII_FLAT_REVERT_CHANGES=True

    and execute "bii work" to back into original form.
'''
import os
import re
import shutil
import platform


def replacement(match_object):
    if not "Poco/Net/" in match_object.group(0):
        return '#include "Poco/Net/%s"' % match_object.group(1)
    return '#include "%s"' % match_object.group(1)


def save(path, binary_content):
    with open(path, 'wb') as handle:
        handle.write(binary_content)


def load(path):
    with open(path, 'rb') as handle:
        return handle.read()


def search_and_replace_pattern(_files, base_path, pattern):
    for _file in _files:
        try:
            _file_path = os.path.join(base_path, _file)
            c = load(_file_path)
            c = re.sub(pattern, replacement, c)
            save(_file_path, c)
        except:
            pass


def search_and_replace(_file, token, _replacement):
    try:
        c = load(_file)
        c = c.replace(token, _replacement)
        save(_file, c)
    except:
        pass


def apply_changes():
    ''' Applying necessary chnages to use Flatbuffers with biicode '''
    shutil.copy(os.path.join(root_folder, 'biicode', 'conf', 'biicode.conf'), root_folder)
    search_and_replace(cmakelist_path, cmakelist_token, cmakelist_replacement)


def revert_changes():
    ''' Revert all the biicode changes code '''
    os.remove(biicode_conf_path)
    if os_platform == "Windows":
        search_and_replace(cmakelist_path, cmakelist_replacement_win, cmakelist_token)
    else:
        search_and_replace(cmakelist_path, cmakelist_replacement, cmakelist_token)


# Main code
os_platform = platform.system()
BII_FLAT_REVERT_CHANGES = os.environ.get('BII_FLAT_REVERT_CHANGES', 'False')

root_folder = bii.block_folder if os.path.exists(bii.block_folder) else bii.project_folder
biicode_conf_path = os.path.join(root_folder, 'biicode.conf')

cmakelist_path = os.path.join(root_folder, "CMakeLists.txt")
cmakelist_token = "project(FlatBuffers)"
cmakelist_replacement = '''if(BIICODE)
include(biicode/cmake/biicode.cmake)
return()
endif()
project(FlatBuffers)'''
cmakelist_replacement_win = "if(BIICODE)\r\ninclude(biicode/cmake/biicode.cmake)\r\nreturn()\r\nendif()\r\nproject(FlatBuffers)"

try:
    # Apply or revert changes
    if BII_FLAT_REVERT_CHANGES == 'False':
        if "if(BIICODE)" in load(cmakelist_path):
            print "Hook: changes just applied"
        else:
            print "Hook: applying changes"
            apply_changes()
    else:
        if "if(BIICODE)" not in load(cmakelist_path):
           print "Hook: changes just reverted"
        else:
            print "Hook: reverting changes"
            revert_changes()
except Exception as e:
    print "Exception: %s" % e