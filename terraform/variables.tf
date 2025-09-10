variable "project_name" {
  default     = "cloud resume"
  type        = string
  description = "This is the name of the s3 bucket that is created"
}

variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "us-east-1"
}

variable "dynamodb_table_name" {
  description = "DynamoDB table name for visitor counter"
  type        = string
  default     = "resume-visitors"
}