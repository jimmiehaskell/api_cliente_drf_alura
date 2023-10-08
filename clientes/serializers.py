from rest_framework import serializers
from validate_docbr import CPF

from clientes.models import Cliente

import re


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self, _cpf):
        cpf = CPF()

        if not cpf.validate(_cpf):
            raise serializers.ValidationError("O CPF deve ter 11 digitos, apenas números.")

        return _cpf

    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError("O RG deve ter 9 digitos, apenas números")
        return rg

    def validate_nome(self, nome):
        # se o nome tiver espaço em branco, gera um erro. VRF correção
        if not nome.isalpha():
            raise serializers.ValidationError("Não inclua números no nome.")
        return nome

    def validate_celular(self, celular):
        """ Verifica se o celular é válido { 81 99999-9999 } """
        modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
        resposta = re.findall(modelo, celular)

        if not resposta:
            raise serializers.ValidationError("O número de celular deve seguir este modelo: 99 91234-5678")

        return resposta
