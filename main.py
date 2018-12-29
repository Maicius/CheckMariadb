# coding = utf-8
import subprocess
import time
import datetime

def check_exist():
    p = subprocess.Popen('lsof -i:3306', shell=True, stdout=subprocess.PIPE)
    out, err = p.communicate()
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'database is running')
    out_put = "".join(out.splitlines())
    if out_put.strip() == '':
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'database was closed')
        p = subprocess.Popen('systemctl start mariadb', shell=True, stdout=subprocess.PIPE)
        out, err = p.communicate()
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), out, err)
        time.sleep(10)


if __name__ == '__main__':
    while True:
        check_exist()
        time.sleep(1)
