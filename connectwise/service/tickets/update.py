def patch_ticket(client, ticket_id, patches, verbose=False):
    """

    :param patches: List of patches in format [
    {"op": op, "path": path, "value": value},
    {"op": op, "path": path, "value": value}
    ]
    :return: requests Response
    """

    data = []

    data = patches
    return client._patch("/service/tickets/{}/".format(ticket_id), json=data, verbose=verbose)

def update_status(client, ticket_id, status_id, verbose=False):

    patchgroup = client.PatchGroup()
    patchgroup.add("replace", "/status/id", status_id)

    data = patchgroup.patches
    if verbose is True: print(f"data = {data}")

    if verbose is True: print("Updating ticket {} status to {}".format(ticket_id, status_id))
    return client._patch("/service/tickets/{}/".format(ticket_id), json=data, verbose=verbose)

def update_board(client, ticket_id, board_id, verbose=False):

    patchgroup = client.PatchGroup()
    # Patch to change ticket's board fails if any of the following don't exist on the target board.
    patchgroup.add("replace", "/status/name", "New")
    patchgroup.add("remove", "/type")
    patchgroup.add("remove", "/subType")
    patchgroup.add("remove", "/item")
    patchgroup.add("replace", "/board/id", board_id)

    data = patchgroup.patches
    if verbose is True: print(f"data = {data}")

    if verbose is True: print("Updating ticket {} board to {}".format(ticket_id, board_id))
    return client._patch("/service/tickets/{}/".format(ticket_id), json=data, verbose=verbose)

def update_company(client, ticket_id, status_id, verbose=False):

    patchgroup = client.PatchGroup()
    patchgroup.add("replace", "/status/id", status_id)

    data = patchgroup.patches
    if verbose is True: print(f"data = {data}")

    if verbose is True: print("Updating ticket {} status to {}".format(ticket_id, status_id))
    return client._patch("/service/tickets/{}/".format(ticket_id), json=data, verbose=verbose)