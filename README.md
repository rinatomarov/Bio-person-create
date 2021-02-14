# Bio-person-create

POSTMAN:

POST request: Create Person
http://127.0.0.1:8000/api/people/

input: Json

{
    "iin":"760724300757"
}

output:

{
    "Description": "Successful operation",
    "iin": "760724300757",
    "age": 44
}
---------------------------------------------------------------
GET reguest: Get person with iin
http://127.0.0.1:8000/api/people/760724300757

response :

{
    "Description": "Successful operation",
    "iin": "760724300757",
    "age": 44
}

if user doesn't exist : http://127.0.0.1:8000/api/people/760724300751
{
    "Description": "Person not found"
}
