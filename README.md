QA Practical Project



This project outcome is to create an application that generates objects. These objects are to be upon a set of predefined rules.

I am required to create a service-orientated architecture for my application which must be composed of at least 4 services that work together.

My idea for this this project is to have a pokemon trainer application.
My application will randomly give you a very cool pokemon. Then it will provide you with its rarity class and its level so you can determine its strength. All these object have been defined eventhough the selection is random.



The Architecture of this application



Service 1 

This service will be the frontend of the application. The user will view this service.

Service 2

This will be the first randomized value. A Pookemon will be chosen.

Service 3

This will be the second randomized value. This is choose the class rarity of the Pokemon which will be defined in service 4.

Service 4

This service accumalates all the information. All the hard coded values of the class rarity and Pokemon will be used to calculate the level of the Pokemon, which can be seen by the user.



Requirements for the Minimum Viable Product



A Kanban Board

This board made via Trello illustrates all the prelimenary tasks throughout the project. Also, it will include the user story and records of difficulties faced.


Risk Assessment

<img width="683" alt="Screenshot 2022-07-05 at 14 39 21" src="https://user-images.githubusercontent.com/104978039/177341977-cb1a84ce-b595-4299-91d6-063c3047534b.png">

An Application fully integrated using the Feature-Branch model with 4 services making use of a reverse proxy up to the specification of the task.


CI Server 

The application will run through a CI server (Jenkins), which will be deployed to a cloud-based virtual machine. This will also have webhooks integrated so that the application is automatically redeployed when updated.


Jenkins

Jenkins is going to be used to automatically to deploy the whole app. This is done by using a jenkins file which is on the development VM, I also added a webhook so that when you push something to github jenkins automatically runs the jenkins file. Within the jenkins file we have mulitple stages within the pipeline.

Testing - Testing the pytest within the application

Ansible Deployment - Automatically runs the ansible playbook and does everything within it


Once all this has been complete the project will be deployed onto the swarm and will be able to be accessed from the swarm ip

Here are some images of the jenkins pipeline terminal in which each stage has been complete, with comments.



