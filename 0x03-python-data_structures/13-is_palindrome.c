#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t   *h = *head, *tmp;
    int         i = 0, len = 0, n;
    while (h)
    {
        h = h->next;
        len++;
    }
    h = *head;
    while (i < len / 2)
    {
        tmp = h;
        n = i;
        while (1)
        {
            n++;
            if (n >= len - i)
                break;
            tmp = tmp->next;
        }
        if (h->n != tmp->n)
            return (0);
        i++;
        h = h->next;
    }
    return (1);
}
