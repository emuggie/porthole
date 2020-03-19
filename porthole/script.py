import sys, json, argparse 
from . import server
from . import client
    
parser = argparse.ArgumentParser()
subParser = parser.add_subparsers(help="command to run. -h with command shows detailed options.", dest="command")
sP=subParser.add_parser("serve",help="host os info through http server.")
sP.add_argument("-host", dest="host",default="", help="host for service.")
sP.add_argument("-p","-port", dest="port",default=8000,type=int, help="port for service.")
sP=subParser.add_parser("get",help="get os info from destination server.")
sP.add_argument("-d", "-destination",dest="url", help="target uri", required=True)
sP=subParser.add_parser("test",help="test expression with os info given from destination server.")
sP.add_argument("-d","-destination",dest="url",required=True, help="target uri")
sP.add_argument("-e","-expression",dest="expr",required=True,help="expression string")

args = parser.parse_args()

#porthole serve -h "" -p 8080
if args.command == "serve" :
    server.serve(args.host, args.port)
    exit(0)

#porthole get "URI"
if args.command == "get" :
    print(json.dumps(client.get(args.url), indent=4))
    exit(0)

#porthole check "URI" "expression"
if args.command == "test" :
    (ok, err) = client.test(args.url, args.expr)
    if not ok :
        print(err)
    exit(not ok)
        