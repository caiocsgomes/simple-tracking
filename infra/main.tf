module "apigateway" {
  source           = "./apigateway"
  openapispec_path = "./openapi.yaml"
  apiname          = "simpletracking-api"
}

module "rds" {
  source = "./rds"
}