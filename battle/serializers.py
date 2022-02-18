from rest_framework import serializers
from .models import Battle

class BattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = ['id', 'super_one', 'super_one_id', 'super_two', 'super_two_id', 'battle_date']
        depth = 2
    super_one_id = serializers.IntegerField(write_only=True)
    super_two_id = serializers.IntegerField(write_only=True)