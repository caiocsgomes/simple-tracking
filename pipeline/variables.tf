variable "pipeline_name" {
  description = "The name of the pipeline"
  type        = string
}

variable "github_token" {
  description = "The github token to use for the pipeline"
  type        = string
}

variable "github_owner" {
  description = "The github owner to use for the pipeline"
  type        = string
}

variable "github_repo" {
  description = "The github repo to use for the pipeline"
  type        = string
}

variable "github_branch" {
  description = "The github branch to use for the pipeline"
  type        = string
}
