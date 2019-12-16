# docker pull  
Dockerfile文件路径下执行：  
docker build -t ubuntu:16.04 .  


# docker run  
docker run --name ub -dit -v /Users/a123/data/docker/data:/root/data  ubuntu:16.04  
说明：  
     -v 目录映射  

# 进入  
docker exec -it ub bash  

