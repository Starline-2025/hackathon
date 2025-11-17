# Репозиторий команды Starline

## Website

[https://kartadobra-nko.ru/](https://kartadobra-nko.ru/)

## Admin-panel:

[https://kartadobra-nko.ru/admin/](https://kartadobra-nko.ru/admin/)

### Email:
```
admin@example.com 
```
### Password:
```
secret
```
<!-- DOCS_START -->
# 📘 API Documentation

**Title:** Карта Добра API

**Version:** 1.0.0

**Description:** API для получения и создания карточек НКО

**OpenApi File:** api/openapi.yaml

---

## `GET /api/get_cards`

**Summary:** Получить карточки с фильтрацией

**Parameters:**

| Name | In | Type | Required | Description |
|------|----|------|----------|-------------|
| name | query | string | No | Имя карточки |
| city | query | string | No | Город |
| category | query | string | No | Категория |

**Responses:**

- **HTTP 200**: Список карточек
  - **Content-Type**: `application/json`
  **Schema**:
    - Array of:
      - **name** (string) **(required)**: N/A
      - **category** (string) **(required)**: N/A
      - **description** (string) **(required)**: N/A
      - **city** (string) **(required)**: N/A
      - **website** (string) **(required)**: N/A
      - **lat** (number) **(required)**: N/A
      - **lng** (number) **(required)**: N/A
      - **address** (string) : N/A
      - **contacts** (string) : N/A
      - **img** (string) : N/A

- **HTTP 404**: Карточки не найдены
  - **Content-Type**: `application/json`
  **Schema**:
    - **message** (string) **(required)**: N/A

- **HTTP 500**: Внутренняя ошибка сервера
  - **Content-Type**: `application/json`
  **Schema**:
    - **message** (string) **(required)**: N/A


---

## `POST /api/get_cards`

**Summary:** Создать новую карточку

**Request Body:**

Content-Type: `application/json`

- **name** (string) **(required)**: N/A
- **category** (string) **(required)**: N/A
- **description** (string) **(required)**: N/A
- **city** (string) **(required)**: N/A
- **website** (string) **(required)**: N/A
- **lat** (number) **(required)**: N/A
- **lng** (number) **(required)**: N/A
- **address** (string) : N/A
- **contacts** (string) : N/A
- **img** (string) : N/A

**Responses:**

- **HTTP 200**: Карточка создана
  - **Content-Type**: `application/json`
  **Schema**:
    - **name** (string) **(required)**: N/A
    - **category** (string) **(required)**: N/A
    - **description** (string) **(required)**: N/A
    - **city** (string) **(required)**: N/A
    - **website** (string) **(required)**: N/A
    - **lat** (number) **(required)**: N/A
    - **lng** (number) **(required)**: N/A
    - **address** (string) : N/A
    - **contacts** (string) : N/A
    - **img** (string) : N/A

- **HTTP 500**: Внутренняя ошибка сервера
  - **Content-Type**: `application/json`
  **Schema**:
    - **message** (string) **(required)**: N/A


---
<!-- DOCS_END -->
## Postman:
### [doc](https://www.postman.com/andrei-555543/workspace/startline)
