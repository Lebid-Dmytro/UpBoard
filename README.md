# UpBoard

Django app for managing tasks in your project.

### **Check it out!**

UpBoard is a task management library deployed on [Render](https://upboard.onrender.com/).

### **Installation**

Ensure you have Python 3 installed before proceeding.

```shell
git clone https://github.com/Lebid-Dmytro/UpBoard
cd UpBoard
python3 -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python manage.py runserver  # starts Django Server
```

### **Features**

* User Authentication: Secure login and registration system.
* Task Management: Create, edit, and delete tasks easily.
* Task Status Updates: Track task progress using three statuses: "To Do", "In Progress", and "Done".
* Commenting System: Leave comments and reply to discussions within tasks.
* Archive System: Tasks marked as "Done" remain visible for 30 days before moving to the archive.
* Company-Based Management: Each task is linked to the creator's company automatically.
* Reviews: Users can submit feedback about the platform.

You can enter:

Superuser: 
```shell
login: user
password: user12345
```

Dev-user: 
```shell
login: user_front
password: user12345
```

### **Demo**

#### Home Page

Manage tasks, view the archive, and filter tasks by status.

<img width="522" alt="home_page" src="https://github.com/user-attachments/assets/6436f70f-f901-4a44-95d4-eb80f8fffff6" />
<hr/>

#### Authentication

Users must be authenticated to access and manage tasks.

<img width="1440" alt="authorization" src="https://github.com/user-attachments/assets/41218b44-3a76-41a0-9742-cfd65f3aa2bb" />
<hr/>

#### Create a Task

Fill in all required fields when adding a task. The creator and company are automatically assigned.

<img width="1370" alt="create_task" src="https://github.com/user-attachments/assets/bf4e5d94-227e-4ea0-9050-672ccee0be32" />
<hr/>

#### Task Archive

Tasks that were completed more than 30 days ago are moved to the archive.

<img width="1425" alt="archive" src="https://github.com/user-attachments/assets/b10393fc-3896-4305-a24f-3c1d9e306dd1" />
<hr/>

#### Task List by Status

Tasks are displayed based on their status ("To Do", "In Progress", "Done"). Each entry shows the task name, description, image, creation date, author, and comment count.

<img width="1422" alt="tasks_list" src="https://github.com/user-attachments/assets/8baee7e7-8d33-4b54-affc-bb464ac2271d" />
<hr/>

#### Task Details & Comments

View a task in detail, update its status, and engage in discussions through comments.

<img width="1414" alt="task_detail" src="https://github.com/user-attachments/assets/7c9effa6-c197-4299-9dad-938afbc5baf8" />
<img width="1440" alt="task_detail_and_comments" src="https://github.com/user-attachments/assets/e3c2765b-8708-4599-9541-90bb3cb39abf" />
<hr/>

#### Leave a Review

Users can provide feedback about their experience.

<img width="1440" alt="review" src="https://github.com/user-attachments/assets/8e7f0d3c-b03d-4d53-ad3b-8b55b4e999e1" />

<hr/>

#### Database Schema

[View Schema](https://drive.google.com/file/d/1qxbcVCgpRbFwbWvz44YgH8aW9X9he6AE/view?usp=sharing
)
