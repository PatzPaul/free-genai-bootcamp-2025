## Frontend Technical Specs 

## Pages 

### Dashboard Index `/dashboard`

#### Purpose
The purpose of this page is to provide a summary for learning and acts as the default page when a user visit the web-app

#### Components 
This page contains the following components 
- Last Study Session 
    shows last activity used 
    shows when last activity used 
    summarizes wrong vs correct from last activity 
    has a link to the groupo 

- Study Progress 
    - Total words study 
        - across all study session show the total words studied out of all possible words in our database 
        - Display a mastery progress eg . 0% 

- Quick stats 
    - Success rate eg 80% 
    - Total study sessions eg. 4 
    - total active groups eg. 3
    - study streak eg. 4 days 
- Start Studying Button 
    - goes to study activities page 

#### Needed API points 
We 'll need following API endpoints to power this page 

- GET /api/dashboard/last_study_session
- GET /api/dashboard/study_progress
- GET /api/dashboard/quick_stats


### Study Activities Index `/study_activities`
#### Purpose 
The purpose of this page is show the user a collection of study activities with a thumbnail and its name, to either launch or view the study activity.

#### Components 
- Study Activity Card
    - Shows a thumbnail of the study activity 
    - The name of the study activity 
    - A launch Button to take us to the launch page 
    - The view page to view ore information about the past study sessions for this study activity


#### Needed API points 

- GET api/study_activities

### Study Actitivity Show `/study_activities/:id`
#### Purpose
The purpose of this page is to show the details of a study activity and its past study sessions

#### Components
- Name of study Activity 
- Thumbnail of study activity 
- Description of study activity
- Launch button 
- Study Activities Paginated List 
    - id 
    - Activity name 
    - group name
    - start time
    - end time ( inferred by the last word_reveiw_item_submitted)
    - number of review items 


#### Needed API points
- GET /api/study_activities/:id
- GET /api/study_activities/:id/study_sessions


### Study Activities Launch `/study_activities/:id/launch`

#### Purpose
The purpose of this page is to launch a study activity

#### Components
-  Name of study activity 
- Launch form
    - select field for group 
    - launch now button 


## Behaviour 
After the form is submitted a new tab opens with the study activity based on its URL provided in the database.

ALso the after form is submitted the page will redirect to the study session show page 

#### Needed API points
- POST /api/study_activities


### Words Index `/words`

#### Purpose
The purpose of this page is to show all words in our Database.

#### Components 
- Paginated Word List 
    - Japanese
    - Romaji 
    - English 
    - Correct COunt 
    - Wrong COunt 
- Pagination with 100 items per page 


#### Needed API Endpoints 
- GET /api/words

### Word Show `/words/:id`

#### Purpose 
The purpose of this page is to show information about a specific word.

#### Components 
- Japanese 
- Romaji 
- English
- Study Statistics 
    - Correct COunt 
    - Wrong COunt 
- Word Groups 
    - SHow an a series of pills eg tags 
    - WHen group name is clicled it will take us to the group show page 

#### Needed API points
- GET /api/words/:id




### Word Groups Index `/groups`

#### Purpose 
The purpose of this page is to show a list of groups in our database.

#### Components 
- Pahinated Group List 
    - Columns 
        - Group Name 
        - Word Count 
    - Clicking the group name will take us to the group show page

#### Needed API points
- GET /api/groups



### Group Show `/groups/:id`

#### Purpose 
The purpose of this page is to show information about a specific group 

#### Components 
- Group Name 
- Group Statistics
    - Total Word Count 
- Word in Group (Paginated List of words)
    - Should use the same component as the words index page  
- Study Sessions  (Paginated List of Study Sessions)
    - SHould use the same component and the study section index page 

#### Neeeded API Endpoints
- GET /api/groups/:id (the name and group stats)
- GET /api/groups/:id/words
- GET /api/groups/:id/study_sessions



### Study Sessions Index `/study_sessions`

#### Purpose 
The purpose of this page is to show a list of study sessions in our database.

#### Components
- Pahinated Study Session List
    - Columns
        - Id 
        - Activity Name 
        - Group Name
        - Start Time 
        - End Time
        - Number of Review Items
    - Clicking the study session id will take us to the study session show page 


#### Needed API points
- GET /api/study_sessions


### Study Sessions Show `/study_sessions/:id`

#### Purpose 
The purpose of this page is to show information about a specific study session 

#### Components
- Study session details 
    - Id 
    - Activity name 
    - group name
    - start time
    - end time ( inferred by the last word_reveiw_item_submitted)
    - number of review items 
- Word Review Items (Paginated List)
    - Should use the same component as the words index page
    - Columns
        - Word 
        - Correctness
        - Time Spent
        - Review Status
        - Reviewer
    - Clicking the word will take us to the word show page

#### Needed API points
- GET /api/study_sessions/:id
- GET /api/study_sessions/:id/words





### Settings Page `/settings`

#### Purpose 
The purpose of this page is to make configurations to the study portal.

#### Compon 
- Theme Selection eg. Light, Dark , System Default
- Reset History Button
    - This will delete all study sessions and word review items 
- Full Reset Button 
    - This will drop all tables and re-create with seed data 


#### Needed API Endpoints
- POST /api/reset_history
- POST /api/full_reset









