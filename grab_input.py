import sys

def thing():
    print sys.argv[1]
    print int(sys.argv[1]) + 7

if __name__ == '__main__':
    print "Hello"
    thing()
