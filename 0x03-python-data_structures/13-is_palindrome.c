#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t   *h = *head, *tmp = NULL;

    while (h)
    {
        h->prev = tmp;
        tmp = h;
        h = h->next;
    }
    h = *head;
    while (h)
    {
        if (h->n != tmp->n)
            return (0);
        h = h->next;
        tmp = tmp->prev;
    }
    return (1);
}
