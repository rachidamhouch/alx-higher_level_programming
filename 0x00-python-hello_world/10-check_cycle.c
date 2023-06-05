#include "lists.h"

/**
 * check_cycle - check is cycle
 * @list: arg 1.
 * Return: 1 or 0.
 */
int check_cycle(listint_t *list)
{
	int n = 0, i;
	listint_t *head = list, *tmp;

	while (list)
	{
		i = 0;
		tmp = head;
		while (i < n)
		{
			if (list == tmp)
				return (1);
			i++;
			tmp = tmp->next;
		}
		list = list->next;
		n++;
	}
	return (0);
}
