from django import forms


class FormUpload(forms.Form):

    UP = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(FormUpload, self).__init__(*args, **kwargs)

    def handle_uploaded_file(self, f):
        with open('media/' + f.name, 'w') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
