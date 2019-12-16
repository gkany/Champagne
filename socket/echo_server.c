#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#include "error.h"

/*
void errorHandling(const char* msg) {
    fputs(msg, stderr);
    fputc('\n', stderr);
    exit(-1);
}
*/

int main(int argc, char* argv[]) {
    if(argc != 2) {
	printf("Usage: %s <port> \n", argv[1]);
	exit(-1);
    }

    //AF_INET 和 PF_INET都可以
    //int sockServ = socket(PF_INET, SOCK_STREAM, 0);
    int sockServ = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in sockServAddr;
    memset(&sockServAddr, 0, sizeof(sockServAddr));
    sockServAddr.sin_family = AF_INET;
    sockServAddr.sin_addr.s_addr = htonl(INADDR_ANY);
    sockServAddr.sin_port = htons(atoi(argv[1]));

    if(bind(sockServ, (struct sockaddr*)& sockServAddr, sizeof(sockServAddr)) == -1){ 
		errorHandling("bind() error");
    }

    if(listen(sockServ, 5) == -1) {
		errorHandling("listen() error");
    }    

	char buf[128];
	for(int i=0; i<5; i++) {
		int sockClient = accept(sockServ, 0, 0);
    	if(sockClient == -1) {
			errorHandling("accept() error");
   		 } else {
			puts("new client connected...");
    	}

		while(1) {
			memset(buf, 0, sizeof(buf));
			int readLen = read(sockClient, buf, sizeof(buf));
			if(readLen == 0) {
				puts("Client disconnected...");
				close(sockClient);
				break;
			} 
		
			//buf[readLen] = 0;
			printf("recv: %s", buf);	
			write(sockClient, buf, readLen);
			//memset(buf, 0, sizeof(buf));
		}
	}

    close(sockServ);

    return 0;
}







