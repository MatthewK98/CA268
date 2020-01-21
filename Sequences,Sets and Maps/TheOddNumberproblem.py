import sys
def get_odd_list():                                                           
    lst = []   
    for i in sys.stdin:
        i = i.strip()
        if str(i) == "-1":
            break
        if int(i) % 2 != 0:
            lst.append(int(i))
        else:
            pass
    return lst

# print(get_odd_list(line))

def main():
    odds = get_odd_list()
    print(odds)

if __name__ == "__main__":
    main()