def get_companies(client, company_name=None, status=None, company_identifier=None, db_rid=None):
    conditionstring = ""
    if db_rid:
        conditionstring = client._add_condition(conditionstring, 'id', db_rid)
    if company_name:
        conditionstring = client._add_condition(conditionstring, 'name', company_name)
    if status:
        conditionstring = client._add_condition(conditionstring, 'status', status)
    if company_identifier:
        conditionstring = client._add_condition(conditionstring, 'identifier', company_identifier)
    print(conditionstring)
    parameters = {
        "conditions": conditionstring
    }

    return client._get("/company/companies/", parameters=parameters)