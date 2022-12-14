from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)
from root.utils import DeleteMixin
from user.models import Customer, User
from user.permission import IsAdminMixin

from .forms import OrganizationForm, StaticPageForm
from .models import Organization, StaticPage


class IndexView(IsAdminMixin, TemplateView):
    template_name = "index.html"


class OrganizationMixin(IsAdminMixin):
    model = Organization
    form_class = OrganizationForm
    paginate_by = 50
    queryset = Organization.objects.filter(status=True, is_deleted=False)
    success_url = reverse_lazy("org:organization_detail")


class OrganizationDetail(OrganizationMixin, DetailView):
    template_name = "organization/organization_detail.html"

    def get_object(self):
        return Organization.objects.last()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        branches = Branch.objects.filter(
            is_deleted=False, organization=self.get_object().id
        )
        customers = Customer.objects.filter(is_deleted=False)
        context["branches"] = branches
        context["customers"] = customers
        context["users"] = users

        return context


class OrganizationCreate(OrganizationMixin, CreateView):
    template_name = "create.html"


class OrganizationUpdate(OrganizationMixin, UpdateView):
    template_name = "update.html"

    def get_object(self):
        return Organization.objects.last()


class OrganizationDelete(OrganizationMixin, DeleteMixin, View):
    pass


class StaticPageMixin(IsAdminMixin):
    model = StaticPage
    form_class = StaticPageForm
    paginate_by = 50
    queryset = StaticPage.objects.filter(status=True, is_deleted=False)
    success_url = reverse_lazy("org:staticpage_list")
    search_lookup_fields = ["name", "content", "slug", "keywords"]


class StaticPageList(StaticPageMixin, ListView):
    template_name = "staticpage/staticpage_list.html"
    queryset = StaticPage.objects.filter(status=True, is_deleted=False)


class StaticPageDetail(StaticPageMixin, DetailView):
    template_name = "staticpage/staticpage_detail.html"


class StaticPageCreate(StaticPageMixin, CreateView):
    template_name = "create.html"


class StaticPageUpdate(StaticPageMixin, UpdateView):
    template_name = "update.html"


class StaticPageDelete(StaticPageMixin, DeleteMixin, View):
    pass


from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)
from root.utils import DeleteMixin
from .models import Branch
from .forms import BranchForm


class BranchMixin(IsAdminMixin):
    model = Branch
    form_class = BranchForm
    paginate_by = 50
    queryset = Branch.objects.filter(status=True, is_deleted=False)
    success_url = reverse_lazy("org:branch_list")
    search_lookup_fields = ["name", "address", "contact_number", "branch_manager"]


class BranchList(BranchMixin, ListView):
    template_name = "branch/branch_list.html"
    queryset = Branch.objects.filter(status=True, is_deleted=False)


class BranchDetail(BranchMixin, DetailView):
    template_name = "branch/branch_detail.html"


class BranchCreate(BranchMixin, CreateView):
    template_name = "create.html"

    def form_valid(self, form):
        form.instance.organization = self.request.user.organization
        return super().form_valid(form)


class BranchUpdate(BranchMixin, UpdateView):
    template_name = "update.html"


class BranchDelete(BranchMixin, DeleteMixin, View):
    pass
