variable "bucket_name" {
  type        = string
  description = "Name for the bucket where the state will be stored"
}

variable "dynamodb_name" {
  type        = string
  description = "Name for the dynamodb table used for state locking"
}

variable "bucket_key_state_file" {
  type    = string
  default = "terraform.tfstate"
}

variable "region" {
  default = "us-east-1"
}