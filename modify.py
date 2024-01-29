import json
import google.auth
import google.auth.transport.requests
creds, project = google.auth.default()
import requests

def main():
    # Set parameters
    project_id = 'antriankjp'
    instance_name = 'antrian-kjp-db'
    machine_type = 'db-n1-standard-1'
    desired_tier = 'db-f1-micro'
    custom_tier = 'db-custom-10-26624'
    custom_tier_low = 'db-custom-4-10240'

    auth_req = google.auth.transport.requests.Request()
    creds.refresh(auth_req)

    value = {"token": str(creds.token)}
    token = creds.token
    #token = 'ya29.a0AfB_byCfQDxmoq99zc8OgurbEaA-mJl3PBy36biurO5a4IP4cXvxBQPN-QOLn-17zkYBMyOdXUTaSoBXWbwsBR7gCXXdopZCgB9DJ8DY3TtUP_9wLfCw9Nec69KsKMfrLbLcEhTIOuKr-4CXo0IbvIozmYtwg-F8OiugV05VTTaGaCgYKAUkSARASFQHGX2MimseppjGhETgQEQvd0MfFOw0179'
    print("Token")
    print(value)
    
    print("\n")


    url = f"https://sqladmin.googleapis.com/v1/projects/{project_id}/instances/{instance_name}"
    headers = {"Authorization": "Bearer " + token}
    data = "{""settings"": { ""tier"": '" + custom_tier + "' } }"

    response = requests.patch(url, data=data, headers=headers)

    print(response.content)


if __name__ == "__main__":
    main()