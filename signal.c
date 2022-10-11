#include <stdio.h>
#include <signal.h>
#include <unistd.h>

int con = 0;

void trabajo(int sig){
    con = sig;
}

int main(){
    signal(10,trabajo);
    while(con != 10){
        printf("Estoy trabajando\n");
        sleep(1);
    }

    printf("Nunca llega\n");
    return 0;
}