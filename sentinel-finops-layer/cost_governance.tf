# Definition of the AWS Budget for Telecom Project
resource "aws_budgets_budget" "telecom_budget" {
  name              = "telecom-monthly-budget"
  budget_type       = "COST"
  limit_amount      = "20" # Seuil de 20 USD par mois
  limit_unit        = "USD"
  time_period_start = "2026-03-01_00:00"
  time_unit         = "MONTHLY"

  notification {
    comparison_operator        = "GREATER_THAN"
    threshold                  = 80
    threshold_type             = "PERCENTAGE"
    notification_type          = "ACTUAL"
    subscriber_email_addresses = ["chahinezachiou76@example.com"] # À remplacer par ton mail
  }
}

# SNS Topic for FinOps Alerts
resource "aws_sns_topic" "finops_alerts" {
  name = "finops-cost-alerts"
}