def get_contacts(client, db_rid=None, first_name=None, last_name=None, company_identifier=None, zip=None, inactive=False):
    conditionstring = ""
    if db_rid:
        conditionstring = client._add_condition(conditionstring, 'id', db_rid)
    if first_name:
        conditionstring = client._add_condition(conditionstring, 'firstName', first_name)
    if last_name:
        conditionstring = client._add_condition(conditionstring, 'lastName', last_name)
    if company_identifier:
        conditionstring = client._add_condition(conditionstring, 'company/identifier', company_identifier)
    if zip:
        conditionstring = client._add_condition(conditionstring, 'zip', zip)

    conditionstring = client._add_condition(conditionstring, 'inactiveFlag', inactive)
    parameters = {
        "conditions": conditionstring
    }

    return client._get("/company/contacts/", parameters=parameters)