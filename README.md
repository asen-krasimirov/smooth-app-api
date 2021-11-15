# Smooth App API
This is the back-end part of the Smooth App.

## Authentication ( /auth )

### Registration (post)

URL = /auth/register/

Upon successful registration a *profile object* will be created as well as *session object and* token will be returned.

```json
/* body */
{
    "email": "valid@email.com",
    "password": "validPassword",
    "is_business": false
}

/* successful response (example) */
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

```json
/* body */
{
    "email": "valid@email.com",
    "password": "validPassword"
}

/* successful response (example) */
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

```json
/* successful response */
{
    "message": "Successfully logged out!"
}
```

### Users List (get)

URL = /auth/users/

```json
/* successful response (example) */
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

```json
/* successful response (example) */
{
  "id": 2,
  "email": "Rembrant1@Test.Test",
  "is_business": false
}
```

### Profile Details (get)

URL = /auth/profile-details/{user_id}/

```json
/* successful response (example for Applicant Object) */
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

/* successful response (example for Business Object) */
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

```json
/* body (for Applicant Object Updates) */
{
  "first_name": "FirstName",
  "last_name": "LastName",
  "about_info": "AboutInfo",
  "icon_image": "123",
  "background_image": "",
  "skills": ["SkillOne", "SkillTwo"],
  "education": ["EducationOne", "EducationTwo"],
  "applicant_blog": "www.example.com"
}

/* successful response (for Applicant Object Updates) */
{
  "id": 6,
  "first_name": "FirstName",
  "last_name": "LastName",
  "about_info": "AboutInfo",
  "icon_image": "123",
  "background_image": "",
  "skills": ["SkillOne", "SkillTwo"],
  "education": ["EducationOne", "EducationTwo"],
  "applicant_blog": "www.example.com"
}

/* body (for Business Object Updates) */
{
  "name": "CompanyName",
  "sub_name": "SubName",
  "about_info": "AboutInfo",
  "icon_image": "image/upload/v1636971912/kbiez7io08flkulz9lcc.png",
  "background_image": "image/upload/v1636971912/kbiez7io08flkulz9lcc.png",
  "business_website": "www.example.com"
}

/* successful response (for Business Object Updates) */
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

```json
/* successful response (example) */
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

```json
/* successful response (example ) */
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

```json
/* successful response (example) */
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

```json
/* body (example) */
{
  "title": "Konche na edar, rogat dobitak",
  "description": "Yes, boy",
  "type": "FT",
  "status": "PH"
}

/* successful response (example) */
{
  "id": 1,
  "owner_id": 3,
  "title": "Konche na edar, rogat dobitak",
  "description": "Yes, boy",
  "type": "FT",
  "status": "PH"
}
```

## Administration

URL = /admin/
