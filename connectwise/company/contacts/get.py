def get_contacts(client, first_name=None, last_name=None, company_identifier=None, db_rid=None):
    conditionstring = ""
    if db_rid:
        conditionstring = client._add_condition(conditionstring, 'id', db_rid)
    if first_name:
        conditionstring = client._add_condition(conditionstring, 'firstName', first_name)
    if last_name:
        conditionstring = client._add_condition(conditionstring, 'lastName', last_name)
    if company_identifier:
        conditionstring = client._add_condition(conditionstring, 'company/identifier', company_identifier)
    parameters = {
        "conditions": conditionstring
    }

    return client._get("/company/contacts/", parameters=parameters)