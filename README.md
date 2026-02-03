# Star Wars Films API

A simple REST API for fetching Star Wars films and comments. The API retrieves film data from the [Star Wars API (SWAPI)](https://swapi.dev/) and allows users to add and view comments. Designed for scalability, caching and efficiency.

---


## **Features**

- Fetch a list of Star Wars films from SWAPI.
- Each film includes:
  - `id`
  - `title`
  - `release_date`
  - `comment_count` (number of user comments)
- Add comments to films (max length 500 characters).  
- Retrieve a list of comments for a film in ascending order of creation.  
- Caching for film lists to reduce API load and improve performance.  
- Pagination support for films and comments.  
- Rate limiting to prevent abuse.  
- Automated deployment to a cloud platform (Heroku/AWS/GCP/DigitalOcean).  

---

## **Tech Stack**

- **Backend:** Django + Django REST Framework
- **Database:** PostgreSQL  
- **Caching:** Redis  
- **External API:** [SWAPI](https://swapi.dev/)
- **Version Control:** Git

---