output "s3_bucket_id" {
  value = aws_s3_bucket.telecom_logs.id
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.network_stats.name
}

output "iam_role_arn" {
  value = aws_iam_role.telecom_role.arn
}