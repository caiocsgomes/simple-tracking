resource "aws_s3_bucket" "codepipeline_bucket" {
  bucket = format("%s-bucket", var.pipeline_name)
}