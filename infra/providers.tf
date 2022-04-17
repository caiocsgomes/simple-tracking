terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.6.0"
    }
  }
  backend "s3" {
    bucket         = "simpletracking-state-store-backend"
    key            = "terraform.tfstate"
    dynamodb_table = "simpletracking-state-locking-table"
    region         = "us-east-1"
  }
}

provider "aws" {
  region = "us-east-1"
}
