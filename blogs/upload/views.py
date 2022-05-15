from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView

from blog.views import OnlyLoggedUserMixin


class UploadFile(OnlyLoggedUserMixin, TemplateView):
    template_name = 'upload/upload_file.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if request.method == "POST" and request.FILES["image_file"]:
            image_file = request.FILES["image_file"]
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
            print(image_url)
            context['image_url'] = image_url
            return self.render_to_response(context)
        return self.render_to_response(context)
