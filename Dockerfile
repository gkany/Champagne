# Base image
FROM ubuntu:16.04

# MAINTAINER
MAINTAINER test

# node run env
RUN apt-get update 
RUN apt-get install autoconf cmake vim libbz2-dev libdb++-dev libdb-dev libssl-dev openssl libreadline-dev libtool libcurl4-openssl-dev libboost-all-dev -y

# port-can 
EXPOSE 8049
EXPOSE 8050
