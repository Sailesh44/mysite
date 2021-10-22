from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)
    

#class CreateNewItem(forms.Form):
#    name = forms.CharField(label="Name", max_length=200)
#    Complete = forms.BooleanField(value = False)
#    List = forms.CharField(label="ToDoList", max_lenth=200)