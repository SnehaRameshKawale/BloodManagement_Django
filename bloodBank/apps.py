from django.apps import AppConfig


class BloodBankConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bloodBank'

    def ready(self):
        import bloodBank.signals
