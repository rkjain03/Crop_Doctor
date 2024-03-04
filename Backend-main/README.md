<h1 align="center">Crop-Doctor App</h1>

<div align="center">
<a href="https://github.com/Crop-Doctor-SIH-22/Crop-doctor-frontend"><img width=200px src="https://github.com/Crop-Doctor-SIH-22/Crop-doctor-frontend/blob/main/frontend/public/android-chrome-512x512.png"  alt="Project logo"/></a></a>
 
</div>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#-table-of-contents)

This folder contains most of the backend. The backend follows a microservice architecture, there are many microservices nd these services communicate with each other through HTTP requests and the fronend communicates with the frontend via an API-gateway. The authentication service uses mongoDB and redis cache for user authentication. THe dl service uses ResNet9 as Deep Learning Model and flask server for deploying this model into an API, while the nginx acts as an API gateway.

The system architecture for the application is as followed:

<a href="https://github.com/Crop-Doctor-SIH-22/Crop-doctor-frontend"><img width="auto" src="https://github.com/Crop-Doctor-SIH-22/Crop-Doctor/blob/main/AboutProject/ArchitectureDiagram.svg"  alt="System Architecture"/></a>
