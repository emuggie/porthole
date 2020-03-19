import porthole

def test() : 
    outputLines = os.popen("df").read().splitlines()
    keywords = outputLines[0].split()
    disks = []
    for i in range(1,len(outputLines)):
        disk = {}
        values = outputLines[i].split()
        for j in range(len(values)) :
            disk[keywords[j]]= values[j]
        disks.append(disk)

    outputLines = os.popen("vmstat").read().splitlines()
    keywords = outputLines[-2].split()
    cpu = {}
    values = outputLines[-1].split()
    for i in range(len(values)) :
        cpu[keywords[i]]= values[i]
    data = {
        "cpu" : cpu,
        "disks" : disks
    }    
    return data

porthole.onGet("/test", test)
porthole.serve()