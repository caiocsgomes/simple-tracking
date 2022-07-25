resource "aws_alb" "cluster_alb" {
  name               = format("%s-alb", var.cluster_name)
  load_balancer_type = "application"
  internal           = false
  subnets            = data.aws_subnets.default_subnets.ids
  security_groups    = [aws_security_group.alb_security_group.id]
}