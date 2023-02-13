from sys import argv

from compare_versions import compare

if __name__ == "__main__":
    if len(argv) != 3:
        print("Incorrent number of arguments passed")
    version_1 = argv[1]
    version_2 = argv[2]
    print(compare(version_1, version_2))
