def create_service_ticket_note(client, ticket_id, text=None, detail_description_flag=None,
                               internal_analysis_flag=None, resolution_flag=None, issue_flag=None,
                               member_name=None, member_identifier=None, contact_name=None,
                               customer_updated_flag=None, process_notifications=None, internal_flag=None,
                               external_flag=None, verbose=False):

    # One of detail_description_flag, internal_analysis_flag, and resolution_flag must be present

    original = {

        "text": text,
        "detailDescriptionFlag": detail_description_flag,
        "internalAnalysisFlag": internal_analysis_flag,
        "resolutionFlag": resolution_flag,
        "issueFlag": issue_flag,
        "member": {
            "identifier": member_identifier,
            "name": member_name,
        },
        "contact": {
            "name": contact_name,
        },
        "customerUpdatedFlag": customer_updated_flag,
        "processNotifications": process_notifications,
        "internalFlag": internal_flag,
        "externalFlag": external_flag,
    }

    data = {k: v for k, v in original.items() if v is not None}

    if verbose is True:
        print(data)

    return client._post('/service/tickets/{}/notes'.format(ticket_id), json=data)
