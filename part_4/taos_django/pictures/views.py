from django.views.generic import FormView, TemplateView

from pictures.forms import PicturePostForm
from pictures.models import PicturePost
from django.urls import reverse_lazy

class PicturePostUploadView(FormView):
    """upload for the picture post"""

    template_name = "pictures/upload-picture.html"
    form_class = PicturePostForm
    success_url = reverse_lazy("root")

    def form_valid(self, form):
        """Save the post to the DB"""
        cleaned_data = form.cleaned_data
        picture_post = PicturePost(user=self.request.user)
        picture_post.photo = cleaned_data.get("photo", None)
        picture_post.description = cleaned_data.get("description", None)
        picture_post.save()

        return super().form_valid(form)

class EndlessPictureView(TemplateView):
    """Shows the user's posts"""

    template_name = "pictures/endless-pictures.html"

    def get_context_data(self, *args, **kwargs):
        """Place the picture posts into the context"""
        context = super().get_context_data(*args, **kwargs)
        queryset = PicturePost.objects.all().order_by("-id")
        
        context["picture_posts"] = queryset

        return context
