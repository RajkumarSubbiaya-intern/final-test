DI Development Process 
=======================
.. contents:: Index
   :depth: 4
   :local:

.. _motivation_section:

1. Motivation
--------------
To have a quick onboarding process to the DI development process for newcomers to minimize the time to start contributing.

.. _setup_section:

2. Setup
---------

.. _setup_installation_tools_libs:

2.1 Installation Tools & Libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ensure the following tools and libraries are installed:

- VS Code
- Extensions:
    - Docker
    - C++ Extension pack

.. _tech_stack_section:

Tech stack
~~~~~~~~~~
- C++ STL
- GTest
- Catkin
- Alica

.. _setup_required_permissions:

2.2 Required Permissions
~~~~~~~~~~~~~~~~~~~~~~~~
You must have access to the following platforms:

- Azure
- GitHub Engineering
- Quay.io
- ReadTheDocs
- GitHub Enterprise Copilot (nice to have, ask for permission on slack/#it-admin)

.. _setup_cloning_procedure:

2.3 Cloning Procedure
~~~~~~~~~~~~~~~~~~~~~
- Generate a new SSH key.
- Add the SSH key to your system.
- Clone the repository using the SSH link:

  ::

    git clone <ssh_link>

.. _setup_repositories_to_clone:

2.4 Repositories to Clone
~~~~~~~~~~~~~~~~~~~~~~~~~
- rr_io_amr
- rr_sootballs

.. _setup_installations:

2.5 Installations
~~~~~~~~~~~~~~~~~
This guide assumes you've already installed ROS and set up your catkin workspace.

.. _useful_tools_section:

3. Useful tools to have in place before starting
-------------------------------------------------

.. _useful_tools_aliases:

3.1 Aliases
~~~~~~~~~~~
Aliases are text substitutions in linux. Whenever you want a string to be replaced by a larger text (usually a command or multiple commands), you can add an alias to your `.bashrc` and source it (`.bashrc` also gets sourced automatically whenever you open a new terminal window).

Some useful aliases:
::

    alias gitpp='git pull; git submodule sync; git submodule update --init --recursive; git submodule foreach git lfs pull'
    alias gittree='git log --all --decorate --oneline --graph'

.. _useful_tools_cli_highlighting:

3.2 CLI highlighting
~~~~~~~~~~~~~~~~~~~~
This is a minor one but useful to know which branch you’re working on at any given point in time. Add to your `.bashrc` anywhere outside a block as such:
::

    parse_git_branch() { git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/' }
    export PS1="\u@\h [\e[32m]\w [\e[91m]\$(parse_git_branch)[\e[00m]\$ "

.. _useful_tools_dev_containers:

3.3 Dev containers
~~~~~~~~~~~~~~~~~~
Dev containers are super helpful as they come prebuilt with all external dependencies used by `rr_io_amr` and by extension, `rr_sootballs`.

.. _dev_containers_concept:

3.3.1 Concept of building a container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A container is simply an environment to isolate processes with all the files they need to run. For example, if you install python on your local system, your python interpreter will point to the location where python was installed. However, if you run the python interpreter on a container, it points to a location within the container.

The reason these two are different is because a container has its own isolated filesystem.

To expose selected files on your computer to the environment of a container, you can mount it through CLI or a docker compose file.

.. _dev_containers_building:

3.3.1.1 Building the container
""""""""""""""""""""""""""""""
Containers can be built using `.Dockerfile`s. These define all the requirements that must be present in your container for development.

Once defined, they can be built and tagged locally using:
::

    docker build . -f <.Dockerfile path> -t <tag>

at the root (`.`) of the filesystem being used to build them. This can also be done automatically using docker-compose, which is how we’ll be doing it for dev purposes.

.. _dev_containers_running:

3.3.1.2 Running the container
"""""""""""""""""""""""""""""
Docker compose files are `.yaml` files containing instructions on what to do with the container once built. For our purposes, we can use them to install dependencies that need to be installed at runtime and mount our workspaces.

.. _dev_containers_setting_up:

3.3.2 Setting up your own dev container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Everyone generally builds and stores their dev container setup at `rapyuta-robotics:rr_amr_dev_tools`. Feel free to pick up any of them, load them into a new directory on your system at `~/catkin_ws/.devcontainer`.

This directory should have a Dockerfile inheriting from an IO_AMR_BASE image, `docker-compose.yaml`, and a shell script to install dependencies into the container at runtime.

**Dockerfile Example:**
::

    ARG IO_AMR_BASE=v0.20
    FROM quay.io/rapyuta/io_amr_base:${IO_AMR_BASE}
    ENV WORKSPACES=/home/rr/rr_ws
    WORKDIR ${WORKSPACES}
    USER rr
    ARG CC='/usr/lib/ccache/gcc'
    ARG CXX='/usr/lib/ccache/g++'
    RUN mkdir src
    # Build set-up
    RUN catkin init && \
        catkin config --no-install --extend /opt/ros/noetic --cmake-args -DCMAKE_BUILD_TYPE=Debug
    USER root
    RUN apt-get -qq update -y && \
        apt-fast -qq install -y --no-install-recommends ccache emacs-nox xterm
    RUN rm /etc/ros/rosdep/sources.list.d/20-default.list
    RUN rosdep init
    USER rr
    RUN pip uninstall -y virtualenv
    RUN pip install pip --upgrade
    RUN pip install pyopenssl --upgrade
    RUN curl -fsSL https://get.docker.com | sh

**docker-compose.yaml Example:**
::

    services:
      sb-devcontainer:
        build: .
        volumes:
          # Mounts files from host system to container. Changes made to the files are reflected on both systems
          # HOSTPATH:CONTAINERPATH
          - /home/$USER/rr_ws:/home/rr/rr_ws
          # Used for GUI applications
          - /tmp/.X11-unix:/tmp/.X11-unix
          # Used to forward SSH agent to container, for example to use GIT
          - $SSH_AUTH_SOCK:/ssh-agent
          # Used to forward gitconfig, for example username and email
          - /home/$USER/.gitconfig:/etc/gitconfig
          - /var/run/docker.sock:/var/run/docker.sock
          # Forward custom bash extension
          - /home/$USER/rr_ws/.devcontainer/.bash_aliases:/home/rr/.bash_aliases
          - /home/$USER/.cli-tools:/home/rr/.cli-tools
          - /home/$USER/Downloads:/home/rr/Downloads
        tty: true
        stdin_open: true
        container_name: "sb-devcontainer"
        # Used to keep container alive
        command: tail -f /dev/null
        network_mode: "host"
        environment:
          DISPLAY: $DISPLAY
          SSH_AUTH_SOCK: /ssh-agent
          IO_AMR_BASE: ${IO_AMR_BASE:-v0.20}

After this, you can start up your container with:
::

    docker compose build
    docker compose up -d
    docker start sb-devcontainer

And connect to it through VSCode.

.. _development_process_section:

4. Development process
-----------------------
We follow an Agile framework for this process. This means that we will have a sprint planning in the beginning of every two week sprint. Here, we decide the priority bugs and feature tasks for the sprint based on the priority for the next release. These tasks will be your sole priority for the next two weeks. The only thing that supersedes this is an active unresolved customer issue that you are on call for.

.. _development_process_rca:

4.0 RCA
~~~~~~~
Before starting off with bugs, here's a note on RCAs. This will help you identify where a change may be necessary in the code. An additional bit of context that helps a lot for this is if you have run all the flows on the robot yourself and generally familiarized yourself with what a functioning system is supposed to look like.

Issue tickets linked to the bugs in question generally have slack threads tracking them along with rosbags and links to Grafana pages pointing to the problem area in the system. Traces are also pretty helpful here, as they may give you information on the state of certain attributes at different points in the functioning of the system.

1. First, identify what happened that was not an expected behaviour of the system. This is usually what is reported first by the customer or field engineers in the issue ticket.

2. If L2 support has identified an unexpected behaviour on the backend that led to the issue visible to the customer/field engineers, then we can start the investigation from there to save some time.

3. Start asking why each event happened. For example, if an order upload failed on the system UI, ask why it happened. To answer this, go to the WMS IF logs. You will see a python exception. This is the answer to your first why. Now ask why this happened. Continuing from the last example, you can check the script that errored out and look it up on RR’s GitHub. A python error will tell you exactly which line threw the exception so you probably already found the bug by this stage. In DI, you’ll be debugging CPP code so rely on Logs and Traces to find out when a function call took place. Using GDB is also an option here if it’s easier to reproduce the issue.

4. In rare cases, your node may have died due to a memory fault. This will require you to reproduce the issue on your devcontainer by launching that node under those conditions to understand what caused the death or by analyzing the core dump on gdb.

5. Patch the bug once you’ve found it. You'll have to rely on your knowledge of OOP, inheritance and smart pointers to know what data you can access to patch it.

.. _development_process_bugs:

4.1 Bugs
~~~~~~~~
.. _bugs_get_ticket:

4.1.1 Get the Ticket (Bugs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Retrieve the Azure Ticket:
    - Obtain the bug ticket from the QA team, customer site, or Scrum Master.
    - Review the work item thoroughly to understand the details of the issue.
- Review the Work Item:
    - Study the provided reproduction steps to ensure they are clear and complete.
    - Identify any edge cases or ambiguities, and add comments or questions to the ticket to clarify.
    - Ensure you understand the priority and impact of the bug.

.. _bugs_reproduce_bug:

4.1.2 Reproduce the Bug (Bugs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Identify the Bug Type:
    - Determine if the issue is related to a specific ROS node, package, or C++ library.
- Verify the Release Version:
    - Confirm which release version or ROS distribution the bug is associated with, and ensure you're testing in the correct environment.
- Reproduce the Bug:
    - Follow the reproduction steps outlined in the work item to verify the bug.
    - Document any additional information or observations you encounter during reproduction.

.. _bugs_repository_setup:

4.1.3 Repository Setup (Bugs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Identify the Relevant Package/Repository:
    - Identify the ROS package or repository that contains the code relevant to the fix.
- Create a New Branch for Development:
    - Pull the latest changes from the repository to ensure you're working with the most recent code.
    - Create and switch to a new branch for the bug fix.

.. _bugs_implementation:

4.1.4 Implementation (Bugs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Apply the Fix:
    - Implement the necessary code changes to resolve the bug. Ensure that the fix addresses the issue without introducing new problems.
- Seek Guidance if Blocked:
    - If you encounter difficulties, seek assistance from your mentor, fellow developers, or the QA team to resolve blockers.

.. _bugs_testing:

4.1.5 Testing (Bugs)
^^^^^^^^^^^^^^^^^^^^
- Verify the Fix:
    - Test the changes locally to ensure the bug is resolved and the system behaves as expected.
    - Ensure that no existing functionality is broken due to your changes.
- Run Unit Tests Using GTest:
    - If there are existing GTest unit tests for the package, run them to confirm that no existing tests are failing.
- Add or Modify Unit Tests:
    - If no GTest tests currently cover the bug, add new unit tests or modify existing ones to test the fix.
    - Run the unit tests again to ensure your changes are validated.

.. _bugs_raising_pr:

4.1.6 Raising a Pull Request (PR) (Bugs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Add the Modified Files:
    - Add the files that were changed.
- Commit the Changes:
    - Commit your changes with a clear, meaningful message that follows conventional commit standards.
- Push the Changes:
    - Push the changes to the remote repository.
- Create a Pull Request (PR):
    - In GitHub or GitLab, create a new pull request.
    - Include a description of the changes you’ve made and reference the Azure task ID using the task number.
- Request Reviews:
    - Request reviews from the relevant code reviewers.

.. _bugs_code_review:

4.1.7 Code Review & Revisions (Bugs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Address Review Comments:
    - Address any feedback from the code reviewers by making the necessary revisions to the code.
- Push Changes After Revisions:
    - Once you've made the revisions, push the updated changes to the remote repository.
- Ensure Approval:
    - Repeat the review process until the pull request is approved.

.. _bugs_qa_testing:

4.1.8 QA Testing (Bugs)
^^^^^^^^^^^^^^^^^^^^^^^
- Request QA Testing:
    - If the fix is for a major feature, request QA to test the pull request in the relevant environment.
- Provide Image/Tag for Testing (if applicable):
    - Share any necessary Docker image tags, container registry information, or ROS workspace details for QA testing.
- Fix Bugs Reported by QA:
    - If QA reports additional bugs or regressions, fix them and request another round of code review.
- QA Signoff:
    - Once QA is satisfied with the changes, request their final sign-off on the feature.

.. _bugs_merging_backporting:

4.1.9 Merging & Backporting (Bugs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Merge the Changes:
    - Once the pull request is approved, merge the changes into the required branch (e.g., main, develop, etc.).
- Backport the Changes if Necessary:
    - If the fix needs to be applied to previous versions of the code, add the necessary backport labels to the PR.
- Resolve Merge Conflicts:
    - If there are any merge conflicts, resolve them manually or using the backport library.
- Merge the Backport PRs:
    - Once the backport PRs are approved, merge them into the corresponding branches.

.. _development_process_features:

4.2 Features
~~~~~~~~~~~~

.. _features_prepare_design_doc:

4.2.1 Prepare a Design Document
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Understand the Requirements:
    - Review the feature requirements from the Azure task, QA team, or product owner.
    - Clarify any ambiguities or edge cases and discuss with the relevant stakeholders if necessary.
- Outline the Design:
    - Provide a detailed design for the feature, ensuring it addresses all required aspects and edge cases.
    - Include diagrams or flowcharts where applicable to clearly represent how the feature will integrate with the existing system.
- Review and Approve Design:
    - Once the design document is ready, share it with the development team, product owner, and QA to ensure everyone is aligned.
    - Make any necessary revisions based on feedback before proceeding with the implementation.

.. _features_boilerplate_objects:

4.2.2 Put Down a Boilerplate of Objects and Data Structures Needed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Define the Objects and Structures:
    - Based on the design document, define the necessary C++ objects and data structures required for the feature.
    - Ensure the design and structure are modular and maintainable.
- Set Up the Boilerplate Code:
    - Create the header and source files for each object, ensuring proper organization of the code.
    - If using existing structures, ensure they are updated or extended where necessary.
- Ensure Consistency:
    - Maintain coding standards and consistency with the rest of the codebase, particularly in naming conventions and formatting.

.. _features_repository_setup:

4.2.3 Repository Setup (Features)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Identify the Relevant Package/Repository:
    - Identify the ROS package or repository that contains the code relevant to the feature.
- Create a New Branch for Development:
    - Pull the latest changes from the repository to ensure you're working with the most recent code.
    - Create and switch to a new branch for the feature development.

.. _features_implement_methods:

4.2.4 Implement the Methods in Each Object or Modify Existing Ones Based on the Requirements Defined in the Design Doc
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Develop Feature Logic:
    - Implement the required methods in the objects and data structures, following the design document.
    - Where applicable, modify existing methods to adapt to the new feature requirements.
- Ensure Modularity and Reusability:
    - Focus on modularity, ensuring that each function or class is self-contained and reusable.
    - If necessary, consider separating concerns into different classes or helper functions.
- Adhere to Code Quality Standards:
    - Ensure the code follows best practices for memory management, performance, and readability (read MISRA C++/JPL standard).
    - Review the feature for any potential bottlenecks or inefficiencies.

.. _features_write_unit_tests:

4.2.5 Write Unit Tests in Sync with QA for the Feature
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Collaborate with QA:
    - Work closely with the QA team to identify key areas for testing and to align the tests with the feature requirements.
    - Discuss edge cases, failure conditions, and other scenarios that need testing.
- Write Unit Tests Using GTest:
    - Implement GTest unit tests for each method or function introduced in the feature.
    - Ensure tests cover all major use cases, edge cases, and failure modes.
- Run the Unit Tests:
    - Run the tests frequently to ensure that each change is validated and that the feature works as expected.
    - Ensure all tests pass before moving on to the next step.
- Coordinate with QA on Test Coverage:
    - Ensure that QA reviews the tests and provides feedback or additional scenarios to test.
    - Keep tests synchronized with any changes made during development.

.. _features_write_documentation:

4.2.6 Write Documentation
^^^^^^^^^^^^^^^^^^^^^^^^^
- Document the Feature:
    - Write clear and concise documentation for the new feature. Include an overview of the feature, how it works, and its intended use.
    - Document all methods, classes, and data structures associated with the feature.
- Ensure Code Comments and Functionality Details:
    - In addition to high-level documentation, include inline comments explaining the purpose and functionality of complex methods or logic.
- Update Any Relevant Existing Documentation:
    - If the feature affects other parts of the system, update relevant documentation to reflect the changes made (e.g., user guides, API docs, etc.).

.. _features_add_logs_traces:

4.2.7 Add Ample Logs and Traces Without Introducing Too Much Log Spam
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Add Logging for Key Actions:
    - Insert logs at strategic points to track the flow of execution, particularly in complex or critical areas.
    - Ensure logs are descriptive, including relevant data (e.g., input parameters, results, error codes) to aid troubleshooting.
- Use Proper Logging Levels:
    - Implement different logging levels (e.g., debug, info, warning, error) based on the severity and importance of the log.
    - Avoid excessive logging at the debug level in production environments to prevent log spam.
- Ensure Log Clarity:
    - Keep logs clear and concise, avoiding unnecessary verbosity that could overwhelm developers or make logs hard to follow.
- Review and Remove Redundant Logs:
    - Periodically review the logs to ensure they remain relevant and remove any redundant or excessive entries.

.. _features_raising_pr:

4.2.8 Raising a Pull Request (PR) (Features)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Add the Modified Files:
    - Add the files that were changed.
- Commit the Changes:
    - Commit your changes with a clear, meaningful message that follows conventional commit standards.
- Push the Changes:
    - Push the changes to the remote repository.
- Create a Pull Request (PR):
    - In GitHub or GitLab, create a new pull request.
    - Include a description of the changes you’ve made and reference the Azure task ID using the task number.
- Request Reviews:
    - Request reviews from the relevant code reviewers.

.. _features_code_review:

4.2.9 Code Review & Revisions (Features)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Address Review Comments:
    - Address any feedback from the code reviewers by making the necessary revisions to the code.
- Push Changes After Revisions:
    - Once you've made the revisions, push the updated changes to the remote repository.
- Ensure Approval:
    - Repeat the review process until the pull request is approved.

.. _features_qa_testing:

4.2.10 QA Testing (Features)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Request QA Testing:
    - If the feature is for a major update, request QA to test the pull request in the relevant environment.
- Provide Image/Tag for Testing (if applicable):
    - Share any necessary Docker image tags, container registry information, or ROS workspace details for QA testing.
- Fix Bugs Reported by QA:
    - If QA reports additional bugs or regressions, fix them and request another round of code review.
- QA Signoff:
    - Once QA is satisfied with the changes, request their final sign-off on the feature.

.. _features_merging_backporting:

4.2.11 Merging & Backporting (Features)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Merge the Changes:
    - Once the pull request is approved, merge the changes into the required branch (e.g., main, develop, etc.).
- Backport the Changes if Necessary:
    - If the feature needs to be applied to previous versions of the code, add the necessary backport labels to the PR.
- Resolve Merge Conflicts:
    - If there are any merge conflicts, resolve them manually or using the backport library.
- Merge the Backport PRs:
    - Once the backport PRs are approved, merge them into the corresponding branches.

Revision History
-----------------

+-----+----------------+-------------------+-------------------------------------------------+-------------------------------------------------+
| Rev.| Date of        | Description       | Author                                          | Reviewers                                       |
|     | revision       |                   |                                                 |                                                 |
+=====+================+===================+=================================================+=================================================+
| 1.  | 11-Mar-2025    | First draft       | Sriram Radhakrishna                             | Dinesh Kumar V                                  |
+-----+----------------+-------------------+-------------------------------------------------+-------------------------------------------------+
