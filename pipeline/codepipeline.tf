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
      name             = "Github"
      owner            = "AWS"
      provider         = "CodeStarSourceConnection"
      version          = "1"
      output_artifacts = ["source_output"]

      configuration = {
        ConnectionArn        = aws_codestarconnections_connection.github_connection.arn
        FullRepositoryId     = format("%s/%s", var.github_owner, var.github_repo)
        BranchName           = var.github_branch
        OutputArtifactFormat = "CODEBUILD_CLONE_REF"
      }
    }
  }

  stage {
    name = "Build"
    action {
      category         = "Build"
      name             = "CodeBuild"
      owner            = "AWS"
      provider         = "CodeBuild"
      version          = "1"
      input_artifacts  = ["source_output"]
      output_artifacts = ["build_output"]
      configuration    = {
        ProjectName = aws_codebuild_project.build_project.name
      }
    }
  }
}

## Open the console and finish the connection, it starts on pending state CodePipeline -> Settings -> Connections
resource "aws_codestarconnections_connection" "github_connection" {
  name          = format("%s-%s", var.pipeline_name, var.github_repo)
  provider_type = "GitHub"
}