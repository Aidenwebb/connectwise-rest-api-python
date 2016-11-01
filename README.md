Python Client for Connectwise REST API
======================================

## Description

Use Python? This library brings the [Connectwise REST API] to your Python application.

The Python Client for Connectwise Rest API is a Python Client library for the following Connectwise REST API's
APIs:

 - [Company]
 - - [Companies]  - "GET" Development Started
 - - [CompanyManagementSummaryReports] - Development Yet Not Started
 - - [CompanyNotes] - Development Yet Not Started
 - - [CompanySites] - Development Yet Not Started
 - - [CompanyStatuses] - Development Yet Not Started
 - - [CompanyTeams] - Development Yet Not Started
 - - [CompanyTypes] - Development Yet Not Started
 - - [ConfigurationStatuses] - Development Yet Not Started
 - - [ConfigurationTypeQuestions] - Development Yet Not Started
 - - [ConfigurationTypes] - Development Yet Not Started
 - - [Configurations] - "GET" and "UPDATE Development Started
 - - [ContactCommunications]- Development Yet Not Started
 - - [ContactDepartments]- Development Yet Not Started
 - - [ContactNotes]- Development Yet Not Started
 - - [ContactRelationships]- Development Yet Not Started
 - - [ContactTracks] - Development Yet Not Started
 - - [ContactTypes] - Development Yet Not Started
 - - [Contacts] - "GET" Development Started
 - [Expense]
 - - [ExpenseEntries] - Development Yet Not Started
 - - [ExpenseTypes] - Development Yet Not Started
 - [Finance]
 - - [AccountingBatchTransactions] - Development Yet Not Started
 - - [AccountingBatches] - Development Yet Not Started
 - - [AccountingUnpostedExpenses] - Development Yet Not Started
 - - [AccountingUnpostedProcurements] - Development Yet Not Started
 - - [AccountingUnpostedInvoices] - Development Yet Not Started
 - - [AgreementAdditions] - Development Yet Not Started
 - - [AgreementAdjustments] - Development Yet Not Started
 - - [AgreementBoardDefaults] - Development Yet Not Started
 - - [AgreementSites] - Development Yet Not Started
 - - [AgreementTypes] - Development Yet Not Started
 - - [AgreementWorkRoleExclusions] - Development Yet Not Started
 - - [AgreementWorkRoles] - Development Yet Not Started
 - - [AgreementWorkTypeExclusions] - Development Yet Not Started
 - - [AgreementWorkTypes] - Development Yet Not Started
 - - [Agreements] - Development Yet Not Started
 - - [Currencies] - Development Yet Not Started
 - - [InvoicePayments] - Development Yet Not Started
 - - [Invoices] - Development Yet Not Started
 - - [TaxCodeXRefs] - Development Yet Not Started
 - - [TaxCodes] - Development Yet Not Started
 - [Marketing]
 - - [CampaignAudits] - Development Yet Not Started
 - - [CampaignEmailsOpened] - Development Yet Not Started
 - - [CampaignFormsSubmitted] - Development Yet Not Started
 - - [CampaignLinksClicked] - Development Yet Not Started
 - - [CampaignStatuses] - Development Yet Not Started
 - - [CampaignSubTypes] - Development Yet Not Started
 - - [CampaignTypes] - Development Yet Not Started
 - - [Campaigns] - Development Yet Not Started
 - - [GroupCompanies] - Development Yet Not Started
 - - [GroupContacts] - Development Yet Not Started
 - - [Groups] - Development Yet Not Started
 - [Procurement] - Development Yet Not Started
 - - [TODO: Complete Modules List]
 - [Project] - Development Yet Not Started
 - - [TODO: Complete Modules List]
 - [Sales] - Development Yet Not Started
 - - [TODO: Complete Modules List]
 - [Schedule] - Development Yet Not Started
 - - [TODO: Complete Modules List]
 - [Service]
 - - [TODO: Complete Modules List]
 - - [Tickets] - "CREATE" Development Started
 - [System] - Development Yet Not Started
 - - [TODO: Complete Modules List]
 - [Time] - Development Yet Not Started
 - - [TODO: Complete Modules List]

## Requirements

 - Python 2.7 or later.
 - A Connectwise API key or token.
 
 ## Installation

    $ pip install -U connectwise
    
## Usage

This example uses the [Companies][Contacts] API with an Auth key:

```python
import connectwise

cwclient = connectwise.Client('connectwisesubdomain.yourdomain.com', auth_token="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==")

# Retreiving a set of contacts
geocode_result = cwclient.company.contacts.get(first_name="userfirstname", company_identifier="CID")
```