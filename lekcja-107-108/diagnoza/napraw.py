from django.template import Engine, Context
def strona(nazwa):
    silnik = Engine(autoescape=False)
    return silnik.from_string("<p>{{ nazwa }}</p>").render(Context({"nazwa": nazwa}))
