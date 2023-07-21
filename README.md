# model_simulator
for simulating models built

cd ../../users/sylvanus jerome/documents/python_scriptstopwordss/models_simulator

cd ~/Documents/things-n-thingses/python/web-stack/models_simulator
nano models_simulator/settingss/production.py
nano git/models_simulator/models_simulator/settingss/production.py

docker logs -n 20 -f mod-sim-con-web
docker exec -it mod-sim-con-web bash


create dump file
docker exec some-mysql sh -c 'exec mysqldump --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD"' > /some/path/on/your/host/all-databases.sql

retrieve data from dump file
$ docker exec -i some-mysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < /some/path/on/your/host/all-databases.sql


Debugging links
http://www.devarchive.org:8181/ nginx
http://www.devarchive.org:8282 gunicorn
http://www.devarchive.org:3307 mysql


Set environment variables
ENV POSTGRES_USER=<your-postgres-username>
ENV POSTGRES_PASSWORD=<your-postgres-password>
ENV POSTGRES_DB=<your-postgres-db-name>
ENV DJANGO_SETTINGS_MODULE=<your-django-settings-module>

Install PostgreSQL
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

Create the database
RUN service postgresql start && \
    su postgres -c "psql -c \"CREATE DATABASE ${POSTGRES_DB};\"" && \
    service postgresql stop


- docker build -t mod-sim .
- docker run --name court -it ubuntu
- docker exec -it court bash


Then commit the changes to a new Docker image instance using the following command.
- docker commit -m "What you did to the image" -a "Author Name" container_id repository/new_image_name


#### Pushing Docker Images to a Docker Repository
- docker login -u docker-registry-username

Note: If your Docker registry username is different from the local username you used to create the image, you will have to tag your image with your registry username. For the example given in the last step, you would type:

- docker tag sammy/ubuntu-nodejs docker-registry-username/ubuntu-nodejs

- docker push docker-registry-username/docker-image-name


cd git/models_simulator
docker compose up