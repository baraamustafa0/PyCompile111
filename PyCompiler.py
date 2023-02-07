import marshal,os
def freez():
    while 1: x=0
a=input("\033[32mfile >\033[39m ")
a=f"{a}"
if("/" in a):
    os.system("clear")
    print("\033[33mYou Should Enter a File Name[not the path]\033[39m")
    freez()
else : pass

if( a.endswith ( ".py" ) ) == True : 
    pass
else : 
    print ('The file isʼnt ends with python extension(".py")')
    freez()

if( os.path.exists(a) ) == True :
    pass
else :
    print("The file isʼnt exists")
    freez()

x=open(a, "r")
r = x.read()
b=compile(r,'','exec')
c=marshal.dumps(b)
d=open("Encrypted"+'_'+a, 'w')
d.write(r"""import marshal
import sys
if( float(sys.version[:3] ) >= float( '3.9' ) ):
    exec ( marshal.loads ( """+repr(c)+r''' ) )
else:
    print(f'# no support for "%s"' % sys.version.split(" ")[0])
''')
x.close()
d.close()
print(f"\033[34msuccessfully\033[39m | \033[35mSaved as \033[39m; \033[31m\"\033[31m"+os.getcwd()+"/Encrypted_"+a+"\033[31m\"\033[39m")