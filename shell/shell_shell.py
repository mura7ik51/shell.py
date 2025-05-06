def echo(y):
    print(y)

def cat(y):
    print("")
    f = open(y)
    print(f.read())
    f.close()

def assign():
    variable = input("Variable:")
    number   = float(input("Nunber:"))

def addline(y):
    z = input("Enter Line:")
    with open(y,"a") as idk_maybe_something_like_file0:
        idk_maybe_something_like_file0.write(z)

def overwrite(y):
    OVERWRITE = input("This Command will overwrite everything. Are you sure? [y,N]")
    if OVERWRITE == "y":
        z = input("Enter Line:")
        with open(y,"w") as idk_maybe_something_like_file0:
            idk_maybe_something_like_file0.write(z)
    else:
        print("aborted")