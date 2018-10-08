import termcolor
import shodan


def shodans():

    bans = """
  _________.__               .___              
 /   _____/|  |__   ____   __| _/____    ____  
 \_____  \ |  |  \ /  _ \ / __ |\__  \  /    \ 
 /        \|   Y  (  <_> ) /_/ | / __ \|   |  |
/_______  /|___|  /\____/\____ |(____  /___|  /
        \/      \/            \/     \/     \/
    """
    print termcolor.cprint(bans, "red")
    SHODAN_API_KEY = "sWfpxsuma0QdxYQ3dLG0OH6Y1QV7bYxr"
    api = shodan.Shodan(SHODAN_API_KEY)
    hs = str(raw_input("Enter a host to scan: "))
    host = api.host(hs)
    print """
                 IP: %s
                 ORGANIZATION: %s
                 OPERATING SYSTEM: %s
             """ % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'))
    for item in host['data']:
        print """Port: %s
                    Banner: %s""" % (item['port'], item['data'])


shodans()