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

### GET /api/dashboard/last_study_session
Returns information about the most recent study session

#### JSON Response
```json
{
    "items": [
        {
        "id": 123,
        "activity_name": "Vocabulary Quiz",
        "group_name": "Basic Greeting",
        "start_time": "2024-10-20T12:18:25-05:00",
        "end_time": "2024-10-20T12:34:25-05:00",
        "review_items_count": 20
        }
    ],
    "pagination": {
        "current_page": 1,
        "total_pages": 1,
        "total_items": 100,
        "items_per_page":20
    }
}
```

### GET /api/dashboard/study_progress
Returns study progress statistics 
Please note that the frontend will determine progress bar based on total words studied and total available words.

#### JSON Response
```json 
{
    "total_words_studied": 3,
    "total_available_words": 124,
}
```

### GET /api/dashboard/quick_stats

Returns quick overview statistics.

#### JSON Response 

```json
{
    "total_words": 500,
    "total_groups": 10,
    "words_mastered": 120,
    "recent_accuracy": 85.5
}

```

### GET /api/study_activities/:id
Returns details of a specific study activity.

#### JSON Response
```json
{
    "id": 45,
    "name": "Verb Conjugation",
    "thumbnail_url": "https://example.com/thumbnail.jpg",
    "description": "Practice your vocabulary with flashcards"
}
```




###  GET /api/study_activities/:id/study_sessions
Returns study sessions for a specific study activity 

#### JSON Response
```json
{
    "items": [
        {
            "id": 123,
            "start_time": "2024-02-28T10:15:00Z",
            "end_time": "2024-02-28T10:30:00Z",
            "total_words": 20,
            "accuracy_rate": 85.5
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
Returns a paginated list of words (100 items per page)

#### JSON Response
```json
{
    "items": [
        {
            "id": 1,
            "japanese": "こんにちは",
            "romaji": "konnichiwa",
            "english": "Hello",
            "correct_count": 5,
            "wrong_count": 2
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
Returns details of a specific word.

#### JSON Response
```json
{
    "japanese": "こんにちは",
    "romaji": "konnichiwa", 
    "english": "Hello",
    "stats": {
        "correct_count": 5,
        "wrong_count": 2
    },
    "groups": [
        {
        "id": 1,
        "name": "Basic Greetings"
    }
    ]
}

```

### GET /api/groups
- Pagination with 100 items per page 

#### JSON Response
```json

{
    "items": [
        {
            "id": 1,
            "name": "Basic Greetings",
            "word_count": 25
        }
    ],
    "pagination": {
        "current_page": 1,
        "total_pages": 3,
        "total_items": 30,
        "items_per_page": 10
    }
}
```

### GET /api/groups/:id
Returns details of a specific group 

#### JSON Response

```json
{
    "id": 1,
    "name": "Basic Greetings",
    "stats":{
    "word_count": 25
}
}
```

### GET /api/groups/:id/words
Returns words in a specific group 

#### JSON Response
```json

{
    "items": [
        {
            "id": 1,
            "japanese": "こんにちは",
            "romaji": "konnichiwa",
            "english": "Hello"
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

### GET /api/study_sessions
Returns a paginated list of study sessions 

#### JSON Response
```json

{
    "items": [
        {
            "id": 123,
            "activity_name": "Vocabulary Quiz",
            "group_name" : "Basic Greetings", 
            "start_time": "2024-02-28T10:15:00Z",
            "end_time": "2024-02-28T10:30:00Z",
            "total_words": 15,
            "accuracy_rate": 90.0
        }
    ],
    "pagination": {
        "current_page": 1,
        "total_pages": 2,
        "total_items": 20,
        "items_per_page": 10
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
    "start_time": "2024-02-28T10:15:00Z",
    "end_time": "2024-02-28T10:30:00Z",
    "review_items_count":20
}
```
## GET /api/study_sessions/:id/words
Returns words for a specific study session

#### JSON Response
```json

{
    "items": [
        {
            "id": 1,
            "japanese": "こんにちは",
            "romaji": "konnichiwa",
            "correct_count": 5,
            "wrong_count": 2
        }
    ],
    "pagination": {
        "current_page": 1,
        "total_pages": 2,
        "total_items": 20,
        "items_per_page": 100
    }
}

```

### POST /api/reset_history
Reset user's study history 

#### JSON Response
```json
{
    "success": true,
    "message": "Study history has been reset"
}
```

### POST /api/full_reset
Performs a complete reset of all data 

#### JSON Response
```json
{
    "success": true,
    "message": "Sytsem has been fully reset"
}
```


### POST /api/study_sessions/:id/words/:word_id/review
Records a word review for a specific study session 

#### Request Params
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
    "status": "success",
    "word_id": 1,
    "was_correct": true,
    "total_reviews": 16,
    "correct_reviews": 13
}
```
    


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
```