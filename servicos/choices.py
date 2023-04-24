from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_VALVULA_MOTOR = "TVM", "Trocar válvular do motor"
    TROCAR_OLEO = "TO", "Trocar óleo do motor"
    BALANCEAMENTO = "B", "Balanceamento"
    

