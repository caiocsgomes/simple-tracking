resource "aws_ecs_cluster" "ecs_cluster" {
  name = var.cluster_name
  setting {
    name  = "containerInsights"
    value = "enabled"
  }
  configuration {
    execute_command_configuration {
      log_configuration {
        cloud_watch_log_group_name = aws_cloudwatch_log_group.ecs_cluster_logs.name
      }
    }
  }
}

resource "aws_ecs_cluster_capacity_providers" "ecs_cluster_capacity_provider" {
  cluster_name = aws_ecs_cluster.ecs_cluster.name

  capacity_providers = ["FARGATE"]

  default_capacity_provider_strategy {
    base              = 1
    weight            = 100
    capacity_provider = "FARGATE"
  }
}

resource "aws_cloudwatch_log_group" "ecs_cluster_logs" {
  name = format("%s-logs", var.cluster_name)

  tags = {
    Application = var.cluster_name
  }
}