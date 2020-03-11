import sys, os, datetime, json
import SimpleHTTPServer, SocketServer

class PortHoleHandler(SimpleHTTPServer.SimpleHTTPRequestHandler) :
    def do_GET(self) :
        
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
        
        self.send_response(200)
        #response with json
        if(self.path.endswith("json")) :
            data = {
                "cpu" : cpu,
                "disks" : disks
            }
            jsonStr = json.dumps(data)
            self.send_header("Content-type", "application/json")
            self.send_header("Content-Length", len(jsonStr))
            self.end_headers()
            self.wfile.write(jsonStr)
            return
        
        #response with text/html
        f = open("index.html","r")
        contents = f.read()
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", len(contents))
        #self.send_header("Last-Modified", self.date_time_string(datetime.datetime.now()))
        self.end_headers()
        self.wfile.write(contents)
        f.close()


PORT = 8000
if len(sys.argv) > 1 :
    PORT = int(sys.argv[1])
print("serving at port", PORT)
httpd = SocketServer.TCPServer(("", PORT), PortHoleHandler)
httpd.serve_forever()

