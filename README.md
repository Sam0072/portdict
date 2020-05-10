# Portdict

Portdict uses python 3, `beautifulsoup` and `requests` to find the definition of ports.

Usage:  `portdict [port number]`

##### Example output:
```
$ portscan 113

Loading. . .
Name:  auth / ident
Purpose: Authentication Service / Identification Protocol
Related ports: -

Auth/Ident servers — which are supposed to run on the local user's machine — open port 113 and listen for incoming connections and queries from remote machines. These querying machines provide a local and remote "port pair" describing some other already-existing connection between the machines. The user's "ident" server is tasked with looking up and returning the connection's "USER ID" and perhaps additional information, such as an eMail address, full name, or whatever.

```

##### Requirements
For this to work you need:
- Beautiful Soup 4
- `requests` pip module

### License
This is licensed under CC BY-SA. For more information, look here: https://creativecommons.org/licenses/by-sa/2.0/
