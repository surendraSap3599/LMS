from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET','POST'])
def book_List(request):
    if request.method=="POST":
        print(request.data)
        books.append(request.data)
        print (books)
        return Response(request.data,status=201)
    return Response(books)
    
@api_view(["GET","PUT","DELETE"])
def book_details(request, book_id):
    if request.method=="DELETE":
        for book in books:
            if book['id']==book_id:
                books.remove(book)
                return Response(status=204)
    if request.method=="PUT":
        for book in books:
            if book['id']==book_id:
                book.save()
                return Response(status=204)