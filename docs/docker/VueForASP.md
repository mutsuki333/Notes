# Vue For ASP

A docker environment for compiling vue js.  
Aims to be used as a compiler for main.js and main.css  
And keep the working dir clean with only the src and dist folder  

## Usage

Use the files in the template folder as a start up  
and mount the *src* and *dist* folder in the docker container  

## Build

cd to the dockerfile folder  
`docker build -t vue_asp:latest .`

## Run

1. Copy the files in the template folder to the desired dir.
2. Replace the dir path and run
3. `docker run -d -it --name NAME -v "PATH/TO/DIST":/app/dist -v "PATH/TO/SRC":/app/src vue_asp bash`

> Ready to code and enjoy
