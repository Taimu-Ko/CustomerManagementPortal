# CustomerManagementPortal

V1-Beta:
-----------------------------------------------------------
Python based application to simulate customer actions, such as card CRUD operations and Invoice CRUD operations.

Includes Admin functionality for user management as well as forced time outs for security.

V1.0:
-----------------------------------------------------------
Dockerized application

Create and run local docker images of application using these commands:

docker build -t "name-of-image" .

docker run -d -p 5000:5000 "name-of-image"

V1.0.1:
------------------------------------------------------------
Removed Lorem Ipsum Text for text taken from company website.

Added user account lock from failed login attempts

V1.0.2:
------------------------------------------------------------
Added unit tests for all functionality

Test commands:

cd .\Tests\

python -m unittest discover

Unit tests only work with fresh version of database

V1.0.3:
------------------------------------------------------------
Updated tests

V1.0.4:
------------------------------------------------------------
Fresh database with test accounts implemented and updated metadata

V1.0.5:
------------------------------------------------------------
Added confirmation popup for delete and lock/unlock actions

Ammended unit tests for popup confirmation

Useful Information
-------------------------------------------------------------
Login Information:

Admin User: rcbrown94@outlook.com

Admin Password: P@ssw0rd12

Normal User: kitsunegrimm1@gmail.com

Normal Password: P@ssw0rd12

[DatabaseScripts.txt](https://github.com/Taimu-Ko/CustomerManagementPortal/files/9506315/DatabaseScripts.txt)

