# SpaceX Challenge - API Execute

We recommended to see the docs: http://127.0.0.1:8000/redoc

## 1.- Start new environment

#### You need to start the environment, for that you need to call the follows endpoint:

> Just you need work space empty, like this:

![image info](./app/work_space.png)


ENDPOINT: `http://localhost:8000/create/new/environment/`

Body: `{
"name_board": "Obi-Wan Kennobi"
}`

This endpoint you just need to call it once time. This endpoint will do the follows:

* Create a new Board
* Crear the follows Labels
  * Bug
  * Maintenance
  * Research
  * Test
* Crear the follows Lists
  * TO-DO
  * IN PROGRESS
  * REVIEW
  * CLOSED

> For this reason this call maybe is a little slow, but it's right for the purpose

## 2.- Create Cards

If everything is OK, with the first step, now you can create your cards.

ENDPOINT: `http://localhost:8000/create/cards/`

Create card bug
Body:
```
{
"type": "bug",
"description": "Descriptions about a bug"
}
```

Create card task
Body:
```
{
"type": "task",
"title": "Task that we need maintenance",
"category": "maintenance"
}
```

Create a card issue
Body:
```
{
"type": "issue",
"title": "We need to fix this issue",
"description": "una descripcion para esta tarea que es un issue"
}
```
#### Comments

if you send other info, you will to see the errors in the response
