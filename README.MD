
# tamatem-technical-assignment

instructions on running and building the application
- Run locally: 
    - install the requirements by running the command 
    ```bash 
    pip install  -r requirements.txt
    ```
    - pass enviroment path PORT to select a different port
    ```bash 
        export PORT=<PORT>
    ```
    - run the app 
    ```bash 
        python3 main.py
    ```
- Run on k8s cluster
     `helm upgrade -i <APPNAME> helm/ -n <name space>`
    - you can run with the provided image that has been uploaded to the Docker Hub or you can change the image in the values.yaml 
        ```helm
        deployments:
            tamatem-technical-assignment:
                containers:
                tamatem-technical-assignment:
                    image: "basharkhouri610/tamatem-technical-assignment:latest"
        ```
        I have uploaded the image under the tags latest,amd64 and arm64 