#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t   *h = *head, *tmp = NULL;
    int         i = 0, n = 0;

    while (h)
    {
        h->prev = tmp;
        tmp = h;
        h = h->next;
        i++;
    }
    h = *head;
    while (n < i / 2)
    {
        if (h->n != tmp->n)
            return (0);
        h = h->next;
        tmp = tmp->prev;
        n++;
    }
    return (1);
}
