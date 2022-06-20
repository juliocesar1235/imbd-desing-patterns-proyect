## Running the app
```sh
#Project can be build using the following command:

docker-compose build

#Project can be run using the following command:

docker-compose –-env-file config/dev.env up

#You can connect to the running container using the following command:

docker-compose exec app bash

#You can connect to the database using the following command:

docker-compose –-env-file config/dev.env exec postgres psql -h localhost -U movies movies

#You can recreate the database with the following command:

docker-compose –-env-file config/dev.env rm -v postgres

#You can access the project using the following url: 
http://localhost:5005/hello
```

<!-- TODO: use a make pipinstall command -->


## Running the tests

```sh
make test
# or, to run individual test types
make unit
make integration
make e2e
# or, if you have a local virtualenv
make up
pytest tests/unit
pytest tests/integration
pytest tests/e2e
```
