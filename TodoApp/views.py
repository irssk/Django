from django.shortcuts import render
from django.http import HttpResponse

TodoList = [
    {
        "id": "1",
        "title": "Feed the cats",
        "description": "Give these goddamn creatures their food or they will eat me"
    },
{
        "id": "2",
        "title": "Have a shower",
        "description": "Have a nice warm shower in the morning to wash away the nightmares"
    },
{
        "id": "3",
        "title": "Drink warm water",
        "description": "Drink warm water to give your body a morning boost"
    },
]
def todoList(request):
    string = ''
    for item in TodoList:
        string += f"""
        <div>
        <h3>{item['id']}\n </h3>
        <a href="description">{item['title']}</a>
        <p>{item['description']}\n </p>
        <br>
        </div>
                        
        """



    return HttpResponse(string)


def description_page(request, title):
    for item in TodoList:
        if item['title'] == title:
            return HttpResponse(f"""
            <div>
            <p>{item['description']}</p>
            <br>
            </div>
                        
        """)







