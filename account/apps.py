from django.apps import AppConfig


# default app along with signal information
class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

    # triggers sending the signal
    def ready(self):
        import account.signals
