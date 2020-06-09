# UTX2

## Summary:
UTX2 is the Github repository made expressly to allow clients a publicly accessible internet address from which to download the client-side of the Violent software package.

******************************************************
### Heartbeat
The heartbeat is defined to POST every 20 seconds. The heartbeat includes the following information regarding the Jupyter container on the host

#### Explanation
- created - Date and time the container was created on the host
- ip - IP address the host is listening on
- jupyterToken - Token for authentication to the Jupyter notebook instance
- jupyterUrl - Full URL with token embedded for authentication to the Jupyter notebook
- last_update - Date and time the last heartbeat was received
- startedAt - Data and time the container was last rebooted
- status - Current status of the Jupyter container

#### Example POST for each Heartbeat
 ````
   0
   created	"2020-05-28T15:03:52.948930874Z"
   ip	"10.10.10.21"
   jupyterToken	"158d9b365bb4e5afca026e2165e65c1cd4f43125b5ee7855"
   jupyterUrl	"http://10.10.10.10:8888/?token=158d9b365bb4e5afca026e2165e65c1cd4f43125b5ee7855"
   last_update	"2020-05-29T19:58:00.155685"
   startedAt	"2020-05-29T16:46:37.69398368Z"
   status	"On"
````
## Docker Containers:
- Jupyter Notebook accessible on port:8888
- Ouroboros Update Server (updates the containers when a new :latest is posted to the registry)
- Portainer  accessible on port:9000

## Getting started
### Requirements
- certifi==2019.11.28
- chardet==3.0.4
- idna==2.8
- netifaces==0.10.9
- requests==2.22.0
- schedule==0.6.0
- urllib3==1.25.7

### Installing
Follow the installation instructions from Github Violent Python: https://github.com/FerrelBurn/violent/blob/master/README.md

## Running the tests TODO CG
<!--### Break down into end to end tests-->
<!--### And coding style tests-->
<!--## Deployment-->
<!--## Built With-->
<!--## Contributing -->
<!--## Versioning-->
<!--## Authors-->
## License
Apache.2.0
<!--## Acknowledgments-->
