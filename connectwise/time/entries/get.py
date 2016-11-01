def get_time_entries(client, db_rid=None, company_identifier=None, charge_to_id=None, charge_to_type=None, member_identifier=None, work_type_name=None, work_role_name=None,
                     billable_option_text=None,
                     added_to_note_description=None, added_to_note_internal_analysis=None, added_to_note_resolution=None, emailed_contact=None, emailed_cc=None,
                     entered_by=None, page_size=1000):
    conditionstring = ""

    if db_rid:
        conditionstring = client._add_condition(conditionstring, 'id', db_rid)
    if company_identifier:
        conditionstring = client._add_condition(conditionstring, 'company/identifier', company_identifier)
    if charge_to_id:
        conditionstring = client._add_condition(conditionstring, 'chargeToId', charge_to_id)
    if charge_to_type:
        conditionstring = client._add_condition(conditionstring, 'chargeToType', charge_to_type)
    if member_identifier:
        conditionstring = client._add_condition(conditionstring, 'member/identifier', member_identifier)
    if work_type_name:
        conditionstring = client._add_condition(conditionstring, 'workType/name', work_type_name)
    if work_role_name:
        conditionstring = client._add_condition(conditionstring, 'workRole/name', work_role_name)
    if billable_option_text:
        conditionstring = client._add_condition(conditionstring, 'billableOption', billable_option_text)
    if added_to_note_description is not None:
        conditionstring = client._add_condition(conditionstring, 'addToDetailDescriptionFlag', added_to_note_description)
    if added_to_note_internal_analysis is not None:
        conditionstring = client._add_condition(conditionstring, 'addToInternalAnalysisFlag', added_to_note_internal_analysis)
    if added_to_note_resolution is not None:
        conditionstring = client._add_condition(conditionstring, 'addToResolutionFlag', added_to_note_resolution)
    if emailed_contact is not None:
        conditionstring = client._add_condition(conditionstring, 'emailContactFlag', emailed_contact)
    if emailed_cc is not None:
        conditionstring = client._add_condition(conditionstring, 'emailCcFlag', emailed_cc)
    if entered_by:
        conditionstring = client._add_condition(conditionstring, 'enteredBy', entered_by)

    print(conditionstring)
    parameters = {
        "conditions": conditionstring,
        "pageSize": page_size

    }
    print(parameters)
    return client._get("/time/entries/", parameters=parameters)