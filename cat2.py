


def read(some_file):

        with open(some_file,"r") as f:
            f_contents = f.read()
            print(f_contents)

def write(some_file):

            f2 = open(some_file,"w")
            f2.write(input("What do you want to write?"))
            f2.close()

def append(some_file):

            f2 = open(some_file,"a")
            f2.write(input("What do you want to append?"))
            f2.close()

def create(some_file):
            
            f2 = open(some_file,"a")
            f2.close()

def cat(some_file):

        with open(some_file,"r") as f:

            f_contents = f.read()
            print(f_contents)

            newfile = input("Where do you want to cat it?")
            f2 = open(newfile,"a")
            f2.write(f_contents)
            f2.close()



def main():
    filename = input("Enter filename: ")
    what_to_do = input("What do you want to do with it?[(r)ead][(w)rite][(c)reate][(a)ppend][(k)cat]")

    if what_to_do == 'r':
        read(filename)
    elif what_to_do == 'w':
        write(filename)
    elif what_to_do == 'c':
        create(filename)
    elif what_to_do == 'a':
        append(filename)
    elif what_to_do == 'k':
        cat(filename)
    else:
        print("Invalid input")

if __name__ == '__main__':
    main()