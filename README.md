# Smooth App API

This is the back-end part of the Smooth App.

### Deployed to:
The application is deployed on Heroku here- https://smooth-app-api.herokuapp.com/

## Authentication ( /auth )

### Registration (post)

URL = /auth/register/

Upon successful registration a *profile object* will be created as well as *session object and* token will be returned.

<b>Body</b>

```json
{
  "email": "valid@email.com",
  "password": "validPassword",
  "is_business": false
}
```

<b>Successful Response (example)</b>

```json
{
  "user": {
    "id": 5,
    "email": "Rembrant3@Test.Test",
    "is_business": true
  },
  "token": "DA4ZCp38unpOhojlUhDgfCo7Y3rru0I73D0Kd6O4grUXBKVU73BENXdBfTgHZIPH"
}
```

### Login (post)

URL = /auth/login/

Upon successful login a *session object* will be created (or called if there is one already) and token will be returned.

<b>Body</b>

```json
{
  "email": "valid@email.com",
  "password": "validPassword"
}
```

<b>Successful Response (example)</b>

```json
{
  "user": {
    "id": 5,
    "email": "Rembrant3@Test.Test",
    "is_business": true
  },
  "token": "DA4ZCp38unpOhojlUhDgfCo7Y3rru0I73D0Kd6O4grUXBKVU73BENXdBfTgHZIPH"
}
```

### Logout (post)

URL = /auth/logout/?AUTH_TOKEN={valid_session_token}

<b>Successful response</b>

```json
{
  "message": "Successfully logged out!"
}
```

### Users List (get)

URL = /auth/users/

<b>Successful Response (example)</b>

```json
[
  {
    "id": 2,
    "email": "Rembrant1@Test.Test",
    "is_business": false
  },
  {
    "id": 3,
    "email": "Rembrant2@Test.Test",
    "is_business": true
  }
]
```

### User Details (get)

URL = /auth/users/{id}

<b>Successful Response (example)</b>

```json
{
  "id": 2,
  "email": "Rembrant1@Test.Test",
  "is_business": false
}
```

### Profile Details (get)

URL = /auth/profile-details/{user_id}/

<b>Successful Response (example for Applicant Object)</b>

```json
{
  "id": 3,
  "first_name": "Tosho",
  "last_name": "Testing",
  "about_info": "This is Tosho Testing",
  "icon_image": "image/upload/v1636971912/kbiez7io08flkulz9lcc.png",
  "background_image": "image/upload/v1636971912/kbiez7io08flkulz9lcc.png",
  "skills": [
    "flying at high autitute",
    "hourse qzdings"
  ],
  "education": [
    "Columbia University"
  ],
  "applicant_blog": "www.example.com"
}
```

<b>Successful Response (example for Business Object)</b>

```json
{
  "id": 4,
  "name": "Ivancho",
  "sub_name": "Testing",
  "about_info": "This is Ivancho Testing",
  "icon_image": "image/upload/v1636971912/kbiez7io08flkulz9lcc.png",
  "background_image": "image/upload/v1636971912/kbiez7io08flkulz9lcc.png",
  "business_website": "www.example.com"
}
```

### Profile Details Updating (put)

URL = /auth/profile-details/{user_id}/?AUTH_TOKEN={valid_session_token}

<b>Body (for Applicant Object Updates)</b>

```json
{
  "first_name": "FirstName",
  "last_name": "LastName",
  "about_info": "AboutInfo",
  "icon_image": "123",
  "background_image": "",
  "skills": [
    "SkillOne",
    "SkillTwo"
  ],
  "education": [
    "EducationOne",
    "EducationTwo"
  ],
  "applicant_blog": "www.example.com"
}
```

<b>Successful Response (for Applicant Object Updates)</b>

```json
{
  "id": 6,
  "first_name": "FirstName",
  "last_name": "LastName",
  "about_info": "AboutInfo",
  "icon_image": "123",
  "background_image": "",
  "skills": [
    "SkillOne",
    "SkillTwo"
  ],
  "education": [
    "EducationOne",
    "EducationTwo"
  ],
  "applicant_blog": "www.example.com"
}
```

<b>Body (for Business Object Updates)</b>

```json
{
  "name": "CompanyName",
  "sub_name": "SubName",
  "about_info": "AboutInfo",
  "icon_image": "image/upload/v1636971912/kbiez7io08flkulz9lcc.png",
  "background_image": "image/upload/v1636971912/kbiez7io08flkulz9lcc.png",
  "business_website": "www.example.com"
}
```

<b>Successful Response (for Business Object Updates)</b>

```json
{
  "id": 4,
  "name": "CompanyName",
  "sub_name": "SubName",
  "about_info": "AboutInfo",
  "icon_image": "image/upload/v1636971912/kbiez7io08flkulz9lcc.png",
  "background_image": "image/upload/v1636971912/kbiez7io08flkulz9lcc.png",
  "business_website": "www.example.com"
}
```

## Jobs ( /jobs )

### Job List (get)

URL = /jobs/

<b>Successful Response (example)</b>

```json
[
  {
    "id": 1,
    "owner_id": 3,
    "title": "Ezdene na edar, rogat dobitak",
    "description": "Yes, boy",
    "type": "FT",
    "status": "PH"
  },
  {
    "id": 2,
    "owner_id": 7,
    "title": "Testing, Testing",
    "description": "YES",
    "type": "PT",
    "status": "AH"
  }
]
```

### Job List by Owner ID (get)

URL= /jobs/?owner_id={valid_owner_id}

<b>Successful Response (example)</b>

```json
[
  {
    "id": 2,
    "owner_id": 7,
    "title": "Testing, Testing",
    "description": "YES",
    "type": "PT",
    "status": "AH"
  },
  {
    "id": 3,
    "owner_id": 7,
    "title": "Testing2, Testing2",
    "description": "YES2",
    "type": "PT",
    "status": "AH"
  }
]
```

### Job Details (get)

URL = /jobs/{id}/

<b>Successful Response (example)</b>

```json
{
  "id": 1,
  "owner_id": 3,
  "title": "Kon na edar, rogat dobitak",
  "description": "Yes, boy",
  "type": "FT",
  "status": "PH"
}
```

### Job Details Update (put)

URL = /jobs/{id}/?AUTH_TOKEN={valid_session_token}

<b>Body (example)</b>

```json
{
  "title": "Konche na edar, rogat dobitak",
  "description": "Yes, boy",
  "type": "FT",
  "status": "PH"
}
```

<b>Successful Response (example)</b>

```json
{
  "id": 1,
  "owner_id": 3,
  "title": "Konche na edar, rogat dobitak",
  "description": "Yes, boy",
  "type": "FT",
  "status": "PH"
}
```

### Job Creation (post)

URL = /jobs/?AUTH_TOKEN={valid_session_token}

<b>Body (example)</b>

```json
{
  "title": "Konche na edar, rogat dobitak",
  "description": "Yes, boy",
  "type": "FT",
  "status": "PH"
}
```

<b>Successful Response (example)</b>

```json
{
  "id": 1,
  "owner_id": 3,
  "title": "Konche na edar, rogat dobitak",
  "description": "Yes, boy",
  "type": "FT",
  "status": "PH"
}
```

### Applied Jobs List (get)

URL = /jobs/applied/?user_id={valid_user_id}

<b>Successful Response (example)</b>

```json
{
  "jobs": [
    {
      "id": 4,
      "job_id": 9,
      "user_id": 15,
      "title": "2",
      "description": "2d",
      "type": "PT",
      "status": "PH"
    },
    {
      "id": 5,
      "job_id": 23,
      "user_id": 15,
      "title": "2",
      "description": "2d",
      "type": "PT",
      "status": "PH"
    }
  ],
  "profile": {
    "id": 15,
    "first_name": "I wass",
    "last_name": "Goshos",
    "about_info": "I am Gosho and I am good employee, I don't need a lot of money (around 800$/month). I don't have any ambitions and I don't really have a social life.",
    "icon_image": "https://media.istockphoto.com/vectors/employee-vector-id1326243788?b=1&k=20&m=1326243788&s=170667a&w=0&h=5tWxD-ZmE-8uIwH4p6rWUpF9_HMp0OjmBmKvoU5vhm8=",
    "background_image": "https://i.pinimg.com/550x/61/8c/bc/618cbcf614fd1782413f1919d64b8509.jpg",
    "skills": [
      "Nothing,Nothing really...",
      "Don't have perspective on of my life"
    ],
    "education": [
      "Pathetic Uni",
      "Pathetic School",
      "Boring Academy"
    ],
    "applicant_blog": "https://example.com"
  }
}
```

### Applied Job Details (get)

URL = /jobs/applied/{job_id}/

<b>Successful Response</b>

***Response is the same as Applied Jobs List but with only one job info***

### Apply Job (post)

URL = /jobs/applied/?AUTH_TOKEN={valid_owner_session_token}

<b>Body (example)</b>

```json
{
  "job_id": "9"
}
```

<b>Successful Response (example)</b>

```json
{
  "id": 5,
  "job_id": 9,
  "user_id": 15,
  "title": "2",
  "description": "2d",
  "type": "PT",
  "status": "PH"
}
```

### Unapply Job (delete)

URL = /jobs/applied/{job_id}/?AUTH_TOKEN={valid_owner_session_token}

<b>Successful Response</b>

```json
{
  "message": "Successfully unapplied!"
}
```

### Job Applicants (get)

URL = /jobs/{valid_job_id}/applicants/

<b>Successful Response (example)</b>

```json
{
  "applicants": [
    {
      "id": 16,
      "first_name": "Mr Goshko",
      "last_name": "Goshev",
      "about_info": "This is the most important intel on me- I am cool.",
      "icon_image": "https://pyxis.nymag.com/v1/imgs/66c/700/bd13af1f94c1c174ed17c7a33b29d36bcc-GettyImages-1278090730.rsquare.w1200.jpg",
      "background_image": "https://wallpaperaccess.com/full/6043682.jpg",
      "skills": [
        ""
      ],
      "education": [
        "Harvard"
      ],
      "applicant_blog": "https://joebiden.com/presidency-for-all-americans/"
    }
  ]
}
```

## Administration

URL = /admin/
