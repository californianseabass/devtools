import argparse
import collections
import hashlib
import os

DESCRIPTION = ''


filepath_to_md5_cache = {}


def check_cache(cache):
    def decorator(f):
        def wrapper(key):
            if key in cache.keys():
                print('cache hit')
                return cache[key]
            value = f(key)
            cache[key] = value
            return value
        return wrapper
    return decorator


def get_files(folder, recursive):
    if not recursive:
        return [
            os.path.join(folder, filename)
            for filename
            in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, filename))
        ]
    else:
        result = []  # files
        for dirpath, dirs, files in os.walk(folder):
            result.extend((os.path.join(dirpath, filename) for filename in files))
        return result


@check_cache(filepath_to_md5_cache)
def get_md5_hash_for_file(filepath):
    try:
        with open(filepath, 'rb') as f:
            contents = f.read()
            m = hashlib.md5()
            m.update(contents)
            return m.hexdigest()
    except Exception as e:
        print(e)


def print_duplicates(duplicates):
    for md5, filepaths in duplicates.items():
        print(md5)
        for filepath in filepaths:
            print(f'\t{filepath}')


def main(folders, recursive, should_print_duplicates):
    files = []
    for folder in (os.path.expandvars(os.path.expanduser(folder)) for folder in folders):
        if not os.path.isdir(folder):
            raise Exception('--folder argument must be a directory')
        files.extend(get_files(folder, recursive))
    file_to_hash = {}
    hash_to_file = collections.defaultdict(list)
    for filepath in files:
        md5 = get_md5_hash_for_file(filepath)
        file_to_hash[filepath] = md5
        hash_to_file[md5].append(filepath)
    duplicates = {k: v for k, v in hash_to_file.items() if len(v) > 1}
    if should_print_duplicates:
        print_duplicates(duplicates)
    else:
        for file_hash, filename in hash_to_file.items():
            print(f'{filename},{file_hash}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='takes a file and print out a comma separated list of filepaths and md5 sums')
    parser.add_argument('--folders', type=str, help='comma separated list of directories to search for duplicates', default=None)
    parser.add_argument('--recursive', '-r', action='store_true', default=False)
    parser.add_argument('--duplicates', '-d', action='store_true', help='print out duplicates instead of csv with md5 sums', default=False)
    parser.add_argument('--cache_path', help='if set, save filepath to md5 as json for cacheing purposes. Will reuse and augment if already existent.')
    args = parser.parse_args()

    folders = args.folders.split(',') if args.folders else os.getcwd()
    if type(folders) == str:
        folders = [folders]
    print(folders)
    main(folders, args.recursive, args.duplicates)
