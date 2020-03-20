# porthole
Simple server and client reporting cpu and disk usage of os.

## What is this?
Tool for continuous monitering of os with minimum efforts.

Run server which runs certain shell command and returns result in json format.
Default contents contains index.html with df, vmstat.

Run client in any machine to fetch current status, or test with your own logics to check.

Use or write your own pages and shell command, parser you need.

Simple, python 2~3 compatible, standard-package-only tool.

## Prerequistes.
Linux environments.
Python 2.7 and above.

## Installation
#### Using Python package manager
```bash
pip install porthole-cmd
```

#### Manual setup
Download distributes and extract and run.
```bash
tar -xvf porthole-0.0.1.tar
cd porthole-0.0.1
python -m porthole.script serve
```

## Server
Run porthole server to OS which desired to be monitored.
#### pip 
```bash
porthole serve -host [host/default:""] -p [port/default:8000]
```

#### Manual setup
```bash
python -m porthole.script serve -host [host/default:""] -p [port/default:8000]
```

### Client
#### Fetch response
Fetch response from server in dict, list format.
```bash
porthole fetch -d [destination]
#OR
python -m porthole.script fetch -d [destination]
```

#### Test
Test response with expression to automate monitoring.
```bash
porthole test -e [expr] -s [source] -d [destination]
#OR
python -m porthole.script test -e [expr] -s [source] -d [destination]
```
-e [expr] is expression to test.
Or -s [source] to write your expression in file.
```python
# Example of using expression script.
# It is recommanded to fetch and examine response before writing expression.

# Test All element in resposne
all(disk["Use%"] < "70" for disk in response)
```

### Help
```bash
porthole -h
#OR
python -m porthole.script -h
```

## Extending and customizing
#### Server
Adding new path.
```python
import porthole

#alter resource path if you have html,js, image, etc...
porthole.ResoursePath = "your static resource path"

# add or redefine your handler
# if object is returned, it will be jsonized.
# if string is returned, it will be just string.
# /df, /vmstat is included default.
onGet('path', yourHandler)

serve(host="", port=8000)
```

#### Client
```python
import porthole

#fetch data from server
data = porthole.fetch("server path")

#write your own code.
if len(data.response.disks) ==0 :
    exit(1)
exit(0)
```

## Next Updates
Make shell options available with query param.