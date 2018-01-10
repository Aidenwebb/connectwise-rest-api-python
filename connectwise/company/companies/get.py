def get_companies(client, db_rid=None, company_identifier=None, company_name=None, status=None, zip=None,
                  phone_number=None, fax_number=None, website=None, verbose=False):
    """
    Gets Companies with a particular set of optional conditions.

    :param client: Pass the authorised connectwise client object
    :type client: Object
    :param db_rid: Company ID
    :type db_rid: Integer
    :param company_identifier: Company Identifier.
    :type company_identifier: String
    :param company_name:
    :type company_name: String
    :param status:
    :type status: String
    :param zip:
    :type zip: String
    :param phone_number:
    :type phone_number: String
    :param fax_number:
    :type fax_number: String
    :param website:
    :type website: String
    :return: Requests object.

    return.json() - json response of the request.
    return.url - requested URL
    return.status_code - status code fo the request
    """


    conditionstring = ""
    if db_rid:
        conditionstring = client._add_condition(conditionstring, 'id', db_rid)
    if company_identifier:
        conditionstring = client._add_condition(conditionstring, 'identifier', company_identifier)
    if company_name:
        conditionstring = client._add_condition(conditionstring, 'name', company_name)
    if status:
        conditionstring = client._add_condition(conditionstring, 'status', status)
    if zip:
        conditionstring = client._add_condition(conditionstring, 'zip', zip)
    if phone_number:
        conditionstring = client._add_condition(conditionstring, 'phoneNumber', phone_number)
    if fax_number:
        conditionstring = client._add_condition(conditionstring, 'faxNumber', fax_number)
    if website:
        conditionstring = client._add_condition(conditionstring, 'website', website)
    if verbose is True: print(conditionstring)
    parameters = {
        "conditions": conditionstring
    }

    return client._get("/company/companies/", parameters=parameters)