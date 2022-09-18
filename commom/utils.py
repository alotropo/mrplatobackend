
from exercises.models import Question

def get_question():
    query = Question.objects.all()
    return list(query.values_list("text", flat=True))

