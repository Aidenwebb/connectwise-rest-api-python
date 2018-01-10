def create_new_ticket(client, summary, company_identifier, contact_name=None, ticket_type=None, sub_type=None,
                      service_item=None, initial_description=None, verbose=False):
    data = {
        "summary": summary,
        "company": {"identifier": company_identifier}
    }
    if contact_name:
        data['contact'] = {}
        data['contact']['id'] = client._get_contact_id(contact_name, company_identifier)
    if ticket_type:
        data['type'] = {}
        data['type']['name'] = ticket_type
    if sub_type:
        data['subType'] = {}
        data['subType']['name'] = sub_type
    if service_item:
        data['item'] = {}
        data['item']['name'] = service_item
    if initial_description:
        data['initialDescription'] = initial_description

    if verbose is True: print(data)

    return client._post('/service/tickets/', json=data)