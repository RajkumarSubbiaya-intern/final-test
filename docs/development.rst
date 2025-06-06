
Development Process: 
=====================

1. Handling Bugs Efficiently
----------------------------

The development process for handling bugs follows a structured workflow:

Task Assignment & Ownership
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Bugs are assigned to developers through Azure tickets, typically by the Scrum team. While senior developers may sometimes assign tasks, this should ideally be avoided to maintain a standardized process. Once a bug is assigned, the developer must change the work item status to "In Progress" to indicate active development. 

Identifying & Reproducing the Bug
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Before making any changes, the first step is to understand and reproduce the issue: 
   - Identify the **affected release version** and check out the corresponding branch in the repository. 
   - Follow the documented steps to reproduce the issue in **simulation or a test environment** (see : Bug Reproduction Guide – Inprogress for details). 
   - If reproduction is successful, create a new feature branch for the fix. 


Bug Fixing & Code Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the bug is confirmed and the relevant code section is identified: 

   - Locate the faulty code and implement the necessary fix. 
   - **Create a Pull Request (PR)** for code review (How to Create a PR – InProgress). 
   - Assign appropriate reviewers and keep the PR open for feedback. 
   - Address any review comments and continue refining the fix **until code owners approve the PR.** 

Merging & Backporting
~~~~~~~~~~~~~~~~~~~~~~~~~

Once the PR is approved: 

   - The fix is merged into the main branch. 
   - Backporting is performed if the fix is required in multiple versions. 
   - The **Azure ticket status is updated to "Merged."** 


Testing & Validation
~~~~~~~~~~~~~~~~~~~~~~~~

   - The **Scrum Master updates the ticket status to "Ready to Test."**
   - QA and L2 validate the fix in a controlled environment. 
   - If any issues arise during testing, the status changes to "Blocked", requiring the developer to revisit the fix and restart the cycle. 



2. Handling Features
---------------------

The process for handling feature development closely follows the bug-fixing workflow, with additional steps to accommodate design and stakeholder approvals. 

Task Assignment & Understanding Requirements 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Feature development begins with the creation of a feature ticket in Azure (How to Create a Feature Ticket -Inprogress). The Product Manager (PdM) assigns tasks to developers, ensuring alignment with business goals and priorities. Developers must first thoroughly review the feature documentation to understand the scope and expected outcome. 

Design & Collaboration 
~~~~~~~~~~~~~~~~~~~~~~

   - A **Figma design** is created to visualize the feature. 
   - The design is shared in **#design** for review and feedback. 
   - Once reviewed and approved, implementation begins. 

Development & Code Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - A **new branch** is created for development. 
   - Code is added and iteratively refined. 
   - A **Pull Request (PR)** is created and opened for reviewers (How to Create a PR-Inprogress). 
   - Reviewers provide feedback, and the **loop continues until code owners approve the PR.**


Testing & Validation 
~~~~~~~~~~~~~~~~~~~~

   - Once approved, the **QA team tests the PR** under **"QA Testing"** status. 
   - The feature remains in this state until testing is completed without issues. 
   - If no issues arise, the **PR is merged,** and backporting occurs if necessary. 
   - The **Azure ticket status is updated to "Merged."** 
   - The **Scrum Master changes the status to "Ready to Test."**

Handling Issues 
~~~~~~~~~~~~~~~

   - If an issue is found during testing, the status is changed to **"Blocked."** 
   - At this point, the feature effectively becomes a **bug**, and the **bug-fixing process begins**, looping back to reproduction, fixing, review, and testing. 

