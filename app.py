import boto3
import pandas as pd
import random
import time

# --- الإعدادات المطلوبة لتجاوز الخطأ ---
REGION = "us-east-1"
ENDPOINT = "http://localhost:4566"

# تعريف الموارد مع تحديد المنطقة والمفاتيح (ضروري جداً)
dynamodb = boto3.resource(
    'dynamodb', 
    endpoint_url=ENDPOINT, 
    region_name=REGION,
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

def process_isp_data():
    print("--- [STEP 1] Generating Sensor Data ---")
    provinces = ['Algiers', 'Oran', 'Constantine', 'Setif', 'Annaba']
    data = {
        'user_id': [f'USER_{i}' for i in range(100)],
        'usage_gb': [round(random.uniform(10, 100), 2) for _ in range(100)],
        'location': [random.choice(provinces) for _ in range(100)]
    }
    df = pd.DataFrame(data)
    
    print("--- [STEP 2] Filtering High Usage (> 80GB) ---")
    high_usage_df = df[df['usage_gb'] > 80]
    
    print(f"--- [STEP 3] Saving {len(high_usage_df)} records to DynamoDB ---")
    table = dynamodb.Table('TelecomNetworkMetrics')
    
    for _, row in high_usage_df.iterrows():
        table.put_item(
            Item={
                'DeviceID': row['user_id'],
                'Timestamp': str(time.time()),
                'UsageGB': str(row['usage_gb']),
                'Location': row['location']
            }
        )
    print("--- [SUCCESS] Data migration to LocalStack completed! ---")

if __name__ == "__main__":
    process_isp_data()