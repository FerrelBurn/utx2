import subprocess
import requests
import socket
import netifaces as ni
import platform
import time
import schedule

token = None
ip = "10.10.10.1"
# rest_ip = "10.139.57.107"
rest_ip = "208.188.184.42"
status = None
heartbeat_frequency = 20


# checks to see if the Jupyter container is running
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
    print("jupyter container is running: ", is_running())
    if is_running():
        global token
        token = None
        # p = subprocess.getoutput('docker logs TX2-UofA-CUDA-GPU-Jupyter 2>&1 | grep token')
        p = subprocess.getoutput('docker exec -i TX2-UofA-CUDA-GPU-Jupyter jupyter notebook list')
        raw_token = ''.join(p)
        print("raw token: ", raw_token)
        if raw_token == "the input device is not a TTY":
            time.sleep(5)
            print("waiting 5 seconds to see if the docker container is up yet")
            get_token()

        start = 'token='
        end = ' ::'
        token = ((raw_token.split(start))[1].split(end)[0])

        print("Token: ", token)
    else:
        token = "None"


# post Jettson data to rest interface
def post_data():
    try:
        global status
        global rest_ip

        api_endpoint = "http://" + rest_ip + ":8008/submit"
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


        else:
            host_ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

        ip = host_ip
        print("TX2 IP: ", ip)
    except:
        print("Unable to get Hostname and IP")

    # Driver code


# calls the rest server to see if it needs to change the API endpoint
def update_rest_ip():
    print("update rest IP")
    global rest_ip
    global heartbeat_frequency
    api_url = "http://" + rest_ip + ":5000/endpoint"
    try:
        r = requests.get("http://" + rest_ip + ":5000/endpoint", timeout=10)
        print("response from update rest IP: ", r.json())
        data = r.json()
        print("data.ip: ", data['ip'])
        rest_ip = data['ip']
        heartbeat_frequency = data['heartbeatFreq']
        print("new REST_API IP: ", rest_ip)
        print("new freq: ", heartbeat_frequency)
    except:
        print("couldn't get an update for the IP or heartbeat frequency")


#     post to rest endpoint on a regular basis
def heart_beat():
    get_token()
    get_host_name_ip()
    post_data()
    update_rest_ip()


get_token()
get_host_name_ip()
post_data()
schedule.every(20).seconds.do(heart_beat)
while True:
    schedule.run_pending()
    time.sleep(1)
