def get_service_ticket_note(client, ticket_id, note_id, page_size=1000, verbose=False):

    parameters = {
        "pageSize": page_size

    }
    if verbose is True:
        print(parameters)
    return client._get("/service/tickets/{0}/notes/{1}".format(ticket_id, note_id),
                       parameters=parameters)
