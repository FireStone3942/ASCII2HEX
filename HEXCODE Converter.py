global n 
global len1
global str1
global hexl
global l

def loop():
    len1 = len(CHAR)
    str1 = ' '
    n = 0
    while n < len1:
        if CHAR[n] in HEXV:
           HEX.append(HEXV.get(CHAR[n]))
        n += 1
    print (str1.join(HEX))


def line():
    l = 1
    hexl = hex(l)
    print(hexl)


HEXV = {" ":"20","A":"41","a":"","B":"42","b":"","C":"43","c":"","D":"44","d":"","E":"45","e":"","F":"46","f":"","G":"47","g":"","H":"48","h":"","I":"49","i":"","J":"","j":"","K":"","k":"","L":"","l":"","M":"","m":"","N":"","n":"","O":"","o":"","P":"","p":"","Q":"","q":"","R":"","r":"","S":"","s":"","T":"","t":"","U":"","u":"","V":"","v":"","W":"","w":"","X":"","x":"","Y":"","y":"","Z":"","z":""}
i = input(str('Insert Phrase:'))
HEX =[]
CHAR = list(i)

line()
loop()
