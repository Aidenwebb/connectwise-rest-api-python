def get_boards(client, db_rid=None, board_name=None, page_size=1000):
    conditionstring = ""

    if db_rid:
        conditionstring = client._add_condition(conditionstring, 'id', db_rid)
    if board_name:
        conditionstring = client._add_condition(conditionstring, 'name', board_name)

    print(conditionstring)
    parameters = {
        "conditions": conditionstring,

    }
    print(parameters)
    return client._get("/service/boards/", parameters=parameters)