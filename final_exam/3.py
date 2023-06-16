import smtplib
from email.message import EmailMessage
import getpass
import paramiko
import time
import filetype # 파일 유형을 판단해주는 모듈


BUFF_SIZE = 65535

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy) 

user = input('Username: ')
pwd = getpass.getpass('Password: ')

ssh.connect('114.71.220.5', username=user, password=pwd)
channel = ssh.invoke_shell()

# 채널을 통해 명령어 전송 
channel.send('mkdir 20191524\n') 
time.sleep(0.5)
channel.send('cd 20191524\n') 
time.sleep(0.5)
channel.send('echo iot > iot.txt\n') 
time.sleep(0.5)
channel.send('cat /proc/meminfo > mem.txt\n') 
time.sleep(0.5)

filename = '/home/net_pro/20191524/20191524.zip'    # 압축파일의 이름 
dirname = '/home/net_pro/20191524'                  # 압축할 폴더 
CMD='zip -r ' + filename + ' ' + dirname            # 리눅스 압축 명령어 
# zip -r /home/net_pro/20191524/20191524.zip /home/net_pro/20191524

channel.send(CMD + '\n') 
time.sleep(0.5)

sftp = ssh.open_sftp()
src_filename = filename.split('/')[4]
sftp.get(filename, src_filename)

sftp.close()
ssh.close()

# 보내는 메일 서버
SMTP_SERVER = 'smtp.gmail.com' 
SMTP_PORT = 587

# 송신자, 수신자, 비밀번호
sender = 'insoosos1234@gmail.com' 
family = ['daeheekim@sch.ac.kr', 'ninanooo@gmail.com']
password = 'zyrineickvzptzyo'

# 메시지 생성하기
msg = EmailMessage()
msg['Subject'] = '네트워크 프로그래밍 기말고사' 
msg['From'] = sender
msg['To'] = ', '.join(family)
text = '네트워크 프로그래밍 기말고사 답안 제출합니다' 
msg.set_content(text)

with open('20191524.zip', 'rb') as f:
    zip_data = f.read()
# add_attachment 함수를 이용해 파일 첨부. 파일 첨부시 첨부된 파일의 mime-type 지정 
msg.add_attachment(zip_data, maintype='application', subtype=filetype.guess_mime(zip_data), filename='20191524.zip')

#SMTP 객체 생성 후, 메시지 전송
s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT) 
s.ehlo()
s.starttls()
s.login(sender, password) 
s.send_message(msg)
s.quit()