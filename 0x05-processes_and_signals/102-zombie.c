#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * main - zombies
 *
 * Description: create five zombies
 * Return: 0 for success
 */
int main(void)
{
    int i;
    pid_t pidme;

    for (i = 0; i < 5; i++)
    {
        pidme = fork();

        if (pidme < 0)
        {
            perror("fork");
            exit(EXIT_FAILURE);
        }
        else if (pidme == 0)
        {
            // Child process
            exit(0);
        }
        else
        {
            // Parent process
            printf("Zombie process created, PID: %i\n", pidme);
        }
    }

    // The parent process sleeps for a while to allow the zombies to remain
    // in the system before being reaped.
    sleep(100);

    // The parent process should now reap the zombies.
    for (i = 0; i < 5; i++)
    {
        int status;
        pid_t zombie_pid = wait(&status);
        printf("Zombie process %i reaped, exit status: %d\n", zombie_pid, WEXITSTATUS(status));
    }

    return (0);
}
