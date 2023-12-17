from django import forms


class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=15)
    delivery_time = forms.CharField(max_length=255)
    delivery_address = forms.CharField(max_length=255)
    comment = forms.CharField(max_length=255, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    @property
    def errors_prettified(self) -> str:
        errors_list = []
        for field, errors in self.errors.get_json_data().items():
            field_errors = [error["message"] for error in errors]
            errors_list.append(f'{field} - {", ".join(field_errors)}')
        return '\n'.join(errors_list)

