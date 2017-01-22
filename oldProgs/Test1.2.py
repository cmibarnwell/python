def volume(l, w, h):
    return l*w*h
    
def main():
    l=input("What is the length of the rectangle? ")
    h=input("What is the height of the rectangle? ")
    w=input("What is the width of the rectangle? ")

    l_int=int(l)
    h_int=int(h)
    w_int=int(w)

    print(volume(l_int,w_int,h_int))

main()
