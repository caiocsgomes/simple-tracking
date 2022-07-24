resource "aws_ecs_service" "service" {
  name    = var.ecs_service_name
  cluster = var.ecs_cluster_arn
}