#Portdict

Portdict uses python 3, `beautifulsoup` and `requests` to find the definition of ports.

Usage:  `portdict [port number]`

##### Example output:
```
$ portscan 113 -w -s

Loading. . .
Name:  auth / ident
Purpose: Authentication Service / Identification Protocol
Related ports: -

Auth/Ident servers — which are supposed to run on the local user's machine — open port 113 and listen for incoming connections and queries from remote machines. These querying machines provide a local and remote "port pair" describing some other already-existing connection between the machines. The user's "ident" server is tasked with looking up and returning the connection's "USER ID" and perhaps additional information, such as an eMail address, full name, or whatever.

```



### License
You may use this for commercial purposes, I don't really care. You can't say you wrote this but you don't need to note my name. .
