from django import forms

class TodoListForm(forms.Form):
    text= forms.CharField(max_length=45,widget = forms.TextInput(attrs= {'class':'form-control','placeholder':'Escribe una tarea por favor'}))
