# CodePipeline IAM
resource aws_iam_role "pipeline_role" {
  name               = format("%s-role", var.pipeline_name)
  assume_role_policy = data.aws_iam_policy_document.pipeline_trust_policy_document.json
}

resource "aws_iam_role_policy" "pipeline_policy" {
  name   = format("%s-pipeline-policy", var.pipeline_name)
  role   = aws_iam_role.pipeline_role.id
  policy = data.aws_iam_policy_document.pipeline_policy_document.json
}

data "aws_iam_policy_document" "pipeline_policy_document" {
  statement {
    actions = [
      "s3:GetObject", "s3:PutObject", "s3:ListBucket", "s3:GetObjectVersion", "s3:GetBucketVersioning",
      "s3:PuObjectAcl",
    ]
    resources = [
      aws_s3_bucket.codepipeline_bucket.arn,
      "${aws_s3_bucket.codepipeline_bucket.arn}/*"
    ]
  }
  statement {
    actions   = ["codebuild:StartBuild", "codebuild:BatchGetBuilds", "codestar-connections:UseConnection"]
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

# CodeBuild IAM
resource "aws_iam_role" "build_role" {
  name               = format("%s-build-role", var.pipeline_name)
  assume_role_policy = data.aws_iam_policy_document.build_trust_policy_document.json
}

resource "aws_iam_role_policy" "build_policy" {
  name   = format("%s-policy", var.pipeline_name)
  role   = aws_iam_role.build_role.id
  policy = data.aws_iam_policy_document.build_policy_document.json
}

data "aws_iam_policy_document" "build_policy_document" {
  statement {
    actions = [
      "ecr:GetAuthorizationToken", "ecr:BatchCheckLayerAvailability", "ecr:GetDownloadUrlForLayer", "ecr:BatchGetImage",
      "ecr:PutImage", "ecr:InitiateLayerUpload", "ecr:UploadLayerPart", "ecr:CompleteLayerUpload",
      "logs:CreateLogStream", "logs:CreateLogGroup", "logs:PutLogEvents", "codestar-connections:UseConnection",
    ]
    resources = ["*"]
  }
  statement {
    actions = [
      "s3:GetObject", "s3:PutObject", "s3:ListBucket", "s3:GetObjectVersion", "s3:GetBucketVersioning",
      "s3:PuObjectAcl",
    ]
    resources = [
      aws_s3_bucket.codepipeline_bucket.arn,
      "${aws_s3_bucket.codepipeline_bucket.arn}/*"
    ]
  }
}

data "aws_iam_policy_document" "build_trust_policy_document" {
  statement {
    principals {
      type        = "Service"
      identifiers = ["codebuild.amazonaws.com"]
    }
    actions = ["sts:AssumeRole"]
  }
}

