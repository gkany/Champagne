#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void errorHandling(const char* msg) {
	fputs(msg, stderr);
	fputc('\n', stderr);
	exit(1);
}

