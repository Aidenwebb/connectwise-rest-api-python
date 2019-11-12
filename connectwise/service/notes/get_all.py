def get_service_ticket_notes(client, ticket_id, note_id=None, text=None, detail_description_flag=None,
                     internal_analysis_flag=None, resolution_flag=None, issue_flag=None,
                     member_name=None, member_identifier=None, contact_name=None,
                     customer_updated_flag=None, process_notifications=None, internal_flag=None,
                     external_flag=None, page_size=1000, verbose=False):
    conditionstring = ""

    if note_id:
        conditionstring = client._add_condition(conditionstring, 'id', note_id)
    if text:
        conditionstring = client._add_condition(conditionstring, 'text', text)
    if detail_description_flag:
        conditionstring = client._add_condition(conditionstring, 'detailDescriptionFlag', detail_description_flag)
    if internal_analysis_flag:
        conditionstring = client._add_condition(conditionstring, 'internalAnalysisFlag', internal_analysis_flag)
    if resolution_flag:
        conditionstring = client._add_condition(conditionstring, 'resolutionFlag', resolution_flag)
    if issue_flag:
        conditionstring = client._add_condition(conditionstring, 'issueFlag', issue_flag)
    if member_name:
        conditionstring = client._add_condition(conditionstring, 'member/name', member_name)
    if member_identifier:
        conditionstring = client._add_condition(conditionstring, 'member/identifier', member_identifier)
    if contact_name:
        conditionstring = client._add_condition(conditionstring, 'contact/name', contact_name)
    if customer_updated_flag:
        conditionstring = client._add_condition(conditionstring, 'customerUpdatedFlag', customer_updated_flag)
    if process_notifications:
        conditionstring = client._add_condition(conditionstring, 'processNotifications', process_notifications)
    if internal_flag:
        conditionstring = client._add_condition(conditionstring, 'internalFlag', internal_flag)
    if external_flag:
        conditionstring = client._add_condition(conditionstring, 'externalFlag', external_flag)

    if verbose is True:
        print(conditionstring)
    parameters = {
        "conditions": conditionstring,
        "pageSize": page_size

    }
    if verbose is True:
        print(parameters)
    return client._get("/service/tickets/{}/notes".format(ticket_id), parameters=parameters)
