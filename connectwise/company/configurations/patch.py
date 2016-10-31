def patch_configuration(client, configuration_id, patches):
    """

    :param patches: List of patches in format [
    {"op": op, "path": path, "value": value},
    {"op": op, "path": path, "value": value}
    ]
    :return: requests Response
    """

    data = []

    data = patches
    print("Patching {} with Data: {}".format(configuration_id, data))
    return client._patch("/company/configurations/{}/".format(configuration_id), json=data)