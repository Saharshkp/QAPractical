QA Practical Project



This project outcome is to create an application that generates objects. These objects are to be upon a set of predefined rules.

I am required to create a service-orientated architecture for my application which must be composed of at least 4 services that work together.

My idea for this this project is to have a pokemon trainer application.
My application will randomly give you a very cool pokemon. Then it will provide you with its rarity class and its level so you can determine its strength. All these object have been defined eventhough the selection is random.



The Architecture of this application



Service 1 

This service will be the frontend of the application. The user will view this service.

Service 2

This will be the first randomized value. A Pokemon will be chosen.

Service 3

This will be the second randomized value. This is choose the class rarity of the Pokemon which will be defined in service 4.

Service 4

This service accumalates all the information. All the hard coded values of the class rarity and Pokemon will be used to calculate the level of the Pokemon, which can be seen by the user.


Application as seen by a user from a browser:


<img width="475" alt="Screenshot 2022-07-08 at 13 51 53" src="https://user-images.githubusercontent.com/104978039/177996000-56f4d920-a1d9-4991-a6bc-1ddcef1652dd.png">


Application in terminal using:

curl localhost


<img width="444" alt="Screenshot 2022-07-08 at 13 51 31" src="https://user-images.githubusercontent.com/104978039/177996191-a08e621f-4a9a-4882-baec-54366c3cf8d4.png">


<img width="410" alt="Screenshot 2022-07-08 at 13 50 53" src="https://user-images.githubusercontent.com/104978039/177996210-9d3298f0-9f5a-42f1-a4e1-f73cd6970ffd.png">




Requirements for the Minimum Viable Product



A Kanban Board

This board made via Trello illustrates all the prelimenary tasks throughout the project. Also, it will include the user story and records of difficulties faced.


<img width="1406" alt="Screenshot 2022-07-08 at 13 56 41" src="https://user-images.githubusercontent.com/104978039/177996378-8625e9a4-e443-4192-87fc-27d41bd3b4ab.png">



Risk Assessment

<img width="683" alt="Screenshot 2022-07-05 at 14 39 21" src="https://user-images.githubusercontent.com/104978039/177341977-cb1a84ce-b595-4299-91d6-063c3047534b.png">

An Application fully integrated using the Feature-Branch model with 4 services making use of a reverse proxy up to the specification of the task.


CI Server 

The application will run through a CI server (Jenkins), which will be deployed to a cloud-based virtual machine. This will also have webhooks integrated so that the application is automatically redeployed when updated.


Jenkins

Jenkins is going to be used to automatically to deploy the whole app. This is done by using a jenkins file which is on the development VM, I also added a webhook so that when you push something to github jenkins automatically runs the jenkins file. Within the jenkins file we have mulitple stages within the pipeline.

Docker Hub- Log into docker hub and build the new containers

Testing - Testing the pytest within the application

Ansible Deployment - Automatically runs the ansible playbook and does everything within it

Once all this has been complete the project will be deployed onto the swarm and will be able to be accessed from the swarm ip



Jenkins Pipeline Test Images


Finished Jenkins Pipeline image:


<img width="777" alt="Screenshot 2022-07-07 at 14 45 29" src="https://user-images.githubusercontent.com/104978039/177996723-60da0ad3-e6c6-4aa1-8c13-1be02d49639d.png">



Serivce 1 test


<img width="655" alt="Screenshot 2022-07-06 at 17 39 42" src="https://user-images.githubusercontent.com/104978039/177979387-f0ae48d3-dbac-4cfd-bd97-dfb8c89ac061.png">


Service 2 test


<img width="657" alt="Screenshot 2022-07-06 at 17 39 51" src="https://user-images.githubusercontent.com/104978039/177979320-3ca3e538-1418-402c-a61c-324bbe22cff8.png">


Service 3 test


<img width="647" alt="Screenshot 2022-07-06 at 17 39 58" src="https://user-images.githubusercontent.com/104978039/177979487-8b492211-6852-413f-81b8-9cbe2b0b24bd.png">


Service 4 test


<img width="647" alt="Screenshot 2022-07-06 at 17 40 08" src="https://user-images.githubusercontent.com/104978039/177979525-916cd5c0-d055-4479-9a60-55d413f23490.png">


Ansible Deployment in Shell Script


<img width="1429" alt="Screenshot 2022-07-07 at 14 45 14" src="https://user-images.githubusercontent.com/104978039/177979701-895297b9-1383-44ec-a491-ba8e25bf2ddd.png">


Pipeline completed with Swarm

<img width="1034" alt="Screenshot 2022-07-08 at 14 02 02" src="https://user-images.githubusercontent.com/104978039/177997206-7c97aca7-173f-4ba8-afc7-2c5cf617e616.png">



CI-CD Pipeline


<img width="689" alt="Screenshot 2022-07-08 at 12 09 25" src="https://user-images.githubusercontent.com/104978039/177981284-5b7d2c09-9287-4df2-8d49-f015036e6434.png">



Future Updates


With more time for this project, I would impliment a button to refresh the random generator and also add a history section where all past Pokemon can be viewed with all their statistics. For this I will need to add a database to store all the outputs.



Challenges


A challenge I faced was to understand a how to correctly code a docker-compose.yaml file. With a lot of research and practise, I was able to perfect this and have it fully running.
The same goes for the jenkinsfile. Generating the script correctly and using the stages to correctly execute tests and also the Ansible deployment.



Conclusion


I believe I have successfully shown my improvement in this project from the fundamentals work. Being able to overcome difficulties from then a lot more easily and tackling more complex concepts such as using Jenkins with Ansible for example. I am definitely more confident on my abilities as a novice developer especially working with deployment programs. Being able to understand how all the parts come to together from Docker images to Jenkins reading containers has allowed me to think and act as a more experience developer. I understand that this application is still very basic however, as a foundation I believe it shows my journey of learning.



Acknowledgements


Adam Gray

Leon Robinson
