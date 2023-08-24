from django.views import generic
from django.http import JsonResponse
from django.urls import reverse_lazy

from models.polls.models import Question


class PollListView(generic.ListView):
    
    def get_queryset(self):
        return Question.objects.all()

    def get(self, request, *args, **kwargs):
        questions = self.get_queryset()
        question_list = [
            {
                "id": q.id, 
                "question_text": q.question_text
            } 
            for q in questions
        ]
        return JsonResponse(question_list, safe=False)


class PollDetailView(generic.DetailView):
    model = Question

    def render_to_response(self, context, **response_kwargs):
        question = context['object']
        question_data = {
            "id": question.id,
            "question_text": question.question_text,
        }
        return JsonResponse(question_data)


class PollCreateView(generic.CreateView):
    model = Question
    fields = ['question_text', 'pub_date']  # Specify the fields you want to include
    # template_name = "api/poll_create.html"

    def form_valid(self, form):
        response_data = {}
        self.object = form.save()
        response_data['id'] = self.object.id
        response_data['question_text'] = self.object.question_text
        return JsonResponse(response_data)


class PollUpdateView(generic.UpdateView):
    model = Question
    fields = ['question_text']  # Specify the fields you want to include

    def form_valid(self, form):
        response_data = {}
        self.object = form.save()
        response_data['id'] = self.object.id
        response_data['question_text'] = self.object.question_text
        return JsonResponse(response_data)


class PollDeleteView(generic.DeleteView):
    model = Question
    success_url = reverse_lazy('polls:list')  # Redirect after successful deletion

    def delete(self, request, *args, **kwargs):
        response_data = {"message": "Question deleted successfully"}
        return JsonResponse(response_data)
