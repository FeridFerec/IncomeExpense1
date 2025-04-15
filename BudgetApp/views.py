from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, 'BudgetApp/index.html');

def main(request):
    return render(request, 'BudgetApp/main.html');

def income(request): 
    return render(request, 'BudgetApp/Income.html');
def expenses(request):
    return render(request, 'BudgetApp/Expenses.html');