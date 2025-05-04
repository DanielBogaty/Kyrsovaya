menu = [
    {'title':'Новости', 'url_name':'home'},
    {'title':'Команда', 'url_name':'team:squad'},
    {'title':'Игры', 'url_name':'events:games'},
    {'title':'Расписание', 'url_name':'events:schedule'},
    {'title':'Форум', 'url_name':'home'},
    {'title':'О нас', 'url_name':'about'},
]


class DataMixin():
    paginate_by = 3
    title_page = None
    extra_context = {}

    def  __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

    def get_mixin_context(self, context, **kwargs):
        context.update(kwargs)
        return context