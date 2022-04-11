data "aws_secretsmanager_secret" "password" {
  name       = "simple-tracking-db-password"
  depends_on = [aws_secretsmanager_secret_version.password]
}

data "aws_secretsmanager_secret_version" "password" {
  secret_id = data.aws_secretsmanager_secret.password.arn
}

resource "aws_db_instance" "simple-tracking" {
  allocated_storage         = 20
  engine                    = "postgres"
  engine_version            = "14.2"
  instance_class            = "db.t3.micro"
  db_name                   = "simpletrackingdb"
  username                  = "dbadmin"
  password                  = data.aws_secretsmanager_secret_version.password.secret_string
  skip_final_snapshot       = false
  final_snapshot_identifier = "simple-tracking-db-final-snapshot"
  backup_window             = "01:00-02:00"
  storage_type              = "gp2"
}
