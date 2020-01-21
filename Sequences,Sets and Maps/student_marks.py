import sys


def make_map():
    students = {}
    for line in sys.stdin:
        line = line.strip().split()
        if line == []:
            break
        student = line[0]
        mark = line[1]
        students[student] = mark
    return students