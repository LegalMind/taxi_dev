import sys
import os
import io
import csv

MAX_LINE = 5

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

input_dir = "input"
abs_input_dir = os.path.join(os.path.abspath('.'), input_dir)


def filter_com_type(rec):
    if rec[0] == '개인':
        return True
    else:
        return False


def view_lines(filen):
    i = 0
    recs = []
    with open(os.path.join(abs_input_dir, filen)) as f:
        for line in f:
            if i > MAX_LINE:
                break
            recs.append([''.join(i) for i in csv.reader(line)])
            i += 1

    recs = filter(filter_com_type, recs)

    for rec in recs:
        print(rec)


def main():
    input_list = os.listdir(abs_input_dir)
    for i in input_list:
        print("[+] filename : %s" % i)
        view_lines(i)


if __name__ == "__main__":
    main()
