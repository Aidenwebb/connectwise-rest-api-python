def patch_ticket(client, ticket_id, patches):
    """

    :param patches: List of patches in format [
    {"op": op, "path": path, "value": value},
    {"op": op, "path": path, "value": value}
    ]
    :return: requests Response
    """

    data = []

    data = patches
    print("Patching {} with Data: {}".format(ticket_id, data))
    return client._patch("/service/tickets/{}/".format(ticket_id), json=data)

def update_status(client, ticket_id, status_id):

    data = ["replace", "/status/id", status_id]

    return client._patch("/service/tickets/{}/".format(ticket_id), json=data)