import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts" # r means raw mode so python will not try to escape eg: \n = breakline
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

#file = open(hosts_path, "r")
#print(file.read())

while True:
    if 16 <= dt.now().hour <= 19:
        print("Working Hours...")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Fun Hours...")
        with open(hosts_path, "r+") as file:
            content = file.readlines() # produces a list of lines instead
            file.seek(0) # move file pointer to start of file
            for line in content:
                if not any(website in line for website in website_list): # any so if any iteration of loop doesnt contain the
                                                                         # website, will write to file
                    file.write(line)
            file.truncate() # remove everything after the current location of file pointer
    time.sleep(5)
