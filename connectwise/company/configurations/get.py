def get_configurations(client, type=None, name=None, company_identifier=None, db_rid=None, status="active"):
    conditionstring = ""
    if status:
        conditionstring = client._add_condition(conditionstring, 'status/name', status)
    if db_rid:
        conditionstring = client._add_condition(conditionstring, 'id', db_rid)
    if type:
        conditionstring = client._add_condition(conditionstring, 'type/name', type)
    if name:
        conditionstring = client._add_condition(conditionstring, 'name', name)
    if company_identifier:
        conditionstring = client._add_condition(conditionstring, 'company/identifier', company_identifier)

    print(conditionstring)
    parameters = {
        "conditions": conditionstring,
        "pageSize": 1000
    }
    print(parameters)
    return client._get("/company/configurations/", parameters=parameters)