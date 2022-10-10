import paramiko


class SimplePythonLogin:

    hostName = "cis-linux2.temple.edu"
    # TODO enter your temple username
    userName = "tuj45886"
    # TODO enter your temple password -- please delete before committing !!!
    password = ""

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostName, username=userName, password=password)

    _stdin, _stdout, _stderr = ssh.exec_command("ls")
    print(_stdout.read().decode())
    ssh.close()





    # we can navigate to and then execute a bash file that already exists in the linux server from here that contains
    # needed commands
    #
    # we can also just run the needed commands line by line from a file locally


    # reading commands from a file
    # commandFile = open('Linux_excution_commands', 'r')
    # command = commandFile.readline()
    # i = 0
    # print("Line{}: {}".format(i, command))

