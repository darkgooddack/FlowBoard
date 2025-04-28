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
