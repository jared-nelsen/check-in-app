# Lustro
-------------------------------------------------------------------------------------------------------------------------------------

# Development Trajectory

    - Secure lustro.ai domain

    1. Deployment

        - Support a local kubernetes deployment
        - GCP Research

    2. Interviewing infrastructure as a service
      
-------------------------------------------------------------------------------------------------------------------------------------

# Product development trajectory

    - Investigation of embedded component technique

        - Ideally I would like to create a few embeddable components to package up and give out
        - Flutter apps may be embeddable
        - Do I even need flutter or are there other JS packages that will accomplish what I need to
    
    - Strategy around genericising interviews

        - Ability for a user to seed questions
        - Ability to use same interview infrastructure for different situations
            - Animated interface
            - Embedded interface
        
    - Business use case investigation and cataloging

        - Product reviews
        - Journalistic Purposes
        - Journaling
        - Performance reviews

-------------------------------------------------------------------------------------------------------------------------------------

# Future Work

    1. Add manipulatable preferences to question generation
    2. Add randomized question generation
        - Question Type order
    3. Add follow up questions
        - Keyword flagging
        - Sentiment Analysis
        - Historical Answer Contect
    4. Logging

-------------------------------------------------------------------------------------------------------------------------------------

## A note on question types

Ideally an interview is an organic experience with different types of questions. This is something I can emulate.

Types of questions:

1. Dichotomous Yes or No questions
2. Elaborative questions
3. Multiple Choice Questions
4. Text Slider Questions
5. Open Ended Questions
6. Thumbs Up Thumbs Down Question
7. User entered question

-------------------------------------------------------------------------------------------------------------------------------------

## Links

### Flutter

    - Dockerizing Flutter apps: https://blog.codemagic.io/how-to-dockerize-flutter-apps/
    - Video detailing Flutter web release strategies (Dart Web servers): https://www.youtube.com/watch?v=yoAdPgw7YLM

### Kubernetes

    - Developing services locally: https://cloud.google.com/community/tutorials/developing-services-with-k8s
    
### Docker

    - Install Docker on Linux Mint: https://computingforgeeks.com/install-docker-and-docker-compose-on-linux-mint-19/
    - User Permission Denied Fix: https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue

### Dart

    - Simple Dart http servers: https://dart.dev/tutorials/server/httpserver

### Flask

    - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
    
### Firestore

    - Install FireStore https://firebase.google.com/docs/cli#install-cli-mac-linux
    - Install Local Emulator Suite - https://firebase.google.com/docs/emulator-suite/install_and_configure
    - Use Python for local database - https://stackoverflow.com/questions/54868011/how-to-use-google-cloud-firestore-local-emulator-for-python-and-for-testing-purp
    - Start local emulator
        - firebase emulators:start
        - Hosted on port 4000
    - Firestore and Flask - https://gaedevs.com/blog/how-to-use-the-firestore-emulator-with-a-python-3-flask-app

-------------------------------------------------------------------------------------------------------------------------------------

## Plans

### Authentication plan

Authentication will be handled through Firebase Auth both in the flutter apps and the python back ends. There are auth packages for each.

-------------------------------------------------------------------------------------------------------------------------------------
