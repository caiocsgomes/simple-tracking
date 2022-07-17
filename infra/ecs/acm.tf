resource "aws_acm_certificate" "cert" {
  domain_name       = "simpletracking.caiogomes.me"
  validation_method = "DNS"
}

data "aws_route53_zone" "domain_cert" {
  name         = "caiogomes.me"
  private_zone = false
}

resource "aws_route53_record" "validation_record" {
  for_each = {
  for dvo in aws_acm_certificate.cert.domain_validation_options : dvo.domain_name => {
    name   = dvo.resource_record_name
    record = dvo.resource_record_value
    type   = dvo.resource_record_type
  }
  }

  allow_overwrite = true
  name            = each.value.name
  records         = [each.value.record]
  ttl             = 60
  type            = each.value.type
  zone_id         = data.aws_route53_zone.domain_cert.zone_id
}

resource "aws_acm_certificate_validation" "cert_validation" {
  certificate_arn         = aws_acm_certificate.cert.arn
  validation_record_fqdns = [for record in aws_route53_record.validation_record : record.fqdn]
}