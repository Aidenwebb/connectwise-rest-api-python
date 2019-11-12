def update_service_ticket_note(client, ticket_id, note_id, text=None, detail_description_flag=None,
                               internal_analysis_flag=None, resolution_flag=None, issue_flag=None,
                               member_name=None, member_identifier=None, contact_name=None,
                               customer_updated_flag=None, process_notifications=None, internal_flag=None,
                               external_flag=None, verbose=False):

    patchgroup = client.PatchGroup()
    if text:
        patchgroup.add("replace", "/text", text)
    if detail_description_flag:
        patchgroup.add("replace", "/detailDescriptionFlag", detail_description_flag)
    if internal_analysis_flag:
        patchgroup.add("replace", "/internalAnalysisFlag", internal_analysis_flag)
    if resolution_flag:
        patchgroup.add("replace", "/resolutionFlag", resolution_flag)
    if issue_flag:
        patchgroup.add("replace", "/issueFlag", issue_flag)
    if member_identifier:
        patchgroup.add("replace", "/member/identifier", member_identifier)
    if member_name:
        patchgroup.add("replace", "/member/name", member_name)
    if contact_name:
        patchgroup.add("replace", "/contact/name", contact_name)
    if customer_updated_flag:
        patchgroup.add("replace", "/customerUpdatedFlag", customer_updated_flag)
    if process_notifications:
        patchgroup.add("replace", "/processNotifications", process_notifications)
    if internal_flag:
        patchgroup.add("replace", "/internalFlag", internal_flag)
    if external_flag:
        patchgroup.add("replace", "/externalFlag", external_flag)

    data = patchgroup.patches
    if verbose is True:
        print(f"data = {data}")

    if verbose is True:
        print("Updating ticket {}".format(ticket_id))

    return client._patch('/service/tickets/{0}/notes/{1}'.format(ticket_id, note_id), json=data, verbose=verbose)
