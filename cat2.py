import argparse

def read(some_file):
# """Read the files chosen and display it on the screen."""
    for files in some_file:
        with open(files,"r") as file_1:
            f_contents = ""
            f_contents += file_1.read()
            print(f_contents)

def write(some_file):
# """Write a certain text per file."""
    for files in some_file:
        with open(files,"w+") as file_1:
            file_1.write(input("What do you want to write in %s?" % [files]))


def append(some_file):
# """Append a certain text per file."""
    for files in some_file:
        with open(files,"a+") as file_1:
            file_1.write(input("What do you want to append in %s?" % [files]))


def create(some_file):
# """Create files."""
    for files in some_file:       
        with open(files,"a+") as file_1:
            file_1.close()

# def xd(some_file):
#     for files in some_file:
#         with open(files,"a+") as file_1:
#             file_1.write("XD")
        

def cat(some_file):
# """Copy all the contents of chosen files then cat it in a specific file."""
    newfile = input("Where do you want to cat it?")

    for files in some_file:
        with open(files,"r+") as file_1:
            f_contents = ""
            f_contents += file_1.read()

            file_2 = open(newfile,"a")
            file_2.write(f_contents)
            
parser = argparse.ArgumentParser()
    
parser.add_argument('files_list',nargs='*')
parser.add_argument('-w','--write',action = "store_true",help='to write on an n number of files')
parser.add_argument('-r','--read',action = "store_true",help='to read contents of n number of files')
parser.add_argument('-cr','--create',action = "store_true",help='to create n number of files')
parser.add_argument('-a','--append',action = "store_true",help='to append files')
parser.add_argument('-k','--cat',action = "store_true",help='to cat files')
# parser.add_argument('-x','--xd',action = "store_true",help=argparse.SUPPRESS)
args = parser.parse_args()

if args.read:
    read(args.files_list)
elif args.write:
    write(args.files_list)
elif args.append:
    append(args.files_list)
elif args.create:
    create(args.files_list)
elif args.cat:
    cat(args.files_list)
# elif args.xd:
#     xd(args.files_list)



