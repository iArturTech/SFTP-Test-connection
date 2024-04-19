import paramiko

# create ssh client 
ssh_client = paramiko.SSHClient()

# remote server credentials
host = "hostname"
username = "username"
password = "password"
port = 22 # edit if not 22

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,port=port,username=username,password=password)

print('connection established successfully')

ssh_client.close()
