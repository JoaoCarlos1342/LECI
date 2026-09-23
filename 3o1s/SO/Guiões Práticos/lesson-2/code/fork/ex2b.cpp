#include <stdio.h>
#include <unistd.h>
#include "process.h"

void print_line() {
    for(int i = 0; i < 40; i++) {
        printf("=");
    }
    printf("\n");
}

int main(void) {
    // O pai imprime a linha superior antes de criar o filho
    print_line();

    pid_t ret = pfork();

    if (ret == 0) {
        // Processo filho: executa o comando ls -l
        execlp("ls", "ls", "-l", NULL);
        
        // Esta linha só é executada se o execlp falhar
        perror("Erro ao executar ls");
        return 1;
    } else {
        // Processo pai: espera que o filho termine
        pwait(NULL);
        
        // O pai imprime a linha inferior
        print_line();
    }

    return 0;
}