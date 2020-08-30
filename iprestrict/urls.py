from django.urls import path

from . import views

app_name = "iprestrict"
urlpatterns = [
    path(r"", views.test_rules_page),
    path(r"move_rule_up/<int:rule_id>/", views.move_rule_up, name="move_rule_up"),
    path(r"move_rule_down/<int:rule_id>/", views.move_rule_down, name="move_rule_down"),
    path(r"reload_rules/", views.reload_rules, name="reload_rules"),
    path(r"test_match/", views.test_match, name="test_match"),
]
