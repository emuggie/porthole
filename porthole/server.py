import sys, os, datetime, json, mimetypes
import SimpleHTTPServer, SocketServer


class PortHoleHandler(SimpleHTTPServer.SimpleHTTPRequestHandler) :
    def do_GET(self) :
        #response with static resource
        if(not self.path.endswith("/json")) :  
            if self.path == "/" :
                self.path = "/index.html"
            path = os.path.dirname(__file__) + "/static" + self.path
            
            self.send_response(200)
            self.send_header("Content-type", self.guess_type(path))
            f = open(path,"rb")
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            self.end_headers()
            self.copyfile(f,self.wfile)
            f.close()
            return
        
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

def serve(host="", port=8000) : 
    print("Porthole server at :[" + host + ":" +  str(port)+"]")
    httpd = SocketServer.TCPServer((host, port), PortHoleHandler)
    httpd.serve_forever()

