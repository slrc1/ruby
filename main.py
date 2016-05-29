import sys,socket

f = open('log.txt','w+')
for item in sys.argv:
  f.write("%s\n" % item)
f.close()

ss = socket()
ss.bind('localhost',sys.argv[1])
ss.listen()
s,a = ss.accept()
s.sendall(b'hello')
s.close()
ss.close()
