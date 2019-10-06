# Realtime Stream JSChart in Flask
 Visualize arbitrary realtime data streams in several different charts using Flask in python3.

![demo2](images/demo2.gif)

<details>
  <summary><strong>Table of Contents</strong> (click to expand)</summary>

<!-- toc -->

- [About](#about)
- [Getting-Started](#Getting-Started)
- [How-to-Send-data-to-your-Server](#How-to-Send-data-to-your-Server)
- [Docker-installation](#Docker-installation)
- [Demo](#Demo)
- [Run Old but still working](#run (Old but still working!))
- [Demo](#demo)
- [Examples](#examples)
- [Background](#Background)
- [Program-Structure](#Program-Structure)
- [What-is-flask?](#What-is-flask?)
- [What-is-JSChart?](#What-is-JSChart?)
- [License](#license)
- [Sources](#sources)

<!-- tocstop -->
</details>

# About
Visualizing data flows are important in a project maintaining data streams.
The abiliy to visualize data in realtime can have many advantages such as debugging,
demonstations and thereby early reach a proof of concept phase.
Showing data in charts using ChartJS, a simple powerful library for Javascript charts.
The implementation utilizes Flask and is developed mainly in python3 but with some
necessary Javascript functions.

<p align="center" >
  <img width="100" height="100" src="images/python.png">
  <img width="100" height="100" src="images/jquery.png">
  <img width="100" height="100" src="images/flask_logo.png">
  <img width="100" height="100" src="images/chartjs.png">
</p>


# Getting Started
install requirements
TODO
```
pip install -r requirements.txt
```
start by running:
```
python3 start.py
```
if website doesn't auto open, open webbrowser and open site:
```
https://127.0.0.1:5000/
```

# How to Send data to your Server
check out
```
socket_client.py
```
and
```
data_streams/samples.py
```

# Docker installation
TODO: The dockerfile is under development and will be fixed sortly
```
docker build . --tag="JSChart-flask:1.0"
```

To run image in background run:
```
docker run -d -p 5000:5000 JSChart-flask:1.0
```

To run image in interactive mode run:
```
docker run -it -p 5000:5000 JSChart-flask:1.0
```

Open your webbrowser of choice and open:
```
http://127.0.0.1:5000/
```


# Demo

This is the output on the console.
![demo1](images/demo1.PNG)

This is how the implementation looks like during execution.
![demo2](images/demo2.gif)

Examples of how each chart look and what to call the data in json:
https://www.chartjs.org/samples/latest/
https://tobiasahlin.com/blog/chartjs-charts-to-get-you-started

# Background
JSChart is great and useful for charts.
Automate stuff always intresting.
Generic server for several streams.

## Program Structure
See program structure image below:
![structure](images/structure.png)

## What is flask?
Flask is a micro web framework, enabling websites to be hosted in python.

## What is JSChart?
JSChart is an opensource project with the main purpose to provide awesome charts for html5 and javascript.

# Licenses
See ![lisence](LICENSE)

# Sources
The main inspiration and solutions comes from the following sources:
* https://gitlab.com/patkennedy79/flask_chartjs_example/tree/master/templates
* https://github.com/roniemartinez/real-time-charts-with-flask
