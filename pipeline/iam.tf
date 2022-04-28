resource aws_iam_role "pipeline_role" {
  name               = format("%s-role", var.pipeline_name)
  assume_role_policy = data.aws_iam_policy_document.pipeline_trust_policy_document.json
}

resource "aws_iam_role_policy" "pipeline_policy" {
  name   = format("%s-policy", var.pipeline_name)
  role   = aws_iam_role.pipeline_role.id
  policy = data.aws_iam_policy_document.pipeline_policy_document.json
}

data "aws_iam_policy_document" "pipeline_policy_document" {
  statement {
    actions   = ["s3:GetObject", "s3:PutObject", "s3:ListBucket"]
    resources = [
      "${aws_s3_bucket.codepipeline_bucket.bucket}/",
      "${aws_s3_bucket.codepipeline_bucket.bucket}/*"
    ]
  }
  statement {
    actions   = ["codebuild:StartBuild", "codebuild:BatchGetBuilds"]
    resources = ["*"]
  }
}

data "aws_iam_policy_document" "pipeline_trust_policy_document" {
  statement {
    principals {
      type        = "Service"
      identifiers = ["codepipeline.amazonaws.com"]
    }
    actions = ["sts:AssumeRole"]
  }
}