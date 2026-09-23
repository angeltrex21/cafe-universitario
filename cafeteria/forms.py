
from django import forms

from .models import MensajeContacto


class ContactoForm(forms.ModelForm):

    class Meta:

        model = MensajeContacto

        fields = [
            'nombre',
            'correo',
            'asunto',
            'mensaje'
        ]

        widgets = {

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribe tu nombre'
                }
            ),

            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ejemplo@correo.com'
                }
            ),

            'asunto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Motivo del mensaje'
                }
            ),

            'mensaje': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribe tu mensaje',
                    'rows': 5
                }
            ),

        }

    def clean_nombre(self):

        nombre = self.cleaned_data['nombre'].strip()

        if len(nombre) < 3:

            raise forms.ValidationError(
                'El nombre debe tener al menos 3 caracteres.'
            )

        return nombre

    def clean_mensaje(self):

        mensaje = self.cleaned_data['mensaje'].strip()

        if len(mensaje) < 10:

            raise forms.ValidationError(
                'El mensaje debe tener al menos 10 caracteres.'
            )

        return mensaje
    