# Project Echo MongoDB

Owner: Backend
Status: active production infrastructure
Runtime boundary: `src/Components/MongoDB`

This folder defines the MongoDB image and initialization data used by the local
EchoNet Docker Compose stack.

## Important Paths

- `MongoDB.Dockerfile` - MongoDB image definition.
- `init/init-mongo.js` - database initialization script.
- `init/*.json` - seed data for EchoNet and user/admin collections.
- `docker-compose.yml` - standalone MongoDB compose file for focused database work.
- `test_connection.py` - local connection smoke-test helper.

## Runtime Configuration

The canonical local runtime is `src/Components/docker-compose.yml`, where the
database service is named `echo_store` and the container is named
`ts-mongodb-cont`. The API should use `MONGODB_URI` and `USER_MONGODB_URI` rather
than hard-coded credentials or hostnames.

Do not commit local database dumps, credentials or generated data files. Seed
JSON files in `init/` should be reviewed before production use because they may
contain sample users, roles, donations, requests or synthetic event data.

## Deployment Notes

`src/Echo_Components_on_K8s/MongoDb` is a Kubernetes deployment copy of MongoDB
assets. Keep it until the K8s deployment has one confirmed source of truth for
MongoDB image, initialization and seed data.
