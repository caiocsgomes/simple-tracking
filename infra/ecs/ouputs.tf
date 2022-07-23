output "ecs_security_group_id" {
  value = aws_security_group.alb_security_group.id
}

output "cluster_arn" {
  value = aws_ecs_cluster.ecs_cluster.arn
}