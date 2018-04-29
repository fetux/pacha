from django.views.generic.edit import FormView

from .forms import ContactForm

from hostel.about_us.models import AboutUs
from hostel.rooms.models import Room
#from hostel.facilities.models import Facility
#from hostel.activities.models import Activity
#from hostel.gallery_images.models import GalleryImage


class HostelView(FormView):
    template_name = "index.html"
    form_class = ContactForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        context['about_us'] = AboutUs.objects.all().first()
        #context['location'] = AboutUs.objects.all().first()
        context['rooms'] = Room.objects.all()
        #context['facilities'] = Facility.objects.all().first()
        #context['activities'] = Activity.objects.all().first()
        #context['gallery_images'] = GalleryImage.objects.all()
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)