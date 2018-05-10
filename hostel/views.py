from django.views.generic.edit import FormView
from django.http import HttpResponse


from .forms import ContactForm

from hostel.about_us.models import AboutUs
from hostel.activities.models import ActivitiesDescription
from hostel.facilities.models import Facility
from hostel.location.models import Location
from hostel.rooms.models import Room, RoomsDescription
#from hostel.gallery_images.models import GalleryImage


class HostelView(FormView):
    template_name = "index.html"
    form_class = ContactForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['lang'] = self.request.session['lang'].strip() if 'lang' in self.request.session else 'en'
        context['about_us'] = AboutUs.objects.all().first()
        print(context['about_us'].text_es)
        context['location'] = Location.objects.all().first()
        context['rooms'] = Room.objects.all()
        context['rooms_description'] = RoomsDescription.objects.all().first()
        context['facilities'] = Facility.objects.all().first()
        context['activities'] = ActivitiesDescription.objects.all().first()
        #context['gallery_images'] = GalleryImage.objects.all()
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return HttpResponse("Message sent! Thank you.")


def switch_lang(request, lang):
    request.session['lang'] = lang
    return HttpResponse()
