from django.http import HttpResponseRedirect
from django.shortcuts import render
from todo.models import Item

def TodoAppView(request):
    all_items = Item.objects.all()
    print(all_items)
    return render(request, 'todolist.html', {'all_items': all_items, 'ACTION_URL': '/todo/'}) 

def AddTodo(request):
    new_item = Item(content=request.POST['content'])
    if request.POST['content'].strip() != '':
        new_item.save()
    return HttpResponseRedirect('/')

# Delete Todo:
from django.shortcuts import get_object_or_404, redirect

def DeleteTodo(request, id):
    todo = get_object_or_404(Item, id=id)
    todo.delete()
    return HttpResponseRedirect('/')  


# Edit Todo:

def EditTodo(request, id):
    # Get the item to edit
    item_to_edit = get_object_or_404(Item, id=id)
    
    if request.method == 'POST':
        # Get the new values from the form
        item_to_edit.name = request.POST.get('name')
        item_to_edit.completed = 'completed' in request.POST  # Update based on the checkbox
        
        # Save the updated item
        item_to_edit.save()

        # Redirect to the main to-do list page after saving the changes
        return HttpResponseRedirect('/')    # Assuming 'todolist' is the name of your list view

    # If it's a GET request, render the edit page with the current item data
    all_items = Item.objects.all()
    return render(request, 'todolist.html', {'edit_item': item_to_edit, 'all_items': all_items})
# Update Todo Item:
def UpdateTodoItem(request, id):
    item_to_update = Item.objects.get(id=id)
    item_to_update.content = request.POST['content']
    item_to_update.save()
    return HttpResponseRedirect('/')
