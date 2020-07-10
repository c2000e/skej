# skej
(as in *schedule*)

Each response will be formatted as

```json
{
    "message": "message"
    "data"
}
```

where the message is a description of what occured on the server,
optionally followed by some relevant data, likely one or more deadlines.

Following responses only detail what data will be returned on a successful
request.

## List all deadlines

**Definition**

`GET /deadlines`

**Responses**

* `200 OK` on success

```json
[
    {
        "name": "Land on the moon",
        "date": "1969-07-20 16:18:00",
        "status": "completed"
    },
    {
        "name": "Land on Mars",
        "date": "2030-12-31 23:59:59",
        "status": "in progress"
    }
]
```

## Lookup a specific deadline

**Definition**

`GET /deadlines/{name}`

**Responses**

* `404 Not Found` if the deadline does not exist

* `200 OK` on success

```json
{
    "name": "Land on Mars",
    "date": "2030-12-31 23:59:59",
    "status": "in progress"
}
```

## Add a new deadline

**Definition**

`POST /deadlines`

**Arguments**

* `"name":string` a name/short description for the deadline
* `"date":date` the *deadline* for this deadline

If a deadline with the given name already exists, nothing will be written.

**Responses**

* `422 Unprocessable Entity` when invalid arguments are provided 

* `201 Created` on success

```json
{
    "name": "Land on Mars",
    "date": "2030-12-31 23:59:59",
    "status": "in progress"
}
```

## Modify a deadline

**Definition**

`PATCH /deadlines/<name>`

**Arguments**

* `"name":string` a name/short description for the deadline
* `"date":date` the *deadline* for this deadline
* `"status":string` in progress/completed/past due

Only one argument must be supplied per request.

**Responses**

* `422 Unprocessable Entity` when invalid arguments are provided

* `404 Not Found` if the deadline does not exist

* `200 OK` on success

```json
{
    "name": "Land on Mars",
    "date": "2030-12-31 23:59:59",
    "status": "in progress"
}
```
## Delete a deadline

**Definition**

`DELETE /deadlines/<name>`

**Response**

* `404 Not Found` if the deadline does not exist
* `204 No Content` on success

