import sys

print('the command line arguments are:')
for i in sys.argv:
    print(i)
print(sys.path)


if __name__ == '__main__':
    print('this is program is being run by itself')
else:
    print('i am being importted from another module')
