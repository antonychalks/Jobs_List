![Landing Page](static/media/README/langing-page.jpg)

# Job List

Organising your companies jobs, so you don't have to

The last update to this file was: **August 30th, 2023**

## Contents

[Design](#design)

- [The Strategy Plane](#the-strategy-plane)

- [The Scope Plane](#the-scope-plane)

- [The Structure Plane](#the-structure-plane)

- [The Skeleton Plane](#the-skeleton-plane)

- [The Surface Plane](#the-surface-plane)

[Agile Methodology](#agile-methodology)

[Features](#features)

- [Existing Features](#existing-features)

- [Future Features](#future-features)

[Languages](#languages)

[Frameworks and Libraries](#frameworks-and-libraries)

[Tools and Technologies](#tools-and-technologies)

[Testing and Validation](#testing-and-validation)

[Bugs and Fixes](#bugs-and-fixes)

[Deployment](#deployment)

[Cloning this repository](#cloning)

[Forking a branch](#forking)

[Credits](#credits)

[Acknowledgements](#acknowledgements)

## Design

### The Strategy Plane

#### Target User Group
Construction companies with at least two admin staff and at least ten tradesman.

- This website will benefit construction companies that deal with repairs, maintenance and insurance jobs.
- Ideal for teams that require a variety of trades for a variety of jobs.
- Tradesman that can attend multiple jobs in one day, without the need of asking job details every time.
- Teams that attend the same job multiple times with different people.

#### Problem Background
When I was working as a repairs carpenter for social housing, we had to use an app to load our jobs down into. This sounds like a good idea, but it was clearly designed by people who aren't going to use the app, and approved by people that also aren't going to use the app.

The problem with this is when people like me had to use the app every day, it didn't work in the best way. Our jobs only displayed for us one at a time, so there was no room for forward planning, the planners or tradesman couldn't set tasks on each job to keep up with the progress, and the tradesman couldn't change any incorrect details for the job.

The app was designed by people that were guessing what a tradesman needed, rather than asking the people who were going to use it.

#### Problem Statement

“I am a tradesman who is trying to be efficient with my work and progress jobs to completion whilst maintaining high standards, but I am being slowed down by my app.”

#### Project Aim

This project aims to provide tradesman and planners at construction companies a fully functioning app that gives both users the data customisation required to enable them to keep jobs updated which will increase efficiency.

[Return to contents list](#contents)

### The Scope Plane

The scope of this project is provided by user stories, organised below by epic and then role. 

Please note that some of the user stories below are not currenlty implemented. See [Product Backlog](#product-backlog) for a list of user stories not completed and [Future Features](#future-features) for further details on what is to come next.

#### EPIC - USER STORY: Register user.

<details>
<summary>
View User Stories
</summary>

As a **new user** I can register my account with the system so that a planner can register me as a tradesman.

 - Sign up using name and password.

</details>

#### EPIC - PLANNER STORY: Account Registration

<details>
<summary>
View User Stories
</summary>

As a **planner** I can register new users so that they can login and use the system.

As a **planner** I can register a new user, either planner or tradesman.

As a **planner** I can add a users role (planner or tradesman) so they receive the appropriate features.

As a **planner** I can register a new users different trades and certifications so they can be assigned the correct jobs.

As a **planner** I can optionally upload a profile image for the new user.

As a **planner** I can register the users first and last name.

As a **planner** I can register the new users emergency details, such as next of kin name and phone number, as well as any medical conditions.

As a **planner** I can register the new users contact information, such as email, address and phone number(s).


</details>

#### EPIC - PLANNER STORY: View user details

<details>
<summary>
View User Stories
</summary>

As a **Planner** I can view a paginated list of users on one screen.

As a **Planner** I can quickly see the users picture, name, phone number, role and any trades they have registered.

As a **Planner** I can click on a user to see a full page of all their details.

As a **Planner** I can edit a users details.

</details>

#### EPIC - PLANNER STORY: Create a job

<details>
<summary>
View User Stories
</summary>

As a **Planner** I can create a new job so that it can be sent to the tradesman.

As a **Planner** I can fill out the required information about the job.

As a **Planner** I can fill out the required information about the jobs contact details.

As a **Planner** I can add tasks to the job which includes assigning trades.

As a **Planner** I can edit or delete tasks that are already on the job.

As a **Planner** I can view the jobs status depending on if tasks are set and what progress they have made

</details>

#### EPIC - PLANNER STORY: View and edit an existing job.

<details>
<summary>
View User Stories
</summary>

As a **Planner** I can view and edit an existing job so that the current status can be seen and the content can be edited.

As a **Planner** I can load the jobs detail page and edit the different categories.

</details>

#### EPIC - TRADESMAN STORY: View jobs

<details>
<summary>
View User Stories
</summary>

As a **Tradesman** I can view a list of jobs, or individual job details so that I can attend the job and update the tasks on the job.

As a **Tradesman** I can view all the jobs on the system

As a **Tradesman** I can filter the jobs by trade and status

As a **Tradesman** I can click on a job to view its full details page

As a **Tradesman** I can edit a jobs details if they require updating

As a **Tradesman** I can add tasks to a job.

As a **Tradesman** I can edit or delete tasks on a job.

</details>

### Still in progress

#### EPIC - TRADESMAN STORY: Complete the risk assessment
This story will be implemented as a future feature by creating a new risk assessment model and form, and being attached to each job.
<details>
<summary>
View User Stories
</summary>

As a **Tradesman** I can view the jobs specific risk assessment so that I know what risks have been found.

As a **Tradesman** I can load the current risk assessment if there is one.

As a **Tradesman** I can edit and change the current risk assessment.

As a **Tradesman** I can create a new risk assessment.

</details>

#### EPIC - PLANNER STORY: Add appointments
This story will be implemented in the future as a feature to set dates in a calender for each tradesman to attend
<details>
<summary>
View User Stories
</summary>

As a **Planner** I can add appointments onto jobs so that the tradesmen can see their future jobs

As a **Planner** I can add an appointment and choose which tradesmen will attend.

As a **Planner** I can choose the time for the appointment.

As a **Planner** I can choose what criteria will be met for each appointment.

As a **Planner** I can send an email to the customer to confirm.

</details>

[Return to contents list](#contents)

---

### The Structure Plane

#### Website flow

The flow of the website depends entirely on the users role.


#### Not signed in:

If you're not signed in, you will have two options from the landing page.
- Login
- Register

This is to ensure the data is protected from anyone who isn't authorised.

Tradesman:
<details>
<summary>
    Landing
</summary>
As a tradesman when you first log in there will be a call to action button prompting you to enter the website. This will then take you to the tradesman home page.

![Landing Page](static/media/README/tradesman_landing.jpg)
</details>

<details>
<summary>
Tradesman Home
</summary>
On this page you can view all the different jobs on the database, and specifically:
- The job number
- The first line of address and postcode
- The job description
- The status

This information was chosen to be displayed on each card as its the information the other tradesman and I would always need to see first when I worked as a carpenter. 
- The job number - For any materials being ordered on accounts.
- The first line of address and postcode - So we knew where to go.
- The job description - We know what we're doing.
- The status - So we know if the job has been started yet.

![Tradesman home](static/media/README/tradesman_home.jpg)
</details>

<details>
<summary>
Job Detail
</summary>
On this page you can view all the jobs data from the database, and specifically:
- Status
- Created by
- Created on
- Description
- Contact Details
- Name
- Phone number
- Other phone number
- Email
- Street
- Town/city
- County
- Postcode
- Any tasks that have been added.

On this page the tradesmen are able to edit the contact details of a job, add a task, edit a task and delete it, enabling CRUD functionality to the page. From here a tradesman will be able to view all the details they need for each job, as well as the tasks that have already been completed, and what needs to be completed. This is useful as it will prevent a tradesman going to a job, just to find out another trade needs to attend first.

![Job Detail](static/media/README/job_detail.jpg)
</details>

<details>
<summary>
Job Detail
</summary>
On this page you can view all the jobs data from the database, and specifically:
- Status
- Created by
- Created on
- Description
- Contact Details
- Name
- Phone number
- Other phone number
- Email
- Street
- Town/city
- County
- Postcode
- Any tasks that have been added.

On this page the tradesmen are able to edit the contact details of a job, add a task, edit a task and delete it, enabling CRUD functionality to the page. From here a tradesman will be able to view all the details they need for each job, as well as the tasks that have already been completed, and what needs to be completed. This is useful as it will prevent a tradesman going to a job, just to find out another trade needs to attend first.

![Job Detail](static/media/README/job_detail.jpg)
</details>