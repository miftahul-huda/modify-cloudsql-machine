import googleapiclient.discovery

def main():
    # Set parameters
    project_id = 'lv-playground-appdev'
    instance_name = 'testing-db'
    machine_type = 'db-n1-standard-1'
    desired_tier = 'db-f1-micro'
    custom_tier = 'db-custom-10-26624'


    # Authenticate with Google Cloud
    service = googleapiclient.discovery.build('sqladmin', 'v1beta4')

    # Get the current instance settings
    get_instance_request = service.instances().get(project=project_id, instance=instance_name)
    get_instance_response = get_instance_request.execute()

    # Extract the current settings version
    current_settings_version = get_instance_response['settings']['settingsVersion']
    print(current_settings_version)

    body = {
        'settings': {
            'settingsVersion': current_settings_version,
            'tier' : custom_tier
        }
    }

    # Update instance
    request = service.instances().update(project=project_id, instance=instance_name, body=body)
    response = request.execute()



    # Check for errors
    if response.get('error'):
        print(f"Error: {response['error']['errors'][0]['message']}")
    else:
        print(f"Successfully updated the machine type of instance '{instance_name}'.")

    #print(response)


if __name__ == "__main__":
    main()