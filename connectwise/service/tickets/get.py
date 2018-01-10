def get_tickets(client, db_rid=None, summary=None, record_type=None, board_name=None, status_name=None,
                project_name=None,
                phase_name=None, company_identifier=None, type=None, subtype=None, severity=None, impact=None,
                page_size=1000, verbose=False):
    conditionstring = ""

    if db_rid:
        conditionstring = client._add_condition(conditionstring, 'id', db_rid)
    if summary:
        conditionstring = client._add_condition(conditionstring, 'summary', summary)
    if record_type:
        conditionstring = client._add_condition(conditionstring, 'recordType', record_type)
    if board_name:
        conditionstring = client._add_condition(conditionstring, 'board/name', board_name)
    if status_name:
        conditionstring = client._add_condition(conditionstring, 'status/name', status_name)
    if project_name:
        conditionstring = client._add_condition(conditionstring, 'project/name', project_name)
    if phase_name:
        conditionstring = client._add_condition(conditionstring, 'phase/name', phase_name)
    if company_identifier:
        conditionstring = client._add_condition(conditionstring, 'company/identifier', company_identifier)
    if type:
        conditionstring = client._add_condition(conditionstring, 'type', type)
    if subtype:
        conditionstring = client._add_condition(conditionstring, 'subType', subtype)
    if severity:
        conditionstring = client._add_condition(conditionstring, 'severity', severity)
    if impact:
        conditionstring = client._add_condition(conditionstring, 'impact', impact)

    if verbose is True: print(conditionstring)
    parameters = {
        "conditions": conditionstring,
        "pageSize": page_size

    }
    if verbose is True: print(parameters)
    return client._get("/service/tickets/", parameters=parameters)