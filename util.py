def load_file(filename):
    f=open(filename,encoding="UTF-8")
    lines=[]
    for x in f: 
        lines.append(x)
    f.close()
    return lines

def write_file(filename, data):
    f = open(filename, "a", encoding= "utf-8")
    f.write(data)
    f.close()
    
  
    
    
