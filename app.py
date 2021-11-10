from flask import Flask
from flask import request
from flask import render_template
import time
import paramiko

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/ssh')
def ssh():
    name = request.values.get("name")
    port = request.values.get("port")
    hostname = '121.42.12.81'
    # port = '40050'
    username = 'boon'
    password = 'Boon2350@#%)'
    # 设置文件路径
    remotepath = "/home/boon/get_data.py"#远程文件路径
    localpath = r"C:\Users\Administrator\Desktop\flask\static\get_data.py" #本地文件路径
    rename = "孙彦丰.txt" #文件下载重命名
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在~/.ssh/known_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=hostname,port=port, username=username,password=password)
    # 获取SFTP实例
    sftp = ssh.open_sftp()
    # 执行上传动作
    sftp.put(localpath,remotepath)
    # get_data = 'python get_data.py'
    # ssh.exec_command(get_data)
    # 执行下载动作
    # sftp.get(remotepath, rename) 
    # 121服务器太慢 取消此下载方法改为scp下载
    # cmd = 'scp  data_v1.tar  root@39.103.149.57:/root/lkimg/' +name+ '.tar'
    # stdin, stdout, stderr = ssh.exec_command(cmd)
    # stdin.write("Y")  # 简单交互，输入 ‘Y’
    # out = stdout.readlines()
    # print("out")
    # 关闭服务器连接
    ssh.close()
    return '成功'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug='ture')