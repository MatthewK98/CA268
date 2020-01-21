import sys



def get_counts(words: str):
    return [list(map(len, words)).count(n)
        for n in range(10)
    ]
    
def main():
    # read the list of words from stdin
    line = sys.stdin.readline()
    line = line.strip()
    words = line.split()
    lst = []

    # call the student's function and ...
    counts = get_counts(words)
    # ... print the result
    for length in range(10):
        lst.append(int(counts[length]))
    print(lst)

if __name__ == "__main__":
    main()