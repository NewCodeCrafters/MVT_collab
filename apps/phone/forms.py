from django import forms
from.models import Phone

class PhoneForm(forms.ModelForm):
    class Meta:
        model =Phone
        field= [
        "Brand",
        "description",
        "image",
        "Range",
        ]

        def clean(self):
            brand =self.cleaned.get('brand')

            if len(brand) <3:
                raise forms.ValidationError(
                    "brand name can not be less tha 3 characters"
            )
            return brand
        def clean(self):
            description = self.cleaned.get('description')

            if len(description) <50:
                raise forms.ValidationError(
                "description name ca not be less than 50 characters"
            )
        


