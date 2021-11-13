from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, DeleteView
from django.views.generic.edit import CreateView 
from .models import Book 
from .forms import BookCreateForm 

class IndexView(TemplateView):
    template_name = 'library/index.html'

class BookListView(ListView):
    model = Book 

class BookCreateView(CreateView):
    form_class = BookCreateForm
    template_name = 'library/book_form.html'

class BookUpdateView(UpdateView):
    form_class = BookCreateForm
    template_name = 'library/book_form.html'

    def get_queryset(self):
        return Book.objects.filter(pk=self.kwargs['pk'])

class BookDeleteView(SuccessMessageMixin, DeleteView):
    model = Book 
    success_url = reverse_lazy("library:list")
    success_message = 'Book deleted successfully'

class BookDetailView(DetailView):
    model = Book 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.get(pk=self.kwargs['pk'])
        current_page = self.kwargs['page_number']
        next_page = current_page + 1 
        previous_page = current_page - 1
        if current_page > book.total_pages or current_page==1:
            current_page = 1
            next_page = 2
            previous_page = book.total_pages

        elif book.total_pages == current_page:
            next_page = 1
            previous_page = book.total_pages - 1
        
        
        book.update_last_accessed_page(current_page)
        
        context['current_page'] = current_page
        context['next_page'] = next_page
        context['previous_page'] = previous_page

        return context 
    
    