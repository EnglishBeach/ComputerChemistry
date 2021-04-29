def f(inarg,outarg):
    return inarg**outarg

def outf(f,k,*args):
    k +=1
    s = f(outarg = k,*args)
    return s

def main():
    inarg= 2
    s = outf(f,5,inarg)
    print (s)
main()