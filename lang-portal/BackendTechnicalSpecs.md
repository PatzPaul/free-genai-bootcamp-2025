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

Our Database will be a sigle sqlite database called `words.db` that will be in the root of the project folder of `backend_go`


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


## API Endpoints 

### GET /api/study_activities/:id
Returns details of a specific study activity for the study activity show page.

#### JSON Response
```json
{
    "id": 45,
    "name": "Vocabulary Quiz",
    "description": "Practice vocabulary with flashcard-style questions",
    "thumbnail_url": "/images/vocab-quiz-thumb.png",

}
```

### GET /api/study_activities/:id/study_sessions
Returns paginated study sessions for a specific study activity.

#### JSON Response
```json
{
    "items": [
        {
            "id": 123,
            "activity_name": "Vocabulary Quiz",
            "group_name": "Basic Greetings",
            "start_time": "2024-10-20T12:18:25-05:00",
            "end_time": "2024-10-20T12:34:25-05:00",
            "review_items_count": 20
        }
    ],
    "pagination": {
        "current_page": 1,
        "total_pages": 3,
        "total_items": 25,
        "items_per_page": 10
    }
}
```

### GET /api/words
Returns a paginated list of words with study statistics (100 items per page).

#### JSON Response
```json
{
    "items": [
        {
            "japanese": "こんにちは",
            "romaji": "konnichiwa",
            "english": "Hello",
            "correct_count": 12,
            "wrong_count": 3
        }
    ],
    "pagination": {
        "current_page": 1,
        "total_pages": 5,
        "total_items": 500,
        "items_per_page": 100
    }
}
```

### GET /api/words/:id
Returns details of a specific word with study statistics and groups.

#### JSON Response
```json
{    
    "japanese": "こんにちは",
    "romaji": "konnichiwa",
    "english": "Hello",
    "correct_count": 12,
    "wrong_count": 3,
    "groups": [
        {
            "id": 1,
            "name": "Basic Greetings"
        },
        {
            "id": 5,
            "name": "Daily Phrases"
        }
    ]
}

```

### GET /api/groups
Returns a paginated list of word groups.

#### JSON Response
```json
{
    "items": [
        {
            "id": 1,
            "name": "Basic Greetings",
            "total_word_count": 25
        }
    ],
    "pagination": {
        "current_page": 1,
        "total_pages": 2,
        "total_items": 15,
        "items_per_page": 10
    }
}
```

### GET /api/groups/:id
Returns details of a specific group with statistics.

#### JSON Response
```json
{
    "id": 1,
    "name": "Basic Greetings",
    "stats": { "total_word_count": 25
}
```

### GET /api/groups/:id/words
Returns paginated words in a specific group with study statistics.

#### JSON Response
```json
{
    "items": [
        {
            "japanese": "こんにちは",
            "romaji": "konnichiwa",
            "english": "Hello",
           "stats": { "correct_count": 12,
            "wrong_count": 3
            }
        }
    ],
    "pagination": {
        "current_page": 1,
        "total_pages": 3,
        "total_items": 25,
        "items_per_page": 10
    }
}
```

### GET /api/groups/:id/study_sessions
Returns paginated study sessions for a specific group.

#### JSON Response
```json
{
    "items": [
        {
            "id": 123,
            "activity_name": "Vocabulary Quiz",
            "group_name": "Basic Greetings",
            "start_time": "2024-10-20T12:18:25-05:00",
            "end_time": "2024-10-20T12:34:25-05:00",
            "review_items_count": 20
        }
    ],
    "pagination": {
        "current_page": 1,
        "total_pages": 2,
        "total_items": 15,
        "items_per_page": 10
    }
}
```

### GET /api/study_sessions
Returns a paginated list of study sessions (100 items per page).

#### JSON Response
```json
{
    "items": [
        {
            "id": 123,
            "activity_name": "Vocabulary Quiz",
            "group_name": "Basic Greetings",
            "start_time": "2024-10-20T12:18:25-05:00",
            "end_time": "2024-10-20T12:34:25-05:00",
            "review_items_count": 20
        }
    ],
    "pagination": {
        "current_page": 1,
        "total_pages": 1,
        "total_items": 5,
        "items_per_page": 100
    }
}
```

### GET /api/study_sessions/:id
Returns details of a specific study session.

#### JSON Response
```json
{
    "id": 123,
    "activity_name": "Vocabulary Quiz",
    "group_name": "Basic Greetings",
    "start_time": "2024-10-20T12:18:25-05:00",
    "end_time": "2024-10-20T12:34:25-05:00",
    "review_items_count": 20
}
```

### GET /api/study_sessions/:id/words
Returns paginated word review items for a specific study session.

#### JSON Response
```json
{
    "items": [
        {
            "id": 1,
            "japanese": "こんにちは",
            "romaji": "konnichiwa",
            "english": "Hello",
            "correct_count": 12,
            "wrong_count": 3,
            "correctness": true,
            "time_spent": 5.2,
            "review_status": "completed",
            "reviewer": "system"
        }
    ],
    "pagination": {
        "current_page": 1,
        "total_pages": 1,
        "total_items": 20,
        "items_per_page": 10
    }
}
```

### POST /api/reset_history
Resets all study history (study sessions and word review items).

#### JSON Response
```json
{
    "success": true,
    "message": "All study history has been reset",
}
```

### POST /api/full_reset
Performs a complete reset, dropping all tables and recreating with seed data.

#### JSON Response
```json
{
    "success": true,
    "message": "All data has been reset to initial state with seed data"
}
```

### POST /api/study_sessions/:id/words/:word_id/review
Records a word review result for a study session.

### Request Params

- id (study_session_id) integer
- word_id integer
- correct boolean

#### Request Payload
```json
{
    "correct": true
}
```

#### JSON Response
```json
{
    "success": true,
    "word_id": 1,
    "study_session_id": 123,
    "correct": true,
    "created_at": "2024-10-20T12:25:30-05:00"
}
```


## Scripts (Tasks)


## Mage Tasks
Mage is a task runner for Gp 
Lets list out possible tasks we need for our lang portal.



### Initialize Database 
This Task will initialize the sqlite database called `words.db` in the root folder of `backend_go`

### Migrate Database 
This task will run a series of migrations sql files on the database 

Migrations live in the `migrations` folder
The migration files will be run in order of their file name 
The file names should look like this:

```sql
0001_init.sql
0002_create_words_table.sql
0003_create_word_reviews_table.sql
0004_create_word_review_items_table.sql
0005_create_groups_table.sql
0006_create_word_groups_table.sql
0007_create_study_activities_table.sql
0008_create_study_sessions_table.sql
```

### Seed Data
This task will import json files and transform them into target data for our database.

All seed files live in the `seeds` folder

In our task we should have DSL to specific each seed file and its expected group word name.

```json
[
    {
        "kanji": "払う",
        "romaji": "harau",
        "english": "to pay",
       
    },
    ```
]