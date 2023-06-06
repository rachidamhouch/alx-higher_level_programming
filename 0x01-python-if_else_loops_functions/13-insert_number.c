#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t   *h = *head, *tmp, *new;
    int         n;

    new = add_nodeint_end(head, number);
    if (!h)
        h = new;
    tmp = h;
    while (tmp->next)
    {
        if (tmp->n > tmp->next->n)
        {
            n = tmp->n;
            tmp->n = tmp->next->n;
            tmp->next->n = n;
            tmp = h;
            continue;
        }
        tmp = tmp->next;
    }
    return (new);
}
