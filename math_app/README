# Mathapp

## Setup
You can create and activate a virtual environment to run the app as follows:
```
python3 -m venv venv
source venv/bin/activate
```

## To run
To start the app:
`uvicorn app/main:app --reload`


## Sample queries
```
curl -X POST http://127.0.0.1:8000/min -d '{"numbers": [1,2,3], "quantifier":3}' -H 'Content-Type: application/json'
```
response: 1

```
curl -X POST http://127.0.0.1:8000/percentile -d '{"numbers": [1,2,3,4], "quantifier":75}' -H 'Content-Type: application/json'
```
response: 3
