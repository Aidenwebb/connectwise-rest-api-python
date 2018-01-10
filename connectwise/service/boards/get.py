def get_boards(client, db_rid=None, board_name=None, page_size=1000, verbose=False):
    conditionstring = ""

    if db_rid:
        conditionstring = client._add_condition(conditionstring, 'id', db_rid, verbose)
    if board_name:
        conditionstring = client._add_condition(conditionstring, 'name', board_name, verbose)

    if verbose is True: print(conditionstring)
    parameters = {
        "conditions": conditionstring,

    }
    if verbose is True: print(parameters)
    return client._get("/service/boards/", parameters=parameters)
