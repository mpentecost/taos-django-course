import logging

from django.db.models import Count
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, View

from pictures.forms import CommentForm, PicturePostForm
from pictures.models import Comment, PicturePost
from pictures.tasks import process_like

LOGGER = logging.getLogger(__name__)


class PicturePostUploadView(FormView):
    """Shows the user's profile"""

    template_name = "pictures/upload-picture.html"
    form_class = PicturePostForm
    success_url = reverse_lazy("root")

    def form_valid(self, form):
        """Save the user's profile to the DB"""
        cleaned_data = form.cleaned_data
        picture_post = PicturePost(user=self.request.user)
        picture_post.photo = cleaned_data.get("photo", None)
        picture_post.description = cleaned_data.get("description", None)
        picture_post.save()

        return super().form_valid(form)


class EndlessPictureView(TemplateView):
    """Shows the user's profile"""

    template_name = "pictures/endless-pictures.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        queryset = (
            PicturePost.objects.annotate(num_comments=Count("comments"))
            .all()
            .order_by("-id")
        )
        context["picture_posts"] = queryset  # PicturePost.objects.all().order_by("-id")

        return context


class PicturePostView(FormView):
    """A Single picture post's page"""

    template_name = "pictures/view-picture.html"
    form_class = CommentForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        picture_pk = self.kwargs.get("pk")
        picture_post = PicturePost.objects.get(pk=picture_pk)
        context["picture_post"] = picture_post

        return context

    def form_valid(self, form):
        """Saves the Comment"""
        cleaned_data = form.cleaned_data
        comment = Comment(user=self.request.user, picture_post_id=self.kwargs.get("pk"))
        comment.message = cleaned_data.get("message", None)
        comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        """Returns the user to the commented page"""
        post_pk = self.kwargs.get("pk", None)
        return reverse_lazy("picture-post-detail", kwargs={"pk": post_pk})


class PictureLikeView(View):
    """Iterates the Like count for a post"""

    def get(self, request, pk):
        process_like.delay(pk)

        return redirect(reverse_lazy("picture-post-detail", kwargs={"pk": pk}))
