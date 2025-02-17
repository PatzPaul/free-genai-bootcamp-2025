## Backend Tech specs


### Business Goal

- A language learning school wants to buld a prototyoe of learning portal whiuch will act as three things: 
- Inventory of possible vocabulary that can be learned
- Act as a learning record store (LRS), providing correct and wrong score on practice vocabulary 
- A unified launchpad to launcg different learning apps 

## Tech Requirements 

- The backend will be built using Go
- The database will be SQlite3
- The API will be built using Gin 
- The API will always return JSON 
- There will be no authentication and authorization 
- Everything to be treated as a single user 

## Database schema 
We have the following tables : 
- words - stored vocabulary words
    - id integer 
    - japanese string 
    - romaji string
    - english string 
    - parts string    
- word_groups - Joined table for words and groups 
many to many
    - id integer 
    - word_id integer 
    - group_id integer
- groups - thematic groups of words
    - id integer 
    - name string 
- study_sessions - records of study sesisons grouping
- id  integer
- group_id  integer
- created_at datetime
- study_activity_id integer

- Study_activities - a specific study activity, Linking a study session to group
- word_review_items - a record of word practice, determining of the word was correct or noti 
- word_id  integer
- study_session_id  integer
- correct boolean
- created_at datetime 


#### API Endpoints 

- GET /api/dashboard/last_study_session
- GET /api/dashboard/study_progress
- GET /api/dashboard/quick_stats
- GET /api/study_activities/:id
- GET /api/study_activities/:id/study_sessions
- GET /api/words
    - pagination with 100 items per page 
- GET /api/words/:id 
- GET /api/groups
    - pagination
- GET /api/groups/:id
- GET /api/groups/:id/words
- GET /api/groups/:id/study_sessions
- GET /api/study_sessions
    - pagination with 100 items per page 
- GET /api/study_sessions/:id
- GET /api/study_sessions/:id/words
- POST /api/study_activities
- POST /api/reset_history
- POST /api/full_reset
- POST /api/study_sessions/:id/words/:word_id/review
    - required params: correct 
    