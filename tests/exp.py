# Example of using expression script.
# It is recommanded to fetch and examine response before writing expression.

# Test All element in resposne
all(disk["Use%"] < "70" for disk in response)