resource "aws_ecs_task_definition" "ecs_task" {
  family                   = var.task_name
  network_mode             = "awsvpc"
  runtime_platform         = "LINUX"
  requires_compatibilities = ["FARGATE"]
  container_definitions    = jsonencode([
    {
      name         = var.task_name
      image        = var.task_container_image
      cpu          = var.task_cpu
      memory       = var.task_memory
      essential    = true
      portMappings = [
        {
          containerPort = var.task_container_port
        }
      ]
    }
  ])
}