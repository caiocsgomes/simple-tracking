output "bucket_name" {
  value = aws_s3_bucket.state_bucket.id
}

output "dybamodb_table_name" {
  value = aws_dynamodb_table.state_dynamo.id
}

output "bucket_key_state_file" {
  value = var.bucket_key_state_file
}