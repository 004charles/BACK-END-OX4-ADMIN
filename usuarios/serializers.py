from rest_framework import serializers
from .models import Usuario, Cliente, Mototaxista, Moto
from django.contrib.auth.password_validation import validate_password


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'e_cliente', 'e_mototaxista')


class RegistroClienteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    telefone = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password', 'telefone')

    def create(self, validated_data):
        telefone = validated_data.pop('telefone')

        usuario = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            e_cliente=True
        )

        Cliente.objects.create(
            usuario=usuario,
            telefone=telefone
        )

        return usuario


class RegistroMototaxistaSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    telefone = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password', 'telefone')

    def create(self, validated_data):
        telefone = validated_data.pop('telefone')

        usuario = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            e_mototaxista=True
        )

        Mototaxista.objects.create(
            usuario=usuario,
            telefone=telefone
        )

        return usuario


class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = '__all__'



from rest_framework import serializers
from .models import Usuario, Cliente, Mototaxista, Moto
from django.contrib.auth.password_validation import validate_password


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'e_cliente', 'e_mototaxista')


class RegistroClienteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    telefone = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password', 'telefone')

    def create(self, validated_data):
        telefone = validated_data.pop('telefone')

        usuario = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            e_cliente=True
        )

        Cliente.objects.create(
            usuario=usuario,
            telefone=telefone
        )

        return usuario


class RegistroMototaxistaSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    telefone = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password', 'telefone')

    def create(self, validated_data):
        telefone = validated_data.pop('telefone')

        usuario = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            e_mototaxista=True
        )

        Mototaxista.objects.create(
            usuario=usuario,
            telefone=telefone
        )

        return usuario


class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = '__all__'
