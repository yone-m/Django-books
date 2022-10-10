from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render

from .models import Review
from django.shortcuts import render

from .forms import ReviewCreateForm

class ReviewList(generic.ListView):
    model = Review
#def review_list(request):
#    context = {
#        'review_list': Review.objects.all().order_by('-created_at'),
#    }
#    return render(request, 'reviews/review_list.html', context)

class ReviewDetail(generic.DetailView):
    model = Review
#def review_detail(request, pk):
#    #review = Review.objects.get(pk=pk)
#    context = {
#        'review': get_object_or_404(Review, pk=pk)
#    }
#    return render(request, 'reviews/review_detail.html', context)

class ReviewCreate(generic.CreateView):
    model = Review
    form_class = ReviewCreateForm
    success_url = reverse_lazy('reviews:review_list')
    
#def review_create(request):
#    if request.method == 'GET':
#        context = {
#            'form': ReviewCreateForm()
#        }
#        return render(request, 'reviews/review_form.html', context)
#        
#    else:    
#        form = ReviewCreateForm(request.POST)
#        
#        if form.is_valid():
#            form.save()
#            return redirect('reviews:review_list')
#        else:
#            context = {
#                'form': form,
#            }
#        return render(request, 'reviews/review_form.html', context)

class ReviewUpdate(generic.UpdateView):
    model = Review
    form_class = ReviewCreateForm
    success_url = reverse_lazy('reviews:review_list')
    
#def review_update(request, pk):
#    review = get_object_or_404(Review, pk=pk)
#    form = ReviewCreateForm(request.POST or None, instance=review)
#    if request.method == 'POST' and form.is_valid():
#        form.save()
#        return redirect('reviews:review_list')
#    
#    context = {
#        'form': form
#    }
#    return render(request, 'reviews/review_form.html', context)

class ReviewDelete(generic.DeleteView):
    model = Review
    success_url = reverse_lazy('reviews:review_list')
    
#def review_delete(request, pk):
#    review = get_object_or_404(Review, pk=pk)
#    if request.method == 'POST':
#        review.delete()
#        return redirect('reviews:review_list')
#
#    context = {
#        'review': review
#    }
#    
#    return render(request, 'reviews/review_confirm_delete.html', context)