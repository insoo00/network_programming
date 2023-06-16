import paramiko
import getpass

filename = '/home/net_pro/test12321312321312313/test99.zip' # 압축파일의 이름 
dirname = '/home/net_pro/test12321312321312313' # 압축할 폴더 
CMD='zip -r ' + filename + ' ' + dirname  # 리눅스 압축 명령어 
# zip -r /home/net_pro/test12321312321312313/test99.zip /home/net_pro/test12321312321312313

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

user = input('Username: ')
pwd = getpass.getpass('Password: ')
ssh.connect('114.71.220.5', 22, username=user, password=pwd)

stdin, stdout, stderr = ssh.exec_command(CMD) 

sftp = ssh.open_sftp()

src_filename = filename.split('/')[4]
sftp.get(filename, src_filename)

sftp.close()
ssh.close()