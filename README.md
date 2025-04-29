# FlowBoard
FlowBoard - удобная система управления задачами и проектами, которая помогает командам планировать спринты, отслеживать прогресс и эффективно сотрудничать.

## Начальный план
### Users:
- Регистрация ✅
- JWT-авторизация ✅
### Projects:
- Создание проекта ✅
- Генерация ссылки приглашения ✅
- Присоединение по ссылке ✅
- Назначение ролей
### Tasks:
- CRUD задач
- Комментарии к задачам
- Проставление статусов, меток
- Назначение участников
### Notifications:
- Автоматическое создание уведомлений при смене статуса на "Готово"


## API Documentation
### Регистрация
POST /api/users/register/

Request:
```
{
  "username": "user",
  "email": "user@example.com",
  "password": "strongpassword123"
}
```
Response:
```
{
    "username": "user",
    "email": "user@example.com"
}
```

### Авторизация
POST /api/users/login/

Request:
```
{
    "username": "user",
    "password": "strongpassword123"
}
```
Response:
```
{
  "access": "your_access_token_here",
  "refresh": "your_refresh_token_here"
}
```

### Проекты

GET /api/projects/

Authorization: Bearer <your_token>

Response:
```
Список всех проектов, к которым принадлежит пользователь
```

GET /api/projects/2

Authorization: Bearer <your_token>

Response:
```
{
    "id": 2,
    "name": "Попытка номер 2",
    "description": "Попытка номер 2 описание",
    "invite_token": "SOtEh_RiJ1nTbmQXLLs50Mx4E6q9DFFrPfUZR3qRu-bIfMvuocsQGJtigIHtnkipXuXUd-5b9dTJFxSMuz9-3w",
    "owner": 5,
    "members": [
        5
    ]
}
```
или
```
{
    "detail": "У вас нет доступа к этому проекту, вы не являетесь участником."
}
```

GET /api/projects/2/generate_invite/

Authorization: Bearer <your_token>
```
{
    "invite_url": "http://127.0.0.1:8000/api/projects/invite/SOtEh_RiJ1nTbmQXLLs50Mx4E6q9DFFrPfUZR3qRu-bIfMvuocsQGJtigIHtnkipXuXUd-5b9dTJFxSMuz9-3w/"
}
```

GET /api/invite/SOtEh_RiJ1nTbmQXLLs50Mx4E6q9DFFrPfUZR3qRu-bIfMvuocsQGJtigIHtnkipXuXUd-5b9dTJFxSMuz9-3w/

Authorization: Bearer <your_token>
```
{
    "status": "Joined project by invite link"
}
```

POST /api/projects/

Authorization: Bearer <your_token>

Request:
```
{
    "name": "FlowBoard MVP",
    "description": "Проект для управления задачами."
}
```
Response:
```
{
    "id": 3,
    "name": "FlowBoard MVP",
    "description": "Проект для управления задачами.",
    "invite_token": "xwuXs8pZNjHbHLwBreqGe1drGovqQIhx3k_x_o6hJHM",
    "owner": 5,
    "members": [
        5
    ]
}
```
### Задачи

GET /api/tasks/

Вернёт задачи по всем проектам, к которым принадлежит пользователь.

GET api/tasks/?project=1

Вернёт задачи по проекту.

Authorization: Bearer <your_token>

Response:
```
[
    {
        "id": 1,
        "assignees": [
            "ulyana",
            "andrey"
        ],
        "labels": [
            "Баг",
            "Frontend"
        ],
        "status": "К выполнению",
        "created_by": "user",
        "project": "Проект 4-ого пользователя",
        "title": "Первая задача",
        "description": "Описание первой задачи 6 проекта",
        "started_at": "2025-04-29",
        "due_date": "2025-04-29"
    }
]
```

POST /api/tasks/

Authorization: Bearer <your_token>

Request:
```
{
    "assignees": ["user", "test"],
    "labels": ["Баг", "Frontend"],
    "status": "К выполнению",
    "project": "Попытка номер 2",
    "title": "Задача проекта 'Попытка номер 2', баг",
    "description": "Описание задачи",
    "due_date": "2025-04-29"
}

```
Response:
```
{
    "id": 2,
    "assignees": [
        "user",
        "test"
    ],
    "labels": [
        "Баг",
        "Frontend"
    ],
    "status": "К выполнению",
    "project": "Попытка номер 2",
    "created_by": "ulyana",
    "title": "Задача проекта 'Попытка номер 2', баг",
    "description": "Описание задачи",
    "started_at": "2025-04-29",
    "due_date": "2025-04-29"
}
```

POST /api/tasks/2/comments_create/

Если вы участник проекта, к которому принадлежит задача.

Authorization: Bearer <your_token>

Request:
```
{
    "content": "Это комментарий к задаче"
}
```
Response:
```
{
    "id": 2,
    "user": "ulyana",
    "task": "Задача проекта 'Попытка номер 2', баг",
    "created_at": "2025-04-29T10:03:43.646555Z",
    "content": "Это комментарий номер 2 к задаче"
}
```

GET /api/tasks/2/comments_list/

Если вы участник проекта, к которому принадлежит задача.

Authorization: Bearer <your_token>

Response:
```
[
    {
        "id": 1,
        "user": "ulyana",
        "task": "Задача проекта 'Попытка номер 2', баг",
        "created_at": "2025-04-29T09:48:19.870736Z",
        "content": "Это комментарий к задаче"
    },
    {
        "id": 2,
        "user": "ulyana",
        "task": "Задача проекта 'Попытка номер 2', баг",
        "created_at": "2025-04-29T10:03:43.646555Z",
        "content": "Это комментарий номер 2 к задаче"
    }
]
```
