'''
f= open('alumnos.txt','r')
nombres = f.read()
print(nombres)
f.seek(0)
nombres2=f.read()
print(nombres2)
f.close()

f= open('alumnos.txt','r')
nombres = f.readlines()
for item in nombres:
    print(item,end='')
f.close()
'''
f= open('alumnos.txt','w')
f.write('\n'+'Hola Mundo')
f.close()