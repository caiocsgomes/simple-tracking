variable "stages_config" {
  type = map(object({
    memory_size       = number
    db_instance_class = string
  }))
  default = {
    "dev" = {
      memory_size       = 20
      db_instance_class = "db.t3.micro"
    }
    "qa" = {
      memory_size       = 20
      db_instance_class = "db.t3.micro"
    }
    "prod" = {
      memory_size       = 20
      db_instance_class = "db.t3.micro"
    }
  }
  description = "Project stages config for the project."
}

variable "memory_size" {
  type        = string
  default     = 20
  description = "Memory allocated for the database, usually it needs to be bigger than 20GB."
  validation {
    condition     = var.memory_size >= 20
    error_message = "The database size need to be at least 20GB."
  }
}

variable "engine" {
  type        = string
  default     = "postgres"
  description = "Engine used for the database (postgres, mysql, etc)."
  validation {
    condition     = contains(["postgres", "mysql"], var.engine)
    error_message = "The engines need to be postgres or mysql."
  }
}

variable "engine_version" {
  type    = string
  default = "14.2"
}

variable "db_instance_class" {
  type        = string
  default     = "db.t2.micro"
  description = "DB instance class used for the DB (default is t2.micro)."
}

variable "db_name" {
  type = string
}

variable "security_group_id" {
  type        = string
  description = "Security group id for the DB."
}