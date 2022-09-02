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


HEXV = {" ":"20","A":"41","a":"61","B":"42","b":"62","C":"43","c":"63","D":"44","d":"64","E":"45","e":"65","F":"46","f":"66","G":"47","g":"67","H":"48","h":"68","I":"49","i":"69","J":"4A","j":"6A","K":"4C","k":"6C","L":"4D","l":"6D","M":"4E","m":"6E","N":"4F","n":"6F","O":"50","o":"70","P":"51","p":"71","Q":"52","q":"72","R":"53","r":"73","S":"54","s":"74","T":"55","t":"75","U":"56","u":"76","V":"57","v":"77","W":"58","w":"78","X":"59","x":"79","Y":"5A","y":"7A","Z":"5B","z":"7B"}
i = input(str('Insert Phrase:'))
HEX =[]
CHAR = list(i)

line()
loop()
