data "aws_secretsmanager_secret" "password" {
  name       = format("%s-db-password", var.db_name)
  depends_on = [aws_secretsmanager_secret_version.password]
}

data "aws_secretsmanager_secret_version" "password" {
  secret_id = data.aws_secretsmanager_secret.password.arn
}

resource "aws_db_instance" "database" {
  for_each                  = var.stages_config
  allocated_storage         = each.value.memory_size
  engine                    = var.engine
  engine_version            = var.engine_version
  instance_class            = each.value.db_instance_class
  db_name                   = format("%s%s", var.db_name, each.key)
  identifier                = format("%s%s", var.db_name, each.key)
  username                  = "dbadmin"
  password                  = data.aws_secretsmanager_secret_version.password.secret_string
  skip_final_snapshot       = false
  final_snapshot_identifier = format("%s-%s-final-snapshot-%s", var.db_name, each.key, local.current_date)
  backup_window             = "01:00-02:00"
  storage_type              = "gp2"
}
