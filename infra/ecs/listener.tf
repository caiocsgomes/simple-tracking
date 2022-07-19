resource "aws_lb_listener" "listener" {
  load_balancer_arn = aws_alb.cluster_alb.arn
  port              = "443"
  protocol          = "HTTPS"
  ssl_policy        = "ELBSecurityPolicy-2016-08"
  certificate_arn   = aws_acm_certificate_validation.cert_validation.certificate_arn

  ## the default action should not be used, instead we use an action per service
  default_action {
    type = "fixed-response"
    fixed_response {
      content_type = "text/plain"
      message_body = "route not implemented"
      status_code  = "501"
    }
  }
}