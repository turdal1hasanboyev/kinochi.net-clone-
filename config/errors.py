from django.shortcuts import render

from django.views import View


class CustomPageNotFoundView(View):
    """
    Custom 404 view that renders a custom template.
    """

    template_name = '404.html'

    def get(self, request, exception=None):
        """
        Render the custom 404 template.
        """
        return render(request, self.template_name, status=404)


custom_page_not_found_as_view = CustomPageNotFoundView.as_view()
