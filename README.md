# courses_drf
Back-end DRF project for online course registration

Functionality: Users can register as teachers or as students. Teachers can create new courses with a year requirement.
Teachers also can see the list of all courses and the list of their personal courses. They also can view/update/delete their course.
Students can see the list of all courses, add some of them (if the year requirements is satisfied) and view them.

URLS:  
    Registration for students: ``http://127.0.0.1:8000/registration/student/``,  
    Registration for teachers: ``http://127.0.0.1:8000/registration/teacher/``,  
    Login: ``http://127.0.0.1:8000/login/``,  
    Logout: ``http://127.0.0.1:8000/logout/``,  
    All courses: ``http://127.0.0.1:8000/courses/all/``,  
    Personal courses: ``http://127.0.0.1:8000/courses/my/``,  
    Course creation: ``http://127.0.0.1:8000/courses/create/``,  
    A single course: ``http://127.0.0.1:8000/courses/<pk>/``,  
    Enroll to a course: ``http://127.0.0.1:8000/courses/<pk>/enroll`` 


This project integrates:
Users app has custom user models, custom registration, login, logout views. Also, view-leve custom permissions were implemented.
Courses app uses filtering and ordering as well as complex lookup. Custom view-level permissions were implemented as well.
The project itself uses postgres as a DB engine and has a throttling configured.
