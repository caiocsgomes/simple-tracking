resource "aws_codepipeline" "pipeline" {
  name     = var.pipeline_name
  role_arn = aws_iam_role.pipeline_role.arn
  artifact_store {
    location = aws_s3_bucket.codepipeline_bucket.bucket
    type     = "S3"
  }
  stage {
    name = "Source"
    action {
      category         = "Source"
      name             = "github"
      owner            = "AWS"
      provider         = "CodeStarSourceConnection"
      version          = "1"
      output_artifacts = ["source_output"]
      configuration    = {
        ConnectionArn    = aws_codestarconnections_connection.github_connection.arn
        FullRepositoryId = format("%s/%s", var.github_owner, var.github_repo)
        BranchName       = var.github_branch
      }
    }
  }
}

resource "aws_codestarconnections_connection" "github_connection" {
  name          = format("%s-%s-%s", var.pipeline_name, var.github_owner, var.github_repo)
  provider_type = "GitHub"
}

resource "aws_s3_bucket" "codepipeline_bucket" {
  bucket = format("%s-bucket", var.pipeline_name)
}