# Docker Compose Yaml  

### Docker engine release 17.06.0+  
version: "3.3"  
### Configuration applied to each container  
services:  

## Portainer Container  
Configuration applied to each container  
* portainer:  

Port mapping  
* ports:  
`- '8000:8000' # Portainer port TCP`  
`- '9000:9000' # TCP port for todo`  

Persisitng data generated  
* volumes:  
`- '/var/run/docker.sock:/var/run/docker.sock'`  
`- 'portainer_data:/data'`  

Instructions for creating the container  
* image: portainer/portainer  

Names the container  
* container_name: portainer  

Container will always restart  
* restart: always  

## Jupyter Container  
Jupyter container file  
* datascience_tx2:  

Persisitng data generated  
* container_name: TX2-UofA-CUDA-GPU-Jupyter  

Instructions for creating the container  
* image: zapataai/datascience_tx2:latest  

Persisitng data generated  
* volumes:  
`- "./notebooks/:/home/zapataai/work"`  

Port mapping  
*ports:  
 `- 8888:8888 # Jupyter notebook service`  
    
Persisitng data generated  
* environment:  
`- RACK_ENV=UofA`  

Container will always restart  
* restart: always  

# Ouroboros Container  
Monitors all containers and updates to the latest image in resgistry.  
* ouroboros:  

Instructions for creating the container  
* container_name: Update_Container  
 
Persisitng data generated  
* volumes:  
`- '/var/run/docker.sock:/var/run/docker.sock'`  
    
Instructions for creating the container  
* image: pyouroboros/ouroboros  

Persisitng data generated  
* volumes:  
    portainer_data:  
    notebooks:  
