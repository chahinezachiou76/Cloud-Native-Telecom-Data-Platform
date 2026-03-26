import boto3

REGION = "us-east-1"
ENDPOINT = "http://localhost:4566"

dynamodb = boto3.resource(
    'dynamodb', 
    endpoint_url=ENDPOINT, 
    region_name=REGION,
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

def show_results():
    table = dynamodb.Table('TelecomNetworkMetrics')
    
    try:
        response = table.scan()
        items = response.get('Items', [])
        
        print(f"\n--- Found {len(items)} Records in DynamoDB ---")
        print("-" * 50)
        
        for item in items:
            user = item.get('DeviceID', 'N/A')
            city = item.get('Location', 'N/A')
            usage = item.get('UsageGB', '0')
            print(f"User: {user} | City: {city} | Usage: {usage} GB")
            
        print("-" * 50)
        print("--- Verification Successful! ---")

    except Exception as e:
        print(f"Error reading from DynamoDB: {e}")

if __name__ == "__main__":
    show_results()