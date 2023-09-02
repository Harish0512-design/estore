# estore

### Registration

1. User can sign up using endpoint http://127.0.0.1:8000/api/accounts/signup/

Request Payload:

* POST

      {
   
         "email" : youremailaddress,
      
         "password" : yourpassword,
      
         "firstname": yourfirstname,
      
         "lastname" : lastname
   
      }

  Here email, password are required and firstname, lastname are optional

1) After signup, user will receive confirmation email to verify. Click on the link in email to confirm.

2) Now user is verified. This link is valid for 3 days.

Response Payload

         200 (OK)
         Content-Type: application/json
         {
            "success": "User verified."
         }
            
         400 (Bad Request)
         Content-Type: application/json
         {
             "detail": "Unable to verify user."
         }

* GET

  http://127.0.0.1:8000//api/accounts/signup/verify/?code=<code>

When the user clicks the link in the verification email, the front end should call this endpoint to verify the user.

      * Parameters
            code (required)

### Login

1. After Signup, Login using the endpoint http://127.0.0.1:8000/api/accounts/login/

   Request Payload

* POST

         {
            "email" : your-registered-email
            "password": your-password
         }

  Response Payload

         200 (OK)

         Content-Type: application/json
         {
            "token": "91ec67d093ded89e0a752f35188802c261899013"
         }
         
         400 (Bad Request)
         Content-Type: application/json
         {
            "password": [
                  "This field may not be blank."
               ],

            "email": [
                  "This field may not be blank."
               ]
         }
         
         {
            "email": [
               "Enter a valid email address."
            ]
         }
         
         401 (Unauthorized)
         {
            "detail": "Authentication credentials were not provided."
         }
         
         {
            "detail": "Unable to login with provided credentials."
         }

### Logout

You can logout using endpoint  http://127.0.0.1:8000/api/accounts/login/

GET

* HTTP Header

      Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

Response Payload

         200 (OK)
         Content-Type: application/json
         {
             "success": "User logged out."
         }
         
         401 (Unauthorized)
         Content-Type: application/json
         {
             "detail": "Authentication credentials were not provided."
         }
         
         {
             "detail": "Invalid token"
         }

### Password Reset

To reset Password use the endpoint http://127.0.0.1:8000/api/accounts/password/reset

Request Payload

* POST

      {
         "email" : your-email-address
      }

Response Payload

      201 (Created)
      Content-Type: application/json
      {
          "email": "amelia.earhart@boeing.com"
      }
      
      400 (Bad Request)
      Content-Type: application/json
      {
          "email": [
              "This field may not be blank."
          ]
      }
      
      {
          "email": [
              "Enter a valid email address."
          ]
      }
      
      {
          "detail": "Password reset not allowed."
      }

### Password reset verification

http://127.0.0.1:8000/api/accounts/password/reset/verify/?code=<code>

When user clicks the link in the password reset email,
call this endpoint to verify the password reset code.

Request Payload

* GET

         {
            "code" : code
         }

Responses

      200 (OK)
      Content-Type: application/json
      {
          "success": "User verified."
      }
      
      400 (Bad Request)
      Content-Type: application/json
      {
          "password": [
              "This field may not be blank."
          ] 
      }
      
      {
          "detail": "Unable to verify user."
      }

Call this endpoint with the password reset code and the new password, to reset the user's password

http://127.0.0.1:8000/api/accounts/password/reset/verified

Request Payload

* GET

        {
            "code":code
            "password": new_password
        }

Responses

      200 (OK)
      Content-Type: application/json
      {
          "success": "Password reset."
      }
      
      400 (Bad Request)
      Content-Type: application/json
      {
          "password": [
              "This field may not be blank."
          ] 
      }
      
      {
          "detail": "Unable to verify user."
      }
    
    