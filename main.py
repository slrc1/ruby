import sys,socket

f = open('log.txt','w+')
for item in sys.argv:
  f.write("%s\n" % item)
f.close()

s = socket()
s.connect('localhost',sys.argv[1])
s.sendall(b'hello')
s.close()
