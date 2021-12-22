import os
import argparse


parser = argparse.ArgumentParser(description='Programme to bulk delete files.')
parser.add_argument(
  '-f',
  metavar='file',
  type=str,
  help='the path to a file with file paths, 1 per line')


def main(file_path):
  with open(file_path) as f:
    count = 0
    for line in f.readlines():
      line = line.replace('\n', '')
      if line and len(line) > 0 and os.path.isfile(line):
        os.remove(line)
        count +=1
        print(line + ' deleted')

    print(str(count) + ' files deleted')


if __name__ == '__main__':
  print('deleting files started...')
  args = parser.parse_args()
  main(args.f)
