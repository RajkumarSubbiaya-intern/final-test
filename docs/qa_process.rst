QA Process: Feature & Bug Validation
====================================

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Details

   qa
   ci_run

To ensure a structured and efficient QA process, the team needs better visibility into the workload beyond sync meetings. Establishing a clear process will help streamline testing, automate ticket creation, and integrate QA activities more effectively into planning and execution. :doc:`QA Process document in detail here <qa>`


Work Assignment & Ticket Creation 
---------------------------------

   - The **QA lead is informed of testing requirements** during the **SB-Dev sync meetings,** where development progress and pending work are discussed. 
   - Based on this, **QA tickets are created** for every development ticket (feature or bug). 
   - An **automated flow for QA ticket creation** is being developed (Assigned to Vasee). 
   - Documentation on **how to create QA tickets** is available here  

Testing Scope & Approach 
~~~~~~~~~~~~~~~~~~~~~~~~

QA activities occur at multiple stages: 

   - **Feature integration** testing. 
   - **Bug fix validation** for both minor fixes and critical issues. 
   - **Regression testing** for full releases (e.g., 3.3.1). 
   - **Daily CI/CD testing** during development cycles.  

The extent of automation depends on **timeline and workload:**

   - **Features** are **fully automated** to ensure long-term test coverage. 
   - **Bug fixes** are automated **only if time permits,** as they may be one-time validations. 


Execution & Reporting
~~~~~~~~~~~~~~~~~~~~~

   - **Testing is performed in simulation** first.  :red:`The setup is now ready; proceed with real-time validation testing.`
   - Upon completion, **QA updates the ticket status** to reflect test results. 
   - Findings and test coverage are **discussed in sprint planning and retrospectives** to ensure continuous improvement. 

Continuous Integration & Release Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - **Daily CI runs occur every evening,** covering all release branches and the development branch. 
   - **Nightly test runs (6.5 hours)** execute across all major branches. 
   - If a CI/CD test fails, it is **investigated—** either fixed immediately or temporarily skipped based on priority. 
   - Detailed documentation on  :doc:`how to initiate different types of CI runs for specific suites or nightly tests, confidence tests, or performance tests can be found here: <ci_run>`


Production Bug Testing & RCA 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - **All production bugs undergo RCA (Root Cause Analysis)** to prevent recurrence. 
   - RCA includes a **comparison between simulation and real-world behaviour** to identify discrepancies. 
   - If a test case gap is found to be the root cause, **new test cases are added** to the suite. 
   - A **review of production bug counts vs. RCA findings** ensures continuous improvement and refinement of test strategies. 










