#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#include "error.h"

/*
void errorHandling(const char* msg) {
	fputs(msg, stderr);
	fputc('\n', stderr);
	exit(1);
}
*/

int main(int argc, char* argv[]) {
	if(argc != 3) {
		printf("Usage: %s <ip> <port> \n", argv[0]);
		exit(1);
	}

	int sock = socket(PF_INET, SOCK_STREAM, 0);
	struct sockaddr_in sockAddr;
	memset(&sockAddr, 0, sizeof(sockAddr));
	sockAddr.sin_family = AF_INET;
	sockAddr.sin_addr.s_addr = inet_addr(argv[1]);
	sockAddr.sin_port = htons(atoi(argv[2]));

	if(connect(sock, (struct sockaddr*)&sockAddr, sizeof(sockAddr)) == -1) {
		errorHandling("connect() error");
	}

	char buf[128];
	while(1) {
		if(NULL == fgets(buf, sizeof(buf), stdin)) {
			errorHandling("fgets error");
		} else {
			if(0 == strcmp(buf, "Q\n") || 0 == strcmp(buf, "q\n")) {
				puts("client disconnected...");
				break;
			}
			write(sock, buf, sizeof(buf));
			int readLen = read(sock, buf, sizeof(sock));
			buf[readLen] = 0;
			printf("Message from server: %s", buf);

			memset(buf, 0, sizeof(buf));
		}
	}

	close(sock);

	return 0;
}

