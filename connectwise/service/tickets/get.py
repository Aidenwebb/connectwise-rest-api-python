def get_tickets(client, summary=None, status=None, record_type=None, company_identifier=None, db_rid=None):
    conditionstring = ""
    if db_rid:
        conditionstring = client._add_condition(conditionstring, 'id', db_rid)
    if summary:
        conditionstring = client._add_condition(conditionstring, 'summary', summary)
    if record_type:
        conditionstring = client._add_condition(conditionstring, 'recordType', record_type)
    if status:
        conditionstring = client._add_condition(conditionstring, 'status/name', status)
    if company_identifier:
        conditionstring = client._add_condition(conditionstring, 'company/identifier', company_identifier)
    parameters = {
        "conditions": conditionstring
    }

    return client._get("/service/tickets/", parameters=parameters)