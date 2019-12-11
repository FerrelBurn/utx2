import subprocess
import requests
import socket
import netifaces as ni
import platform
import time
import schedule
token = None
ip = "10.10.10.1"
status = None


def is_running():
    global status
    p = subprocess.getoutput("docker inspect -f '{{.State.Running}}' TX2-UofA-CUDA-GPU-Jupyter")

    if p == 'true':
        status = "On"
        return True
    else:
        status = "Off"
        return False


# get the jupyter notbook token
def get_token():
    print("jupyter container is running method call: ", is_running())
    if is_running():
        global token
        token = None
        # p = subprocess.getoutput('docker logs TX2-UofA-CUDA-GPU-Jupyter 2>&1 | grep token')
        p = subprocess.getoutput('docker exec -it TX2-UofA-CUDA-GPU-Jupyter jupyter notebook list')
        raw_token = ''.join(p)

        print("raw token: ", raw_token)

        start = 'token='
        end = ' ::'
        token = ((raw_token.split(start))[1].split(end)[0])

        print("Token: ", token)
    else:
        token = None


# post Jettson data to rest interface
def post_data():
    try:
        global status
        print("trying to post data to rest endpoint")
        api_endpoint = "http://208.188.184.42:5000/submit"
        print("trying to post data to rest endpoint:", api_endpoint)
        data = {'ip': ip, 'jupyterToken': token, 'status': status}

        r = requests.post(url=api_endpoint, json=data, timeout=10)

        # extracting response text
        print("response: ", r)

        return "done"
    except requests.exceptions.RequestException as e:
        print("Unable to post data", e)


# Function to display hostname and
# IP address
def get_host_name_ip():
    try:
        global ip
        host_ip = ""
        host_name = socket.gethostname()
        os = platform.system()
        if os == "Windows":
            host_ip = socket.gethostbyname(host_name)
            print(platform.system())
            print("windows IP:", host_ip)

        else:
            host_ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
            print("Hostname :  ", host_name)
            print("IP : ", host_ip)

        ip = host_ip
        print("final ip: ", ip)
    except:
        print("Unable to get Hostname and IP")

    # Driver code


#     post to rest endpoint on a regular basis
def heart_beat():
    get_token()
    get_host_name_ip()
    post_data()


get_token()
get_host_name_ip()
post_data()
schedule.every(20).seconds.do(heart_beat)
while True:
    schedule.run_pending()
    time.sleep(1)
