from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content') 
        # Đây là những trường sẽ hiển thi ra bên ngoài, giá trị này phải giống với giá trị trong model

                