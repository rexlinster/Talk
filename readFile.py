def readFile(filename) :
    with open(filename,'r',encoding='utf-8-sig') as f :
        readFile = []
        for line in f :
            readFile.append(line.strip())
        return readFile



def main() :
    readfiles = readFile('input.txt')
    print(readfiles)

main()



