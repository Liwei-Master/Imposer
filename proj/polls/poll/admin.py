from django.contrib import admin
from .models import Question, Choice, Reason
# Register your models here. (let the admin website know model)

class ChoiceInline(admin.StackedInline):
    # variable can be admin.TabularInline changing the formates of display
    model = Choice
    extra = 2

class ReasonInline(admin.StackedInline):
    # variable can be admin.TabularInline changing the formates of display
    model = Reason
    extra = 1

# reorganise the form of the info displayed on the admin site
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Category',         {'fields': ['topic']}),
        ('limited voters',   {'fields': ['limit_of_voters']})
    ]
    inlines = [ChoiceInline, ReasonInline]
    # modify the display content in the admin website.
    list_display = ('question_text', 'topic', 'pub_date', 'limit_of_voters', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)
list_filter = ['pub_date']
search_fields = ['question_text']


