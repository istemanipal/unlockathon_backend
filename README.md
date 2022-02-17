# ISTE Manipal Unlockathon Backend | Django

##### This repository has the code for the event Unlockathon, which is a part of our TechWeek. TechWeek is generally held in the month of January, in the even Semester

## Prerequisites

##### The dependencies are listed in the file _requirements.txt_. <br/><br/>To install the dependencies, use the command `pip install -r requirements.txt`

## Starting the development server

##### To start the development server, use the command `python manage.py runserver`. The development server will start on port number* 8000*

## API Documentation

1. /api/get_logged_in_user (GET): <b>Get the details of the logged in user</b>

```
{
    first_name:string,
    last_name:string,
    registration_number:string,
    email:string,
    phone:string,
    points:number,
    current_question:number,
    skips:number
}
```

2. /api/get_question (GET): <b>Get the question of the logged in user based on question_number in the database</b> <br/>
   <b> Case 1 </b>:Found (Question exists)

```
{
    status:'found'
    question:{
        question_number:number,
        question:string,
        image:string,
        hint:string
    }
}
```

<b>Case 2</b> Not found (Which means user has completed the game)

```
{
    status:'not found',
    question:null,
    message:'Congratutlations! You have completed all questions!'
}
```

3. /api/leaderboard (GET): <b>Get current leaderboard</b>

<b> Case 1 </b>:Found (People are playing)

```
{
    status:'found',
    leaderboad:List<user>
}
```

Refer to 1 for user type <br/>
<b>Case 2:</b> Not found (People are not playing)

```
{
    status:'not found',
    leaderboard:[]
}
```

4. /api/check_answer (POST): <b>Checks answer to the question the user is currently on</b></br>

Reqest Body

```
{
    answer:string
}
```

Response:<br/>
Case 1: Correct answer</b>
1.1: User has more questions to answer

```
{
    status:'correct',
    points:number,
    next_question:{
        question_number:number,
        question:string,
        image:string,
        hint:string
    }
}
```

1.2: User does not have more questions to answer

```
{
    status:'correct',
    points:number,
    next_question:null,
    message:'Congratulations! You have completed all questions!'
}
```

Case 2: Wrong answer

```
{
    status:'wrong'
}
```

Case 3: Error

```
{
    status:'Something Went Wrong'
}
```

5. /api/skip (POST): Skip the question the user is on </br>

Case 1: User has suffienct skips <br>
1.1: User has more questions to answer <br>

```
{
    status:'successful',
    skips:number,
    next_question:{
        question_number:number,
        question:string,
        image:string,
        hint:string
    }
}
```

1.2 User does not have more questions to answer <br>

```
{
    status:'successful',
    skips:number,
    next_question:null,
    message: 'Congratulations! You have completed all questions!'
}
```

Case 2: Insufficient skips

```
status: 'insufficient skips'
```

Case 3: Error

```
{
    status:'Something went wrong'
}
```
