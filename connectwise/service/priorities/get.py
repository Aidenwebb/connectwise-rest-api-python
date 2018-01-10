def get_priorities(client, db_rid=None, priority_name=None, page_size=1000, verbose=False):
    conditionstring = ""

    if db_rid:
        conditionstring = client._add_condition(conditionstring, 'id', db_rid, verbose)
    if priority_name:
        conditionstring = client._add_condition(conditionstring, 'name', priority_name, verbose)

    if verbose is True: print(conditionstring)
    parameters = {
        "conditions": conditionstring

    }
    if verbose is True: print(parameters)
    return client._get("/service/priorities/", parameters=parameters)