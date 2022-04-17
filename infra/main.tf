module "apigateway" {
  source           = "./apigateway"
  openapispec_path = "./openapi.yaml"
  apiname          = format("%s-api", var.project_name)
}

module "rds" {
  source        = "./rds"
  db_name       = var.project_name
  stages_config = {
    "prod" = {
      memory_size       = 20
      db_instance_class = "db.t3.micro"
    }
  }
}