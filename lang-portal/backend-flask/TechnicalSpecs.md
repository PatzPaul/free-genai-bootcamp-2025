## Business Requirements

We are building a language learning portal that acts as a launchpad for study activities put also lets browse our vocabulary library.

- Have an inventory of words in the target language.
- Have a group of words to thematic categories.


### API Endpoints

### `GET /api/words` 
- Return a list of words 100 words at a time.
- pagination default:1
- sort by:
    - last reviewed
    - new
    - kanji
    - romaji
    - english
- review statistics

### Response Json

```json
[
    {
        "id":1,
        "kanji": "水",
        "romaji": "jin",
        "english": "person",
        "group_id": 1
    },
    ...
]
```




### `GET /api/words/{word_id}` 
- Get a single word by ID.

#### Response Json

```json
{
    "id":1,
    "kanji": "水",
    "romaji": "jin",
    "english": "person",
    "group_id": 1
}
```

### `GET /api/groups` 
- Get a list of word groups with word counts.
- Pagination 

#### Response Json

```json
[
    {
        "id":1,
        "name": "Animals"
    },
    ...
]
```

### `GET /api/groups/{group_id}`
 - Get words from a specific group.
 - Intended to be used by target apps 

#### Response Json

```json
{
    "id":1,
    "name": "Animals",
    "words": [
        {
            "id":1,
            "kanji": "水",
        }
    ]
}
```




### `GET /api/study-activities`
- Get all study activities.

#### Response Json

```json
[
    {
        "id":1,
        "name": "Study Activity 1",
        "description": "Study Activity 1 Description",
        "group_id": 1
    },
    ...
]
```
### `POST /api/study-sessions` 

- Create a new study session.  

#### Request Json

```json
{
    "study_activity_id": 1,
    "user_id": 1
}
``` 

#### Response Json

```json
{
    "id":1,
}
```     








## Technical Requirements


## Documentation