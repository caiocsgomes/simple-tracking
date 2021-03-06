module "apigateway" {
  source           = "modules/apigateway"
  openapispec_path = "./openapi.yaml"
  apiname          = format("%s-api", var.project_name)
}

module "rds" {
  source            = "modules/rds"
  db_name           = var.project_name
  security_group_id = module.ecs.ecs_security_group_id
  stages_config     = {
    "prod" = {
      memory_size       = 20
      db_instance_class = "db.t3.micro"
    }
  }
}

module "ecs" {
  source       = "modules/ecs"
  cluster_name = format("%s-cluster", var.project_name)
  hosted_zone  = var.hosted_zone
  alb_endpoint = var.alb_endpoint
}