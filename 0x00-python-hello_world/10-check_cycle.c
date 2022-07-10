#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list, *temp = list;

	while (current != NULL && temp != NULL && temp->next != NULL)
	{
		current = current->next;
		temp = temp->next->next;
		if (current == temp)
			return (1);
	}
	return (0);
}
