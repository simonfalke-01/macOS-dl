import argparse
import subprocess
import os
import posixpath
from urllib.parse import urlsplit, unquote
import pathlib
import colorama
import re

username = subprocess.run(['whoami'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()


def parse_args():
    parser = argparse.ArgumentParser()
    # URL Arg
    parser.add_argument('url', nargs='?', type=str, default=None, help='URL to download')

    return parser.parse_args()


def exists(path):
    return pathlib.Path(f'/Users/{username}/Downloads/{path}').exists()


def add_ext(split_basename, ext):
    return f'{split_basename[0]} {ext}.{split_basename[1]}'


def filename(url):
    urlpath = urlsplit(url).path
    basename = posixpath.basename(unquote(urlpath))
    if os.path.basename(basename) != basename or unquote(posixpath.basename(urlpath)) != basename:
        raise ValueError

    if exists(basename):
        ext = 1
        split_basename = basename.split('.')

        while exists(add_ext(split_basename, ext)):
            ext += 1

        basename = add_ext(split_basename, ext)

    return basename


def main():
    args = parse_args()
    url = args.url
    file = filename(url)
    full_path = f'/Users/{username}/Downloads/{file}'

    # Regex that matches any curl error
    curl_error = r'curl: \(\d+\) .*'

    process = subprocess.Popen(f'curl -L {url} -o "{full_path}"',
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               shell=True)

    while True:
        output = process.stdout.readline().decode('utf-8').strip()

        # If curl error, print error and exit
        if searched := re.search(curl_error, output):
            # Let error be the matched text from the regex
            error = searched.group(0)
            print(colorama.Fore.RED + error + colorama.Fore.RESET)
            exit(1)

        if output == '' and process.poll() is not None:
            break

        if output:
            print(output.strip(), flush=True)

    print('Downloaded', colorama.Fore.GREEN + file + colorama.Fore.RESET, 'to', colorama.Fore.BLUE + '~/Downloads/' +
          colorama.Fore.RESET)


if __name__ == '__main__':
    main()
