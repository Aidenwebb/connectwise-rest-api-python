def get_configurations(client, db_rid=None, name=None, type_name=None, status="active", company_identifier=None, serial_number=None, verbose=False):
    """

    :param client: Pass the authorised connectwise client object
    :type client: Object
    :param db_rid: Configuration ID
    :type db_rid: Integer
    :param name: Configuration Name
    :type name: String
    :param type_name: Configuration Type. E.G. "Printer" or "Access Point"
    :type type_name: String
    :param status: Name of the Status of the configuration. E.G. "Active" or "Inactive"
    :type status: String
    :param company_identifier: Company Identifier under which the configuration is registered
    :type company_identifier: String
    :param serial_number: Serial number of the configuration
    :type serial_number: String
    :return: Requests object.

    return.json() - json response of the request.
    return.url - requested URL
    return.status_code - status code fo the request
    """


    conditionstring = ""

    if db_rid:
        conditionstring = client._add_condition(conditionstring, 'id', db_rid)
    if name:
        conditionstring = client._add_condition(conditionstring, 'name', name)
    if type_name:
        conditionstring = client._add_condition(conditionstring, 'type/name', type_name)
    if status:
        conditionstring = client._add_condition(conditionstring, 'status/name', status)
    if company_identifier:
        conditionstring = client._add_condition(conditionstring, 'company/identifier', company_identifier)
    if serial_number:
        conditionstring = client._add_condition(conditionstring, 'serialNumber', serial_number)

    if verbose is True: print(conditionstring)
    parameters = {
        "conditions": conditionstring,
        "pageSize": 1000
    }
    if verbose is True: print(parameters)
    return client._get("/company/configurations/", parameters=parameters)