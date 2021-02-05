#include <pthread.h>
#include <unistd.h>
#include <stdio.h>

static void *child(void *ignored) {
    while(1){
        sleep(5);
        printf("Child is done sleeping 5 second.\n");
    }
    return NULL;
}

int main() {
    pthread_t child_thread;
    int code;
    char enter;
    
    code = pthread_create(&child_thread, NULL, child, NULL);
    if(code){
        fprintf(stderr, "pthread_create failed with code %d\n", code);
    }
    printf("Press enter to kill child...\n");
    scanf("%c", &enter);
    pthread_cancel(code);
    printf("Parent killed child!\n");
    return 0;
}
  