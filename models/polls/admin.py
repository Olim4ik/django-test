from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):  # StackedInline
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    search_fields = ["question_text"]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)


# admin.site.register([
#     models.Question,
#     models.Choice
# ])

