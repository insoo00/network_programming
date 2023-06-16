import paramiko
import getpass

ssh = paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

user = input('Username: ')
pwd = getpass.getpass('Password: ')
ssh.connect('114.71.220.5', 22, username=user, password=pwd)

# SFTP 클라이언트 객체 생성 
sftp = ssh.open_sftp()
src_file_path = 'index_sftp2.html' 
dst_file_path = 'test12321312321312313/' + src_file_path 
sftp.put(src_file_path, dst_file_path)

src_file_path = dst_file_path 
dst_file_path = 'index_sftp2_get.html' 
sftp.get(src_file_path, dst_file_path)

sftp.close()
ssh.close()