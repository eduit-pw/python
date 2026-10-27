def aktywne(model):
    return model.objects.get(aktywny=True)
