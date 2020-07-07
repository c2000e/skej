# skej

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

`PUT /deadlines/<name>`

**Arguments**

* `"name":string` a name/short description for the deadline
* `"date":date` the *deadline* for this deadline
* `"status":string` in progress/completed/past due

Only one argument must be supplied per request.

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
## Delete a deadline

**Definition**

`DELETE /deadlines/<name>`

**Response**

* `404 Not Found` if the deadline does not exist
* `204 No Content` on success

