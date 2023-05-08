#include "lists.h"

/**
 * check_cycle - checks if a linked lit consist of a cycle
 * @list: linked lst to check
 *
 * @list: pointer ti the start of the node
 * Return: 1 if the lst has a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	check = current->next;

	while (current != NULL && check->next != NULL
	      &&check->next->next->next;

	{
		if (current == check)
		      return (1);
		current = current->next;
		check = check->next->next;

	}
	return (0);
}	      
