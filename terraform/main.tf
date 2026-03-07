provider "aws" {
  region                      = var.aws_region
  access_key                  = "test"
  secret_key                  = "test"
  s3_use_path_style           = true
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    s3       = "http://localhost:4566"
    dynamodb = "http://localhost:4566"
    iam      = "http://localhost:4566"
  }
}

resource "aws_s3_bucket" "telecom_logs" {
  bucket = var.bucket_name
}

resource "aws_dynamodb_table" "network_stats" {
  name           = var.table_name
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "DeviceID"
  range_key      = "Timestamp"

  attribute {
    name = "DeviceID"
    type = "S"
  }

  attribute {
    name = "Timestamp"
    type = "S"
  }
}

resource "aws_iam_role" "telecom_role" {
  name = "TelecomDataAccessRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_policy" "telecom_policy" {
  name = "TelecomDataPolicy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:PutObject",
          "s3:GetObject",
          "s3:ListBucket"
        ]
        Effect   = "Allow"
        Resource = [
          aws_s3_bucket.telecom_logs.arn,
          "${aws_s3_bucket.telecom_logs.arn}/*"
        ]
      },
      {
        Action = [
          "dynamodb:PutItem",
          "dynamodb:GetItem",
          "dynamodb:UpdateItem",
          "dynamodb:Query"
        ]
        Effect   = "Allow"
        Resource = aws_dynamodb_table.network_stats.arn
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "telecom_attach" {
  role       = aws_iam_role.telecom_role.name
  policy_arn = aws_iam_policy.telecom_policy.arn
}