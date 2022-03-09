print('''|~~\   /\  |\  /||\  |
|   | /__\ | \/ || \ |
|__/ /    \|    ||  \|
                      ''')
with open("website.log","r") as f:
    lines = f.readlines()
    for line in lines:
        l=line.split(" ")
        print("IP \t Datetime\t Requesttype\t protocol\t statuscode\t filesize\t useragentdetails\t")
        print("{} \t {} \t {} \t {} \t {} \t {} \t {} \t".format(l[0],l[3:5],l[5],l[7],l[8],l[9],l[11:]).replace('"',' '))
