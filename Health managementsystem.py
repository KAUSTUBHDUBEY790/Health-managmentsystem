def newrecipient(name,h):
    if h == 'D':
        k = open("{} diet plan.exe".format(name),'w')
        k.close()
    elif h == 'T':
        m = input("Name of the recipient")
        k = open("{} Training plan.exe".format(name),'w')

a = input("Press 1 to continue and -1 to end\n")
while a!=-1:
    k = input("Press N for new user and O for the exiting one\n")
    if k=='N':
        m = input("Name of the recipient\n")
        l = input("Press D for diet and T for training\n")
        newrecipient(m, l)
        a = input("Press 1 to continue and -1 to end\n")
        
        