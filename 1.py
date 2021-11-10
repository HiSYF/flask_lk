import paramiko

def ssh_exec_command2(device_ip, username, password, command1, command2):
    port = 22
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(device_ip, port, username, password, timeout=5)

    print("连接设备 ", device_ip)
    channel = ssh_client.invoke_shell()
    stdin = channel.makefile("wb")
    stdout = channel.makefile("rb")

    stdin.write(
        f"""
{command1}
{command2}
exit
    """
    )
    print("执行完毕")
    output = stdout.read()
    print("读取完毕")
    ssh_client.close()
    return output