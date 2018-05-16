def main():
    print("Module name is: {}".format(__name__))

if __name__ == '__main__':
    main()
    print("Ran Directly")
else:
    print("Ran from Import")