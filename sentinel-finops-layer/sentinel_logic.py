import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    print("--- Starting FinOps Sentinel Scan ---")
    
    # 1. Cleaning Unused EBS Volumes (Storage not attached to any Instance)
    volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
    for volume in volumes['Volumes']:
        v_id = volume['VolumeId']
        print(f"[ACTION] Deleting unused EBS volume: {v_id}")
        ec2.delete_volume(VolumeId=v_id)

    # 2. Releasing Unused Elastic IPs (AWS charges for EIPs not associated)
    eips = ec2.describe_addresses()
    for eip in eips['Addresses']:
        if 'InstanceId' not in eip:
            print(f"[ACTION] Releasing unassociated Elastic IP: {eip['PublicIp']}")
            ec2.release_address(AllocationId=eip['AllocationId'])

    # 3. Stop Development Instances at Night (Scheduling)
    # We target instances with the tag 'Environment: Dev'
    dev_instances = ec2.describe_instances(Filters=[
        {'Name': 'tag:Environment', 'Values': ['Dev']},
        {'Name': 'instance-state-name', 'Values': ['running']}
    ])
    
    for reservation in dev_instances['Reservations']:
        for instance in reservation['Instances']:
            i_id = instance['InstanceId']
            print(f"[ACTION] Stopping Dev Instance for cost saving: {i_id}")
            ec2.stop_instances(InstanceIds=[i_id])

    print("--- FinOps Sentinel Scan Completed Successfully ---")
    return {"status": "Cleaned"}