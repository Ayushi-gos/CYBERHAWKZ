with open("website.log","r") as f:
    lines = f.readlines()
    with open("new.txt","w+") as nf:
        for line in lines:
            l=line.split(" ")
            nf.write("IP \t Datetime\t Requesttype\t protocol\t statuscode\t filesize\t useragentdetails\t\n")
            nf.write("{} \t {} \t {} \t {} \t {} \t {} \t {} \t".format(l[0],l[3:5],l[5],l[7],l[8],l[9],l[11:]).replace('"',' '))
