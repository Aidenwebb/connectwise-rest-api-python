def get_boardstatuses(client, board_id, db_rid=None, status_name=None, page_size=1000):
    conditionstring = ""

    if db_rid:
        conditionstring = client._add_condition(conditionstring, 'id', db_rid)
    if status_name:
        conditionstring = client._add_condition(conditionstring, 'name', status_name)

    print(conditionstring)
    parameters = {
        "conditions": conditionstring

    }
    print(parameters)
    return client._get("/service/boards/{0}/statuses".format(board_id), parameters=parameters)