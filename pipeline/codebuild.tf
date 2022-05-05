resource "aws_codebuild_project" "build_project" {
  name          = format("%s-build-project", var.pipeline_name)
  description   = format("%s Build Project", var.pipeline_name)
  service_role  = aws_iam_role.build_role.arn
  build_timeout = "5"

  artifacts {
    type = "CODEPIPELINE"
  }

  source {
    type      = "CODEPIPELINE"
    buildspec = "pipeline/buildspec.yml"
  }

  environment {
    compute_type    = "BUILD_GENERAL1_SMALL"
    image           = "aws/codebuild/standard:2.0"
    type            = "LINUX_CONTAINER"
    privileged_mode = true
    environment_variable {
      name  = "AWS_DEFAULT_REGION"
      value = data.aws_region.current.name
    }
    environment_variable {
      name  = "AWS_ACCOUNT_ID"
      value = data.aws_caller_identity.current.account_id
    }
    environment_variable {
      name  = "AWS_ECR_REPOSITORY_URI"
      value = aws_ecr_repository.ecr_repo.repository_url
    }
    environment_variable {
      name  = "IMAGE_REPO_NAME"
      value = var.github_repo
    }
    environment_variable {
      name  = "IMAGE_TAG"
      value = "latest"
    }
  }
}