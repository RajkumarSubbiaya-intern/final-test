L2 to Dev Team Process Guide
============================

This guide outlines the structured flow of issues/cases from the **L2 support team** to the **development team**, ensuring smooth handling, tracking, and resolution.

Issue/Cases Identification & Categorization
-------------------------------------------

L2 support receives issues/cases from L1, monitoring systems, Glory Team or directly from customer. L2 debugging begins with checking logs, assessing system health, and reviewing previous occurrences to identify patterns or recurring issues. If the problem aligns with known resolutions, L2 applies quick fixes such as restarting services, adjusting configurations, or updating database entries. However, if the issue requires code changes or deeper investigation, it is escalated to the development team. Before escalation, L2 ensures that all necessary details, including logs, steps to reproduce, and environmental information, are thoroughly documented in Azure tickets to facilitate efficient troubleshooting by the developers. 

Issue/Cases Analysis Guide Docs:
--------------------------------
- `Cases Handling Handbook - US.docx <https://gajanrapyutarobotics.sharepoint.com/:w:/r/sites/04_chennai/Shared%20Documents/01_onboarding/SB_Systems_Docs/Cases%20Handling%20Handbook%20-%20US.docx?d=w9e84adfb07b54685b59c98310bb4aba4&csf=1&web=1&e=ZqRm3q>`_
- `Issue Handling Handbook_v1.0.docx <https://gajanrapyutarobotics.sharepoint.com/:w:/r/sites/04_chennai/Shared%20Documents/01_onboarding/SB_Systems_Docs/Issue%20Handling%20Handbook_v1.0.docx?d=wf8e2d27a4a3b454db3bb7e5eb1edf67b&csf=1&web=1&e=oa9nAA>`_
- `U.S CASES CHECKLIST.docx <https://gajanrapyutarobotics.sharepoint.com/:w:/r/sites/04_chennai/Shared%20Documents/01_onboarding/SB_Systems_Docs/U.S%20CASES%20CHECKLIST.docx?d=wa5700ab88f77446fb40382d2d7438663&csf=1&web=1&e=Iq5tcO>`_

The issue/cases are then categorized into: 

- **Bugs -** Functional defects requiring code fixes. 
- **Feature Requests -** New functionalities requested by users or stakeholders. 
- **Improvements -** Configuration changes or optimizations to enhance velocity, productivity, or product stability. 

Issue/Case Routing & Documentation
----------------------------------

Each category follows a distinct workflow:

**Bugs (From Reporting to Completion)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When L2 identifies a bug, they log it in the tracking system (Azure) with a detailed issue description, steps to reproduce, relevant logs, screenshots, and environment details to ensure clarity for the development team. Once reported, the RTE evaluates its priority—categorizing it as critical, major, or minor—before scheduling it in an upcoming sprint based on its impact. Assigned developers then begin investigating and resolving the bug, ensuring the fix undergoes thorough peer review and testing before deployment. Once the fix is integrated into the release pipeline, L2 performs final validation to confirm that the issue is resolved before marking it as closed.

**Detailed Bug Management Process:** 
   - `How to create Bug ticket docs <https://gajanrapyutarobotics.sharepoint.com/:w:/s/04_chennai/EQswy4MsZqxKjchI1x9KbDgBtD4serf9jqcdqNX4NWdLNQ?e=qMmNen>`_


**Feature Requests**
~~~~~~~~~~~~~~~~~~~~
When L2 identifies the need for a new feature, they submit a feature request along with a justification and impact assessment, outlining how the enhancement would improve functionality or user experience. The Product Manager and RTE then review the request to evaluate its feasibility, alignment with business goals, and priority within the development roadmap. If approved, the feature request is added to the backlog and scheduled for implementation in an upcoming sprint, ensuring it is developed in a structured and timely manner. 

**Feature Request Workflow:** 
   - `How to create Feature request docs <https://gajanrapyutarobotics.sharepoint.com/:w:/s/04_chennai/ETpMGAUXEJtCkegojOtbd2sBlOYvHWEMGzlNHch0NlCkkQ?e=8RKtja>`_


**Improvements (Config Changes, Velocity/Productivity Enhancements)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

L2 identifies areas for improvement, such as system tuning, process automation, or optimizations that enhance performance and productivity. Once an improvement is proposed, the RTE or Product Manager reviews its feasibility, potential impact, and alignment with ongoing priorities. If approved, the implementation is assigned to either the DevOps team or the development team, ensuring that the necessary changes are executed efficiently to enhance system reliability and operational efficiency. 
