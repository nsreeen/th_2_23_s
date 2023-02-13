# Scaling

To make this app production ready, some of the things I'd think about are:
- Write logs to a database so they persist
- Tests
- Dockerise the app (with the database as a separate service)

I'd expect the following bottlenecks:
1) writing to the database
2) checking if the ok file exists

To allow this app to scale I would consider the following:
- Use a nosql database that can handle many writes, and allow more straightforward scaling of non relational data
- Use a timeseries specific database
- Configure the uvicorn server to use multiple processes
- Cache the result of /ping (as that does not need to be logged), and setting a very short time to live (perhaps 1 second).  This may or may not be worthwhile - I would analyse the requests first
- If needed I would consider running multiple instances of the server
