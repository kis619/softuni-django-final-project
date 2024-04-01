from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'final_exam.accounts'

    def ready(self):
        import final_exam.accounts.signals
