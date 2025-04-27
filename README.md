# FlowBoard
FlowBoard - удобная система управления задачами и проектами, которая помогает командам планировать спринты, отслеживать прогресс и эффективно сотрудничать.

## Начальный план
### Users:
- Регистрация
- JWT-авторизация
### Projects:
- Создание проекта
- Генерация ссылки приглашения
- Присоединение по ссылке
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
POST /api/register/

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
POST /api/login/

Request:
```
{
  "email": "user@example.com",
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