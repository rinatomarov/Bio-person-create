# Bio-person-create

info:
  title: Biometric Test
  description: Get age by iin
  version: 1.0.0
paths:
  /people/:
    post:
      summary: Create a person
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                iin:
                  type: string
                  example: 760724300757
      responses:
        "201":
          description: successful operation
          content:
            application/json:
              schema:
                type: object
                properties:
                  iin:
                    type: string
                    example: 760724300757
                  age:
                    type: number
                    example: 44
        "400":
          description: Invalid input
  /people/{iin}/:
    get:
      summary: Get person by IIN
      description: Returns a single person
      parameters:
      - name: iin
        in: path
        description: IIN
        required: true
        schema:
          type: string
      responses:
        "200":
          description: successful operation
          content:
            application/json:
              schema:
                type: object
                properties:
                  iin:
                    type: string
                    example: 760724300757
                  age:
                    type: number
                    example: 44
        "404":
          description: Person not found
