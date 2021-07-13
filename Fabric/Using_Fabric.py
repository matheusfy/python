from fabric import *

host = '192.168.0.108'
port = 22
user = 'matheusfy'
connect_kwargs = {'password' : ''}

c = Connection(host=host, port=port, user=user, connect_kwargs=connect_kwargs)

c.open()
with c.cd('Documentos'):
    c.run('ls')
    c.put('\\*.py', '/')
# print(c.is_connected)