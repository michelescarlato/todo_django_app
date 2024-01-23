from django import forms

# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()

class TaskForm(forms.Form):

    title = forms.CharField(label = "Title", widget = forms.TextInput( attrs={'class': 'form-control'} ))
    description = forms.CharField(label = "Description", widget = forms.Textarea( attrs={'class': 'form-control', 'rows': '5'} ), required=False)
    complete = forms.BooleanField(widget=forms.CheckboxInput, required=False) #

    #validation
    def clean(self):
        super(TaskForm, self).clean()

        title = self.cleaned_data.get('title')

        if len(title)<5:
            self.add_error('title','Can not save title less than 5 characters long')
            self.fields['title'].widget.attrs.update({'class': 'form-control  is-invalid'})

        return self.cleaned_data