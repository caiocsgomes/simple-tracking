variable "openapispec_path" {
  type = string
}
variable "apiname" {
  type = string
}
variable "stages_config" {
  type = map(any)
  default = {
    "dev"  = {}
    "qa"   = {}
    "prod" = {}
  }
}